# Cloud Systems Operations

## About

AWS re/Start lab work covering centralized systems management, configuration, secure instance access, patching, and compliance with AWS Systems Manager.

The two labs are grouped because they address the same broader operational problem: managing running cloud systems consistently at scale.

## Labs

### [01 — Systems Hardening with Patch Manager](systems-hardening-patch-manager.md)

Applied patch policy across Linux and Windows EC2 fleets using managed and custom patch baselines, patch groups, tag-based targeting, and compliance reporting.

### [02 — Using AWS Systems Manager](using-systems-manager.md)

Used Inventory, Run Command, Parameter Store, and Session Manager to centrally inspect, configure, operate, and access an EC2 instance.

## Relationship

Patch Manager applies Systems Manager to a specific operational responsibility: maintaining patch state and verifying compliance.

The broader Systems Manager lab expands that same management model into inventory, remote execution, application configuration, and controlled instance access.

Together, the labs demonstrate:

**centralized management → operational maintenance → verified system state**
