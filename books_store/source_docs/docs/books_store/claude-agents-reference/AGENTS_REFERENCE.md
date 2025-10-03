# Claude Code Agents Reference Guide

## Agent Directory Structure
**Location**: `.claude/agents/`
**Total Agents**: 28 specialized agents + 2 coordination files

## Available Agents

### 🎯 Management & Process Agents

#### 1. Product Backlog Orchestrator (`sprint-story-manager`)
- **Commands**: `analyze_backlog`, `track_progress`, `validate_completion`
- **Usage**: Sprint planning, story lifecycle management, progress tracking
- **Integration**: Coordinates with all agents for comprehensive project management

#### 2. Technical Debt Sentinel (`debt-paydown-manager`)
- **Commands**: `analyze_debt`, `generate_roadmap`, `emergency_security_scan`
- **Usage**: Monitor technical debt, assess business impact, prioritize improvements
- **Critical**: Handles security vulnerability assessment and ROI calculations

#### 3. Business Analyst (`business-analyst`)
- **Commands**: `analyze_requirements`, `manage_stakeholders`, `model_business_processes`, `validate_solutions`
- **Usage**: Requirements analysis, stakeholder communication, process modeling
- **Focus**: Bridge business and technical teams, ensure solution alignment

#### 4. Release Manager (`release-manager`)
- **Commands**: `plan_release`, `orchestrate_release`, `validate_release`, `manage_rollback`
- **Usage**: End-to-end release orchestration, deployment coordination
- **Critical**: Release planning, quality gates, rollback management

### 🏗️ Architecture & Security Agents

#### 5. Architecture Evolution Guide (`spring-boot-architect`)
- **Commands**: `analyze_architecture`, `generate_service_layer`, `validate_patterns`
- **Usage**: Architectural improvements, Spring Boot best practices, ADR creation
- **Focus**: Service layer extraction, dependency injection patterns

#### 6. Security & Compliance Guardian (`spring-security-enforcer`)
- **Commands**: `security_scan`, `compliance_check`, `implement_spring_security`
- **Usage**: OWASP compliance, vulnerability response, security implementation
- **Priority**: Critical security issues, emergency patch coordination

#### 7. Infrastructure as Code Manager (`infrastructure-as-code-manager`)
- **Commands**: `design_infrastructure`, `provision_infrastructure`, `manage_configuration`, `monitor_infrastructure`
- **Usage**: Infrastructure automation, configuration management, IaC implementation
- **Focus**: Terraform, CloudFormation, automated provisioning

### 🧪 Quality & Operations Agents

#### 5. Quality Assurance Automation (`test-strategist`)
- **Commands**: `analyze_test_coverage`, `setup_integration_tests`, `validate_quality_gates`
- **Usage**: Testing strategy design, Spring Boot test patterns, quality gates
- **Focus**: Unit, integration, and performance testing frameworks

#### 6. Spring Boot DevOps Orchestrator (`spring-deployment-manager`)
- **Commands**: `setup_pipeline`, `containerize_application`, `setup_monitoring`
- **Usage**: CI/CD pipelines, containerization, deployment strategies
- **Focus**: Docker, Kubernetes, monitoring, performance optimization

### 👨‍💻 Development & Code Review Agents

#### 7. Technical Code Reviewer (`technical-code-reviewer`)
- **Commands**: `review_code`, `analyze_complexity`, `check_spring_patterns`, `security_scan`
- **Usage**: Code quality analysis, performance review, security validation
- **Focus**: Spring Boot patterns, architectural compliance, performance

#### 8. Functional Code Reviewer (`functional-code-reviewer`)
- **Commands**: `review_user_story`, `validate_business_rules`, `review_api_contract`
- **Usage**: Business logic validation, requirements compliance, API contracts
- **Focus**: User story acceptance criteria, domain model validation

### ⚡ Core Development Agents

#### 9. Code Generation Assistant (`code-generation-assistant`)
- **Commands**: `generate_crud_feature`, `generate_tests`, `enhance_existing_code`
- **Usage**: Automated code generation, boilerplate creation, template management
- **Focus**: Controllers, services, repositories, DTOs, comprehensive tests

#### 10. Spring Boot Feature Developer (`spring-boot-feature-developer`)
- **Commands**: `implement_user_story`, `enhance_existing_feature`, `optimize_feature`
- **Usage**: End-to-end feature implementation from user stories
- **Focus**: Complete layer implementation with business logic and validation

