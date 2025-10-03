# Agent Usage Patterns Documentation

This document provides comprehensive usage patterns for all specialized Claude Code agents and their commands.

## Agent Command Structure

### Basic Command Pattern
```bash
claude-code run-agent <agent-name> --command=<command-name> [options]
```

### Global Agent Operations
```bash
# Analyze entire project with all agents
claude-code analyze-project --agents=all

# Execute coordinated workflows
claude-code execute-workflow <workflow-name>

# List available agents
claude-code list-agents

# Get agent status
claude-code agent-status <agent-name>
```

## Management & Process Agents

### 1. Product Backlog Orchestrator (`sprint-story-manager`)

#### Commands
```bash
# Analyze current backlog
claude-code run-agent sprint-story-manager --command=analyze_backlog

# Track story progress
claude-code run-agent sprint-story-manager --command=track_progress --story-id=<id>

# Validate story completion
claude-code run-agent sprint-story-manager --command=validate_completion --story-id=<id>

# Generate sprint recommendations
claude-code run-agent sprint-story-manager --command=generate_sprint_recommendations

# Calculate burndown metrics
claude-code run-agent sprint-story-manager --command=calculate_burndown --sprint-id=<id>

# Prioritize backlog items
claude-code run-agent sprint-story-manager --command=prioritize_backlog

# Create user story from requirements
claude-code run-agent sprint-story-manager --command=create_user_story --requirements="<requirements>"
```

#### Usage Examples
```bash
# Start sprint planning
claude-code run-agent sprint-story-manager --command=analyze_backlog --output-format=json

# Track specific epic progress
claude-code run-agent sprint-story-manager --command=track_progress --epic-id=EPIC-123

# Generate weekly sprint report
claude-code run-agent sprint-story-manager --command=generate_sprint_report --week=current
```

### 2. Technical Debt Sentinel (`debt-paydown-manager`)

#### Commands
```bash
# Analyze technical debt
claude-code run-agent debt-paydown-manager --command=analyze_debt

# Generate debt paydown roadmap
claude-code run-agent debt-paydown-manager --command=generate_roadmap

# Emergency security scan
claude-code run-agent debt-paydown-manager --command=emergency_security_scan

# Calculate ROI for debt reduction
claude-code run-agent debt-paydown-manager --command=calculate_roi --debt-item=<item>

# Track dependency vulnerabilities
claude-code run-agent debt-paydown-manager --command=track_vulnerabilities

# Business impact assessment
claude-code run-agent debt-paydown-manager --command=assess_business_impact
```

#### Usage Examples
```bash
# Weekly debt analysis
claude-code run-agent debt-paydown-manager --command=analyze_debt --scope=weekly

# Critical vulnerability response
claude-code run-agent debt-paydown-manager --command=emergency_security_scan --severity=critical

# Generate executive debt report
claude-code run-agent debt-paydown-manager --command=generate_roadmap --audience=executive
```

## Architecture & Security Agents

### 3. Architecture Evolution Guide (`spring-boot-architect`)

#### Commands
```bash
# Analyze current architecture
claude-code run-agent spring-boot-architect --command=analyze_architecture

# Generate service layer
claude-code run-agent spring-boot-architect --command=generate_service_layer

# Validate architectural patterns
claude-code run-agent spring-boot-architect --command=validate_patterns

# Create architectural decision record
claude-code run-agent spring-boot-architect --command=create_adr --decision="<decision>"

# Plan microservices migration
claude-code run-agent spring-boot-architect --command=plan_microservices_migration

# Review Spring Boot configuration
claude-code run-agent spring-boot-architect --command=review_configuration
```

#### Usage Examples
```bash
# Full architecture assessment
claude-code run-agent spring-boot-architect --command=analyze_architecture --depth=comprehensive

# Generate service layer for specific domain
claude-code run-agent spring-boot-architect --command=generate_service_layer --domain=user-management

# Create ADR for database migration
claude-code run-agent spring-boot-architect --command=create_adr --decision="Migrate from H2 to PostgreSQL"
```

### 4. Security & Compliance Guardian (`spring-security-enforcer`)

#### Commands
```bash
# Comprehensive security scan
claude-code run-agent spring-security-enforcer --command=security_scan

# OWASP compliance check
claude-code run-agent spring-security-enforcer --command=compliance_check

# Implement Spring Security
claude-code run-agent spring-security-enforcer --command=implement_spring_security

# Vulnerability assessment
claude-code run-agent spring-security-enforcer --command=vulnerability_assessment

# Security pattern enforcement
claude-code run-agent spring-security-enforcer --command=enforce_security_patterns

# Generate security documentation
claude-code run-agent spring-security-enforcer --command=generate_security_docs
```

