# Serverless & Containerized Workloads

## Labs

### [01 — Serverless Reporting Workflow](serverless-reporting-workflow.md)

Built and troubleshot an event-driven reporting workflow using AWS Lambda, EventBridge, Parameter Store, Amazon SNS, IAM, CloudWatch, and VPC networking. The workflow retrieves sales data from a MySQL database, generates a scheduled report, and delivers the result through SNS.

**Architecture:** EventBridge → Lambda orchestration → Lambda data extraction → MySQL → SNS