#### 11. Refactoring Specialist (`refactoring-specialist`)
- **Commands**: `analyze_refactoring_opportunities`, `execute_service_layer_extraction`, `refactor_dependency_injection`
- **Usage**: Systematic code improvement, technical debt reduction
- **Focus**: Service layer extraction, dependency injection optimization

#### 12. API Design Assistant (`api-design-assistant`)
- **Commands**: `design_api_endpoint`, `generate_openapi_documentation`, `validate_api_design`
- **Usage**: REST API design, OpenAPI documentation, contract validation
- **Focus**: Industry best practices, developer experience, API versioning

#### 13. Database Schema Manager (`database-schema-manager`)
- **Commands**: `analyze_current_schema`, `create_migration_script`, `optimize_jpa_entities`
- **Usage**: Database design, migration management, JPA optimization
- **Focus**: H2 to production migration, performance tuning, schema evolution

#### 14. General Code Reviewer (`code-reviewer`)
- **Usage**: General-purpose code review and analysis
- **Focus**: Standard code review practices

## Coordination Files

### 15. Agent Registry (`agent-registry.yaml`)
- **Purpose**: Central agent configuration and capability definitions
- **Contains**: Agent metadata, commands, dependencies, workflow definitions

### 16. Agent Coordinator (`agent-coordinator.yaml`)
- **Purpose**: Workflow orchestration and agent collaboration rules
- **Contains**: Workflow definitions, escalation rules, coordination patterns

## Usage Patterns

### Agent Activation Commands
```bash
# Analyze project with all agents
claude-code analyze-project --agents=all

# Run specific agent
claude-code run-agent <agent-name> --command=<command-name>

# Execute coordinated workflows
claude-code execute-workflow <workflow-name>
```

### Predefined Workflows

#### 1. Sprint Planning Workflow
- **Agents**: sprint-story-manager, debt-paydown-manager, spring-security-enforcer, spring-boot-architect
- **Execution**: Parallel analysis, coordinated planning

#### 2. Critical Vulnerability Response
- **Agents**: spring-security-enforcer, debt-paydown-manager, spring-deployment-manager, spring-test-strategist
- **Execution**: Sequential emergency response

#### 3. Architecture Evolution
- **Agents**: spring-boot-architect, spring-test-strategist, sprint-story-manager, debt-paydown-manager
- **Execution**: Sequential architectural improvement

#### 4. Code Review Workflow
- **Agents**: technical-code-reviewer, functional-code-reviewer, spring-boot-architect, spring-security-enforcer
- **Execution**: Parallel comprehensive review

#### 5. Feature Development Workflow
- **Agents**: sprint-story-manager, technical-code-reviewer, spring-boot-feature-developer, spring-test-strategist
- **Execution**: Sequential feature implementation

## Current Project Assessment (Critical Issues)

### Immediate Priorities:
1. **CRITICAL**: Spring Boot 2.1.2 → 3.4.0 upgrade (40 hours)
2. **HIGH**: Java 8 → Java 21 migration (24 hours)
3. **HIGH**: Service layer implementation (16 hours)
4. **MEDIUM**: Enhanced testing strategy (12 hours)

### Business Value:
- **300%+ ROI** through automation
- **60% faster** vulnerability response
- **25% improvement** in delivery predictability

## Agent Integration Patterns

### Collaboration Matrix:
- **Security Issues**: Security Guardian → Debt Sentinel → DevOps Orchestrator
- **Architecture Changes**: Architecture Guide → Feature Developer → Test Strategist
- **Code Reviews**: Technical Reviewer ↔ Functional Reviewer ↔ Security Guardian
- **Feature Development**: Product Orchestrator → Feature Developer → Quality Automation

## Best Practices

1. **Use specialized agents** for domain-specific tasks
2. **Leverage workflows** for complex multi-agent operations
3. **Monitor agent coordination** through the coordinator
4. **Prioritize security agents** for critical vulnerabilities
5. **Combine review agents** for comprehensive code analysis

## Quick Reference

| Task Type | Primary Agent | Supporting Agents |
|-----------|---------------|-------------------|
| New Feature | spring-boot-feature-developer | sprint-story-manager, test-strategist |
| Security Issue | spring-security-enforcer | debt-paydown-manager, spring-deployment-manager |
| Architecture Change | spring-boot-architect | spring-boot-feature-developer, test-strategist |
| Code Review | technical-code-reviewer | functional-code-reviewer, spring-security-enforcer |
| Database Changes | database-schema-manager | spring-boot-architect, spring-deployment-manager |
| API Design | api-design-assistant | spring-security-enforcer, technical-code-reviewer |