#### Usage Examples
```bash
# Emergency security audit
claude-code run-agent spring-security-enforcer --command=security_scan --priority=emergency

# OWASP Top 10 compliance
claude-code run-agent spring-security-enforcer --command=compliance_check --standard=owasp-top-10

# Implement JWT authentication
claude-code run-agent spring-security-enforcer --command=implement_spring_security --auth-type=jwt
```

## Quality & Operations Agents

### 5. Quality Assurance Automation (`spring-test-strategist`)

#### Commands
```bash
# Analyze test coverage
claude-code run-agent spring-test-strategist --command=analyze_test_coverage

# Setup integration tests
claude-code run-agent spring-test-strategist --command=setup_integration_tests

# Validate quality gates
claude-code run-agent spring-test-strategist --command=validate_quality_gates

# Generate test strategy
claude-code run-agent spring-test-strategist --command=generate_test_strategy

# Create performance tests
claude-code run-agent spring-test-strategist --command=create_performance_tests

# Setup test data management
claude-code run-agent spring-test-strategist --command=setup_test_data_management
```

#### Usage Examples
```bash
# Full test coverage analysis
claude-code run-agent spring-test-strategist --command=analyze_test_coverage --target=80

# Setup Spring Boot integration tests
claude-code run-agent spring-test-strategist --command=setup_integration_tests --framework=testcontainers

# Create API performance tests
claude-code run-agent spring-test-strategist --command=create_performance_tests --type=api
```

### 6. Spring Boot DevOps Orchestrator (`spring-deployment-manager`)

#### Commands
```bash
# Setup CI/CD pipeline
claude-code run-agent spring-deployment-manager --command=setup_pipeline

# Containerize application
claude-code run-agent spring-deployment-manager --command=containerize_application

# Setup monitoring
claude-code run-agent spring-deployment-manager --command=setup_monitoring

# Deploy to environment
claude-code run-agent spring-deployment-manager --command=deploy --environment=<env>

# Setup load balancing
claude-code run-agent spring-deployment-manager --command=setup_load_balancing

# Performance optimization
claude-code run-agent spring-deployment-manager --command=optimize_performance
```

#### Usage Examples
```bash
# Setup GitHub Actions pipeline
claude-code run-agent spring-deployment-manager --command=setup_pipeline --platform=github-actions

# Create Docker configuration
claude-code run-agent spring-deployment-manager --command=containerize_application --registry=docker-hub

# Setup Prometheus monitoring
claude-code run-agent spring-deployment-manager --command=setup_monitoring --tool=prometheus
```

## Development & Code Review Agents

### 7. Technical Code Reviewer (`technical-code-reviewer`)

#### Commands
```bash
# Review code quality
claude-code run-agent technical-code-reviewer --command=review_code --path=<path>

# Analyze code complexity
claude-code run-agent technical-code-reviewer --command=analyze_complexity

# Check Spring Boot patterns
claude-code run-agent technical-code-reviewer --command=check_spring_patterns

# Security scan
claude-code run-agent technical-code-reviewer --command=security_scan

# Performance analysis
claude-code run-agent technical-code-reviewer --command=analyze_performance

# Code maintainability review
claude-code run-agent technical-code-reviewer --command=review_maintainability
```

#### Usage Examples
```bash
# Review specific controller
claude-code run-agent technical-code-reviewer --command=review_code --path=src/main/java/controllers/UserController.java

# Analyze entire service layer complexity
claude-code run-agent technical-code-reviewer --command=analyze_complexity --scope=service-layer

# Security review for authentication module
claude-code run-agent technical-code-reviewer --command=security_scan --module=authentication
```

### 8. Functional Code Reviewer (`functional-code-reviewer`)

#### Commands
```bash
# Review user story implementation
claude-code run-agent functional-code-reviewer --command=review_user_story --story-id=<id>

# Validate business rules
claude-code run-agent functional-code-reviewer --command=validate_business_rules

# Review API contract
claude-code run-agent functional-code-reviewer --command=review_api_contract

# Domain model validation
claude-code run-agent functional-code-reviewer --command=validate_domain_model

# Acceptance criteria check
claude-code run-agent functional-code-reviewer --command=check_acceptance_criteria --story-id=<id>

# Business logic compliance
claude-code run-agent functional-code-reviewer --command=check_business_compliance
```

#### Usage Examples
```bash
# Review user registration story
claude-code run-agent functional-code-reviewer --command=review_user_story --story-id=USER-123

# Validate e-commerce business rules
claude-code run-agent functional-code-reviewer --command=validate_business_rules --domain=ecommerce

# Check REST API contract compliance
claude-code run-agent functional-code-reviewer --command=review_api_contract --api-version=v1
```

