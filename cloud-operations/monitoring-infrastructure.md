# Monitoring Infrastructure

## Overview

When operating cloud infrastructure, engineers require also need visibility into system behavior, application activity, infrastructure changes, and configuration state rather than just keeping resources available. This enables swift detection and investigation of abnormal conditions.

I used Amazon CloudWatch, AWS Systems Manager, Amazon EventBridge, Amazon SNS, and AWS Config to collect telemetry from an EC2 web server, centralize application logs, detect error conditions, monitor infrastructure changes, and evaluate resource compliance.

### Key Concepts

- **CloudWatch Agent** — Software running on the EC2 instance that collects host-level metrics and log files and sends them to CloudWatch.
- **CloudWatch Logs** — Centralizes application and system logs so they can be reviewed and monitored without directly accessing the instance.
- **Amazon EventBridge** — Detects discrete AWS infrastructure events and routes matching events to another service.
- **Amazon SNS** — Delivers notifications when monitored conditions or infrastructure events occur.
- **AWS Config** — Evaluates resource configuration against defined rules and reports compliant or noncompliant state.

### Lab Environment

AWS re/Start provided an EC2 web server and the supporting IAM permissions required for the monitoring workflow.

The infrastructure was already provisioned. My work focused on configuring the monitoring, alerting, and compliance layers around the running system.

## Configuring Host Monitoring with the CloudWatch Agent

I used AWS Systems Manager Run Command to configure and start the CloudWatch Agent on the web server.

The agent configuration was stored in Systems Manager Parameter Store and defined both the web server log files and the operating-system metrics that should be collected. The completed Run Command confirmed that the agent was successfully configured against the managed instance.

![CloudWatch Agent configured through Systems Manager](images/31-cloudwatch-agent-configured.png)

This established the telemetry pipeline between the running EC2 instance and CloudWatch without requiring manual configuration through an interactive server session.

## Centralized Application Logging

After the agent was running, the web server's access and error logs were shipped into CloudWatch Logs.

I generated a request for a nonexistent `/start` path and verified that the resulting HTTP `404` response appeared in the centralized access-log stream.

![Centralized web server logs in CloudWatch](images/32-cloudwatch-access-log-404.png)

This demonstrated how application logs can be collected centrally and reviewed without connecting directly to the instance.

## Detecting Application Errors with Logs and Alarms

I created a CloudWatch Logs metric filter that matched access-log entries with HTTP status code `404`.

Each matching event incremented a custom metric. I then created a CloudWatch alarm that evaluated the metric and entered the `ALARM` state after the number of errors crossed the configured threshold.

![CloudWatch alarm triggered by repeated 404 responses](images/33-cloudwatch-404-alarm.png)

The workflow connected application behavior to an operational signal:

```mermaid
flowchart LR
    A[Web Request] --> B[Access Log]
    B --> C[CloudWatch Logs]
    C --> D[Metric Filter]
    D --> E[Custom Metric]
    E --> F[CloudWatch Alarm]
```

Instead of requiring an operator to inspect logs manually, the monitoring system could detect the condition automatically.

## Monitoring Operating-System Metrics

I reviewed metrics collected by the CloudWatch Agent from inside the EC2 instance.

The `CWAgent` namespace exposed operating-system telemetry such as disk utilization and filesystem information that is not available from the standard EC2 service metrics alone.

![Operating-system metrics collected by the CloudWatch Agent](images/34-cloudwatch-agent-metrics.png)

This reinforced the distinction between platform-level metrics provided automatically by AWS and deeper host-level metrics collected from inside the instance.

## Detecting Infrastructure State Changes

I created an EventBridge rule that matched EC2 instance state-change events when an instance entered the `stopped` or `terminated` state.

![EventBridge rule for EC2 stopped or terminated events](images/35-eventbridge-ec2-state-rule.png)

The rule routed matching events to an SNS topic. After stopping the web server, I received an SNS notification containing the EC2 state-change event.

![SNS notification for an EC2 stopped event](images/36-ec2-state-change-notification.png)

```mermaid
flowchart LR
    A[EC2 State Change] --> B[EventBridge Rule]
    B --> C[SNS]
    C --> D[Notification]
```

Unlike metric-based monitoring, this workflow reacts directly to a discrete infrastructure event.

## Monitoring Configuration Compliance

I used AWS Config managed rules to evaluate whether resources matched defined configuration requirements.

The `required-tags` rule identified resources that did not contain the required `project` tag.

![AWS Config required-tags noncompliance](images/37-config-required-tags-noncompliance.png)

I also reviewed the `ec2-volume-inuse-check` rule, which identified an EBS volume that was not attached to an EC2 instance.

![AWS Config unattached EBS volume noncompliance](images/38-config-ebs-volume-noncompliance.png)

CloudWatch monitoring primarily answers questions about **what a system is doing**, while AWS Config evaluates whether **the system's configuration matches an expected policy state**. They provide two different forms of operational visibility: runtime behavior and configuration compliance.

## Operational Model

The lab demonstrated a broader monitoring workflow for running cloud systems:

1. **Instrument** — Configure the CloudWatch Agent to collect logs and host metrics.
2. **Observe** — Centralize telemetry in CloudWatch for system and application visibility.
3. **Detect** — Convert meaningful log patterns and infrastructure events into operational signals.
4. **Notify** — Route detected conditions through alarms and SNS.
5. **Evaluate** — Use AWS Config to compare resource configuration against expected policy.

```text
Running Cloud System
        │
        ▼
Collect telemetry
logs / host metrics
        │
        ▼
Observe system behavior
        │
        ├───────────────┐
        ▼               ▼
Detect runtime      Detect infrastructure
conditions          state changes
        │               │
        ▼               ▼
CloudWatch alarm    EventBridge
        │               │
        └───────┬───────┘
                ▼
             Notify
                │
                ▼
Evaluate configuration
with AWS Config
```

## Takeaways

- **Centralized telemetry reduces server-by-server operations.** CloudWatch made logs and system metrics available without requiring direct access to the instance.
- **Event-driven monitoring complements metric monitoring.** EventBridge detected discrete infrastructure changes that did not depend on a thresholded performance metric.
- **Compliance is a form of operational visibility.** AWS Config evaluated whether resources matched expected configuration rules rather than only reporting runtime behavior.
- **The operational goal is actionable visibility.** Useful monitoring should make abnormal state easier to detect, communicate, and investigate.
