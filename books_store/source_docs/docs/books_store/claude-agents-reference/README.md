# Agent Configurations

This directory contains configuration files for Claude Code agents.

## Directory Structure

```
configs/
├── architecture-security/
├── core-development/
├── development-review/
├── governance/
├── management-process/
├── quality-operations/
└── README.md           # This file
```

## Agent Categories

### Architecture & Security
- `spring-boot-architect.md` - Architecture Evolution Guide
- `spring-security-enforcer.md` - Security & Compliance Guardian
- `infrastructure-as-code-manager.md` - Infrastructure as Code Manager

### Core Development
- `spring-boot-feature-developer.md` - Spring Boot Feature Developer
- `code-generation-assistant.md` - Code Generation Assistant
- `api-design-assistant.md` - API Design Assistant
- `database-schema-manager.md` - Database Schema Manager
- `refactoring-specialist.md` - Refactoring Specialist
- `feature-flag-manager.md` - Feature Flag Manager

### Development & Review
- `technical-code-reviewer.md` - Technical Code Reviewer
- `functional-code-reviewer.md` - Functional Code Reviewer
- `code-reviewer.md` - General Code Reviewer

### Quality & Operations
- `test-strategist.md` - Quality Assurance Automation
- `spring-deployment-manager.md` - Spring Boot DevOps Orchestrator
- `performance-testing-specialist.md` - Performance Testing Specialist
- `monitoring-observability-engineer.md` - Monitoring & Observability Engineer
- `environment-manager.md` - Environment Manager
- `incident-response-manager.md` - Incident Response Manager
- `quality-metrics-analyst.md` - Quality Metrics Analyst
- `user-experience-analyst.md` - User Experience Analyst

### Management & Process
- `sprint-story-manager.md` - Product Backlog Orchestrator
- `debt-paydown-manager.md` - Technical Debt Sentinel
- `business-analyst.md` - Business Analyst
- `release-manager.md` - Release Manager

### Governance
- `documentation-specialist.md` - Documentation Specialist
- `compliance-officer.md` - Compliance Officer

## Configuration Format

Each agent configuration file contains:

1. **Agent Identity**: Name, role, and responsibilities
2. **Core Capabilities**: Primary functions and expertise areas
3. **Command Interface**: Available commands and their descriptions
4. **Collaboration Patterns**: How the agent works with other agents
5. **Templates & Standards**: References to templates in `.claude/templates/`
6. **Quality Standards**: Standards and criteria the agent enforces

## Template References

Agents reference templates from the centralized `.claude/templates/` directory:

```markdown
## Templates and Standards

**Spring Boot Templates**: Uses `.claude/templates/spring-boot/`
- Controller template for REST endpoints
- Service template for business logic
- Repository template for data access
- Entity template for JPA entities
- DTO template for data transfer
- Test template for comprehensive testing
```

## Agent Coordination

Agents are designed to work together through defined workflows:

- **Sequential**: Agents work in a specific order
- **Parallel**: Agents work simultaneously
- **Conditional**: Agent activation based on conditions

See `.claude/agents/agent-coordinator.yaml` for workflow definitions.

## Usage

These configuration files are used by Claude Code to:

1. Understand agent capabilities and limitations
2. Route tasks to appropriate specialists
3. Coordinate multi-agent workflows
4. Maintain consistency across implementations
5. Reference appropriate templates and standards

## Maintenance

When updating agent configurations:

1. Keep descriptions current with capabilities
2. Update template references when templates change
3. Maintain consistency in command naming
4. Document new collaboration patterns
5. Update workflow dependencies as needed