## Core Development Agents

### 9. Code Generation Assistant (`code-generation-assistant`)

#### Commands
```bash
# Generate CRUD feature
claude-code run-agent code-generation-assistant --command=generate_crud_feature --entity=<entity>

# Generate tests
claude-code run-agent code-generation-assistant --command=generate_tests --class=<class>

# Enhance existing code
claude-code run-agent code-generation-assistant --command=enhance_existing_code --path=<path>

# Generate Spring Boot starter
claude-code run-agent code-generation-assistant --command=generate_starter --type=<type>

# Create boilerplate
claude-code run-agent code-generation-assistant --command=create_boilerplate --template=<template>

# Generate documentation
claude-code run-agent code-generation-assistant --command=generate_documentation --scope=<scope>
```

#### Usage Examples
```bash
# Generate complete User CRUD
claude-code run-agent code-generation-assistant --command=generate_crud_feature --entity=User --include-tests=true

# Generate unit tests for service
claude-code run-agent code-generation-assistant --command=generate_tests --class=UserService --test-type=unit

# Create REST controller boilerplate
claude-code run-agent code-generation-assistant --command=create_boilerplate --template=rest-controller --entity=Product
```

### 10. Spring Boot Feature Developer (`spring-boot-feature-developer`)

#### Commands
```bash
# Implement user story
claude-code run-agent spring-boot-feature-developer --command=implement_user_story --story-id=<id>

# Enhance existing feature
claude-code run-agent spring-boot-feature-developer --command=enhance_existing_feature --feature=<feature>

# Optimize feature
claude-code run-agent spring-boot-feature-developer --command=optimize_feature --feature=<feature>

# Add feature documentation
claude-code run-agent spring-boot-feature-developer --command=document_feature --feature=<feature>

# Create feature tests
claude-code run-agent spring-boot-feature-developer --command=create_feature_tests --feature=<feature>

# Validate feature implementation
claude-code run-agent spring-boot-feature-developer --command=validate_implementation --feature=<feature>
```

#### Usage Examples
```bash
# Implement user authentication feature
claude-code run-agent spring-boot-feature-developer --command=implement_user_story --story-id=AUTH-001 --include-security=true

# Enhance search functionality
claude-code run-agent spring-boot-feature-developer --command=enhance_existing_feature --feature=search --add-filters=true

# Optimize payment processing
claude-code run-agent spring-boot-feature-developer --command=optimize_feature --feature=payment --focus=performance
```

### 11. Refactoring Specialist (`refactoring-specialist`)

#### Commands
```bash
# Analyze refactoring opportunities
claude-code run-agent refactoring-specialist --command=analyze_refactoring_opportunities

# Execute service layer extraction
claude-code run-agent refactoring-specialist --command=execute_service_layer_extraction

# Refactor dependency injection
claude-code run-agent refactoring-specialist --command=refactor_dependency_injection

# Extract common functionality
claude-code run-agent refactoring-specialist --command=extract_common_functionality

# Modernize legacy code
claude-code run-agent refactoring-specialist --command=modernize_legacy_code

# Apply design patterns
claude-code run-agent refactoring-specialist --command=apply_design_patterns --pattern=<pattern>
```

#### Usage Examples
```bash
# Full refactoring analysis
claude-code run-agent refactoring-specialist --command=analyze_refactoring_opportunities --scope=entire-project

# Extract service layer from controllers
claude-code run-agent refactoring-specialist --command=execute_service_layer_extraction --controllers=all

# Apply Strategy pattern to payment processing
claude-code run-agent refactoring-specialist --command=apply_design_patterns --pattern=strategy --domain=payment
```

### 12. API Design Assistant (`api-design-assistant`)

#### Commands
```bash
# Design API endpoint
claude-code run-agent api-design-assistant --command=design_api_endpoint --resource=<resource>

# Generate OpenAPI documentation
claude-code run-agent api-design-assistant --command=generate_openapi_documentation

# Validate API design
claude-code run-agent api-design-assistant --command=validate_api_design

# Create API versioning strategy
claude-code run-agent api-design-assistant --command=create_versioning_strategy

# Design RESTful resources
claude-code run-agent api-design-assistant --command=design_restful_resources --domain=<domain>

# Generate API client
claude-code run-agent api-design-assistant --command=generate_api_client --language=<language>
```

#### Usage Examples
```bash
# Design User management API
claude-code run-agent api-design-assistant --command=design_api_endpoint --resource=User --operations=crud

# Generate complete OpenAPI spec
claude-code run-agent api-design-assistant --command=generate_openapi_documentation --version=3.0 --format=yaml

# Validate REST API design
claude-code run-agent api-design-assistant --command=validate_api_design --standards=rest-best-practices

# Create v2 API versioning
claude-code run-agent api-design-assistant --command=create_versioning_strategy --current-version=v1 --target-version=v2
```

