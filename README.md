<img width="4747" height="970" alt="aws-restart-banner" src="https://github.com/user-attachments/assets/a668c6a6-3329-4b99-8621-be124a2d94c4" />

# AWS re/Start Portfolio

A collection of Cloud Engineering work from AWS re/Start intentionally selected to explore, develop deeper understanding, and hands-on experience across cloud infrastructure & operations, storage, databases, serverless, containers, and applied AI.

The work combines hands-on provisioning, configuration and validation with reasoning about system architecture and behavior.

| Domain | Focus |
| ------ | ----- |
| [**Elastic Compute Architecture**](./elastic-compute/) | Transforming an EC2 web server into a multi-AZ, load-balanced, health-aware, automatically scaling compute tier |
| [**Cloud Operations Engineering**](./cloud-operations/) | Operating EC2 fleets through centralized management, monitoring, compliance, security investigation, and proactive alerting |
| [**Storage & Recovery**](./storage-recovery/) | Managing persistent storage through EBS volumes, snapshots, restore workflows, S3 synchronization, and version recovery |
| [**Database Migration / Modernization**](./rds-migration/) | Application and database modernization through migration from instance-hosted relational data to Amazon RDS |
| [**Serverless & Event-Driven Architecture**](./serverless-event-driven/) | Building serverless workflows triggered by schedules and state-change events, managed services, and end-to-end validation |
| [**Containers & Orchestration**](./containers-orchestration/) | Deploying and orchestrating containerized workloads on Amazon ECS with EC2, desired state, task definitions, and Auto Scaling |
| [**Agentic AI Systems**](./agentic-ai/) | Generative AI solutions using Amazon Bedrock, grounded knowledge, model controls, and assistant-oriented workflows |

### Lab Environment

AWS re/Start labs use guided training environments with pre-provisioned resources. Each artifact documents the configuration, troubleshooting, validation, and technical work I performed within those environments.

## Shared Engineering Foundations

The portfolio is organized around distinct technical domains, but those domains don't capture the full range of engineering competencies demonstrated. The examples below illustrate how these shared foundations apply across different workloads and environments.

### Networking & Security Principles

- **Network segmentation and access boundaries:**
    - [Elastic Compute](./elastic-compute/) places internet-facing load balancers in public subnets while keeping application instances private.
    - [Database Migration](./rds-migration/) extends segmentation to a private database tier, restricting MySQL connectivity through security-group references.

- **Workload connectivity across compute models:**
    - [Serverless Reporting](./serverless-event-driven/serverless-reporting-workflow.md) connects Lambda to a private database through VPC networking and ENIs.
    - [Containers & Orchestration](./containers-orchestration/) uses ECS `awsvpc` networking to give tasks independent private IPs and security-group boundaries. 

- **Identity, permissions, and layered security:**
    - [Serverless Reporting](./serverless-event-driven/serverless-reporting-workflow.md) applies IAM execution roles and service permissions.
    - [CloudTrail Investigation](./cloud-operations/cloudtrail-investigation.md) connects AWS API activity, IAM identities, security-group exposure, and Linux authentication to investigate and remediate a security incident.  

### Architectural Reasoning

- **Workload and infrastructure boundaries:**
    - [Elastic Compute](./elastic-compute/) demonstrates EC2 fleet capacity managed through Auto Scaling.
    - [Containers & Orchestration](./containers-orchestration/) extends this distinction by separating ECS task desired state from EC2 host capacity, including the additional capacity needed during rolling deployments. 

- **Workload fit and execution models:**
    - [Serverless & Event-Driven Architecture](./serverless-event-driven/) uses scheduled and state-change triggers for intermittent workloads, reducing the need for continuously running compute while introducing dependencies across managed services.
    - [Containers & Orchestration](./containers-orchestration/) demonstrates a contrasting model for maintaining long-running application workloads. 

- **Separation of concerns and availability:**
    - [Database Migration](./rds-migration/) separates application compute from persistent database state, externalizes configuration through Parameter Store, and distinguishes a multi-AZ subnet group from a database deployment with Multi-AZ failover.  

### Linux Administration & CLI

- **Linux storage administration:**
    - [EBS Storage & Recovery](./storage-recovery/amazon-ebs.md) uses `mkfs`, `mount`, `/etc/fstab`, and filesystem inspection to transform attached block storage into a usable, persistent Linux filesystem.  

- **Host and runtime inspection:**
    - [Containers & Orchestration](./containers-orchestration/) uses Docker commands and `curl` to inspect running workloads and diagnose connectivity.
    - [CloudTrail Investigation](./cloud-operations/cloudtrail-investigation.md) examines Linux authentication logs, processes, users, and SSH configuration during incident investigation.  

- **Command-line infrastructure and data operations:**
    - [Database Migration](./rds-migration/) combines AWS CLI provisioning with `mysqldump` export and database restoration.
    - [Serverless Reporting](./serverless-event-driven/serverless-reporting-workflow.md) uses the AWS CLI to create and configure Lambda resources.

## ℹ️ About AWS re/Start

AWS re/Start is an official Amazon Web Services (AWS) workforce development training program designed to prepare learners for entry- to mid-level cloud careers, including roles such as systems administrator, cloud automation lead, infrastructure engineer, and more.

The program combines instructor-led learning, scenario-based exercises, and hands-on labs across Linux, Python, networking, security, databases, automation, and core AWS Cloud skills — delivered through collaborating organizations around the world. I attend the program in New York City through [Per Scholas](https://www.perscholas.org/locations/new-york/).

**View the official program site: [AWS re/Start](https://aws.amazon.com/training/restart/)**
