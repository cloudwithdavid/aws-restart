# Cloud Systems Operations

## About

Cloud infrastructure does not stop at deployment. These labs demonstrate the operational layer required to manage running cloud systems consistently at scale through centralized management, repeatable configuration, secure access, maintenance, and compliance verification with AWS Systems Manager.

## Labs

### [01 — Systems Hardening with Patch Manager](systems-hardening-patch-manager.md)

Applied patch policy across Linux and Windows EC2 fleets using managed and custom patch baselines, patch groups, tag-based targeting, and compliance reporting.

### [02 — Using AWS Systems Manager](using-systems-manager.md)

Used Inventory, Run Command, Parameter Store, and Session Manager to centrally inspect, configure, operate, and access an EC2 instance.

## Relationship

Patch Manager applies Systems Manager to a specific operational responsibility: maintaining patch state and verifying compliance.

The broader Systems Manager lab expands that same management model into inventory, remote execution, application configuration, and controlled instance access.

Together, the labs demonstrate: **centralized management → operational maintenance → verified system state**

~~~
    Systems Hardening with Patch Manager  
    │  
    ├── identify/manage EC2 fleets  
    ├── patch Linux  
    ├── create Windows patch baseline  
    ├── patch groups  
    └── verify compliance  
    │  
    ▼   
    Using AWS Systems Manager  
    │  
    ├── Fleet Manager / Inventory  
    ├── Run Command  
    ├── Parameter Store  
    └── Session Manager  
    │  
    ▼  
┌────────────────────────────────────┐  
│      Cloud Systems Operations      │         
│                                    │
│   Managed EC2 fleet                │
│   ├── inventory                    │
│   ├── remote commands              │
│   ├── centralized configuration    │
│   ├── secure remote administration │
│   ├── patch management             │
│   └── compliance verification      │
└────────────────────────────────────┘
~~~