### 13. Database Schema Manager (`database-schema-manager`)

#### Commands
```bash
# Analyze current schema
claude-code run-agent database-schema-manager --command=analyze_current_schema

# Create migration script
claude-code run-agent database-schema-manager --command=create_migration_script --from=<source> --to=<target>

# Optimize JPA entities
claude-code run-agent database-schema-manager --command=optimize_jpa_entities

# Design database schema
claude-code run-agent database-schema-manager --command=design_schema --domain=<domain>

# Generate test data
claude-code run-agent database-schema-manager --command=generate_test_data --entities=<entities>

# Performance tuning
claude-code run-agent database-schema-manager --command=performance_tuning
```

#### Usage Examples
```bash
# Analyze H2 to PostgreSQL migration
claude-code run-agent database-schema-manager --command=analyze_current_schema --target-db=postgresql

# Create migration from H2 to MySQL
claude-code run-agent database-schema-manager --command=create_migration_script --from=h2 --to=mysql

# Optimize User entity performance
claude-code run-agent database-schema-manager --command=optimize_jpa_entities --entity=User --focus=performance
```

## Coordinated Workflows

### Sprint Planning Workflow
```bash
claude-code execute-workflow sprint_planning_workflow --sprint-duration=2weeks
```

### Critical Vulnerability Response
```bash
claude-code execute-workflow critical_vulnerability_response --severity=critical
```

### Architecture Evolution Workflow
```bash
claude-code execute-workflow architecture_evolution --target-architecture=microservices
```

### Feature Development Workflow
```bash
claude-code execute-workflow feature_development --story-id=<id> --parallel-review=true
```

### Code Review Workflow
```bash
claude-code execute-workflow code_review_workflow --scope=feature --feature-branch=<branch>
```

## Agent Configuration Commands

### Agent Registry Management
```bash
# Update agent registry
claude-code update-agent-registry

# Validate agent configuration
claude-code validate-agent-config --agent=<agent-name>

# Reset agent to defaults
claude-code reset-agent --agent=<agent-name>

# Export agent configuration
claude-code export-agent-config --agent=<agent-name> --format=yaml
```

### Agent Coordination
```bash
# Setup agent coordination
claude-code setup-agent-coordination

# Configure workflow triggers
claude-code configure-workflow-triggers --workflow=<workflow>

# Monitor agent performance
claude-code monitor-agents --metrics=performance
```

## Advanced Usage Patterns

### Parallel Agent Execution
```bash
# Run multiple agents in parallel
claude-code run-agents-parallel \
  --agent1="technical-code-reviewer --command=review_code" \
  --agent2="functional-code-reviewer --command=review_user_story" \
  --agent3="spring-security-enforcer --command=security_scan"
```

### Conditional Agent Execution
```bash
# Run agent based on conditions
claude-code run-agent-conditional \
  --condition="test_coverage < 80" \
  --agent="spring-test-strategist" \
  --command="analyze_test_coverage"
```

### Agent Pipeline
```bash
# Execute agents in sequence
claude-code execute-agent-pipeline \
  --pipeline="debt-analysis,architecture-review,security-scan" \
  --fail-fast=true
```

## Output Formats and Options

### Output Format Options
```bash
# JSON output
--output-format=json

# YAML output
--output-format=yaml

# Markdown report
--output-format=markdown

# Plain text
--output-format=text

# HTML report
--output-format=html
```

### Logging and Debugging
```bash
# Enable verbose logging
--verbose

# Debug mode
--debug

# Log to file
--log-file=agent-execution.log

# Trace execution
--trace
```

### Integration Options
```bash
# IDE integration
--ide-integration=true

# CI/CD integration
--ci-mode=true

# Webhook notifications
--webhook=<url>

# Slack notifications
--slack-channel=<channel>
```

## Best Practices

### Agent Selection Guidelines
1. Use **Management Agents** for planning and tracking
2. Use **Architecture Agents** for design decisions
3. Use **Security Agents** for compliance and vulnerability management
4. Use **Quality Agents** for testing and code quality
5. Use **Development Agents** for implementation tasks

### Workflow Optimization
1. Run agents in parallel when possible
2. Use coordinated workflows for complex tasks
3. Cache agent results for repeated operations
4. Monitor agent performance and adjust accordingly

### Error Handling
```bash
# Retry failed agents
--retry-count=3

# Fallback strategy
--fallback-agent=<agent-name>

# Continue on error
--continue-on-error=true
```