# Template Specifications

**Document Version:** 1.0
**Last Updated:** 2025-10-01
**Status:** Draft
**Owner:** Development Team

---

## Executive Summary

This document provides detailed specifications for all Claude Code templates supporting the SDLC process. Templates are organized into five categories: Agile, Code, Testing, Documentation, and Architecture. Each template specification includes structure, required fields, validation rules, and usage guidelines.

**Template Location:** `.claude/templates/`

**Total Templates:** 25 templates across 5 categories

---

## Table of Contents

1. [Agile Templates](#1-agile-templates)
2. [Code Templates](#2-code-templates)
3. [Testing Templates](#3-testing-templates)
4. [Documentation Templates](#4-documentation-templates)
5. [Architecture Templates](#5-architecture-templates)
6. [Template Usage Guidelines](#6-template-usage-guidelines)
7. [Template Maintenance](#7-template-maintenance)

---

## 1. Agile Templates

### 1.1 User Story Template

**File:** `.claude/templates/agile/user-story.md`

**Purpose:** Standardize user story format for consistency and completeness

**Structure:**
```markdown
---
type: user-story
id: US-{{STORY_ID}}
sprint: {{SPRINT_NUMBER}}
status: {{STATUS}}
priority: {{PRIORITY}}
story_points: {{POINTS}}
epic_id: {{EPIC_ID}}
created: {{DATE}}
assignee: {{ASSIGNEE}}
---

# User Story: {{TITLE}}

## As a...
{{USER_ROLE}}

## I want to...
{{DESIRED_FEATURE}}

## So that...
{{BUSINESS_VALUE}}

## Acceptance Criteria

- [ ] {{CRITERION_1}}
- [ ] {{CRITERION_2}}
- [ ] {{CRITERION_3}}

## Technical Notes

{{TECHNICAL_IMPLEMENTATION_DETAILS}}

## Dependencies

- {{DEPENDENCY_1}}
- {{DEPENDENCY_2}}

## Definition of Done

- [ ] Code implemented and peer-reviewed
- [ ] Unit tests written (>80% coverage)
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Acceptance criteria validated
- [ ] Deployed to staging environment

## Test Scenarios

### Scenario 1: {{HAPPY_PATH_NAME}}
**Given:** {{PRECONDITION}}
**When:** {{ACTION}}
**Then:** {{EXPECTED_RESULT}}

### Scenario 2: {{ERROR_CASE_NAME}}
**Given:** {{PRECONDITION}}
**When:** {{ACTION}}
**Then:** {{EXPECTED_RESULT}}

## UI/UX Mockups

{{LINK_OR_EMBEDDED_IMAGE}}

## Estimation Breakdown

| Task | Estimate (hours) |
|------|------------------|
| {{TASK_1}} | {{HOURS_1}} |
| {{TASK_2}} | {{HOURS_2}} |
| **Total** | **{{TOTAL_HOURS}}** |
```

**Required Fields:**
- `id`: Unique story identifier (US-XXX)
- `sprint`: Sprint number or "Backlog"
- `status`: Draft/Ready/In Progress/Review/Done
- `priority`: P0 (Critical) / P1 (High) / P2 (Medium) / P3 (Low)
- `story_points`: Fibonacci sequence (1, 2, 3, 5, 8, 13)
- User role, feature description, business value
- At least 3 acceptance criteria

**Validation Rules:**
- Story points must be Fibonacci numbers
- Status must follow workflow: Draft → Ready → In Progress → Review → Done
- Acceptance criteria must be testable and measurable
- Definition of Done checklist must have minimum 6 items

**Agent Integration:**
- Created/managed by: `sprint-story-manager`
- Reviewed by: `business-analyst`, `product-owner`
- Implemented by: `feature-developer`

---

### 1.2 Epic Template

**File:** `.claude/templates/agile/epic.md`

**Purpose:** Define large initiatives spanning multiple sprints

**Structure:**
```markdown
---
type: epic
id: EPIC-{{EPIC_ID}}
status: {{STATUS}}
priority: {{PRIORITY}}
business_value: {{VALUE_SCORE}}
target_quarter: {{QUARTER}}
owner: {{OWNER}}
---

# Epic: {{TITLE}}

## Business Goal

{{HIGH_LEVEL_OBJECTIVE}}

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| {{METRIC_1}} | {{TARGET_1}} | {{MEASUREMENT_METHOD_1}} |
| {{METRIC_2}} | {{TARGET_2}} | {{MEASUREMENT_METHOD_2}} |

## User Stories

- [ ] US-XXX: {{STORY_TITLE_1}}
- [ ] US-YYY: {{STORY_TITLE_2}}
- [ ] US-ZZZ: {{STORY_TITLE_3}}

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| {{MILESTONE_1}} | {{DATE_1}} | {{STATUS_1}} |
| {{MILESTONE_2}} | {{DATE_2}} | {{STATUS_2}} |

## Dependencies

{{EXTERNAL_DEPENDENCIES}}

## Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| {{RISK_1}} | {{IMPACT_1}} | {{PROB_1}} | {{MITIGATION_1}} |

## ROI Analysis

**Investment:** {{COST}}
**Expected Return:** {{BENEFIT}}
**Payback Period:** {{MONTHS}}
```

**Agent Integration:**
- Created by: `product-owner`
- Decomposed by: `sprint-story-manager`
- Reviewed by: `business-analyst`

---

### 1.3 Bug Report Template

**File:** `.claude/templates/agile/bug-report.md`

**Purpose:** Standardize bug reporting with reproducible steps

**Structure:**
```markdown
---
type: bug
id: BUG-{{BUG_ID}}
severity: {{SEVERITY}}
priority: {{PRIORITY}}
status: {{STATUS}}
reported_date: {{DATE}}
reporter: {{REPORTER}}
assignee: {{ASSIGNEE}}
affected_version: {{VERSION}}
---

# Bug: {{TITLE}}

## Severity

{{CRITICAL|HIGH|MEDIUM|LOW}}

## Environment

- **Application Version:** {{VERSION}}
- **Environment:** {{PROD|STAGING|DEV}}
- **OS/Browser:** {{DETAILS}}
- **Database:** {{DB_VERSION}}

## Description

{{CLEAR_DESCRIPTION}}

## Steps to Reproduce

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

## Expected Behavior

{{WHAT_SHOULD_HAPPEN}}

## Actual Behavior

{{WHAT_ACTUALLY_HAPPENS}}

## Screenshots/Logs

{{ATTACH_EVIDENCE}}

## Impact

- **Users Affected:** {{NUMBER_OR_PERCENTAGE}}
- **Business Impact:** {{DESCRIPTION}}
- **Workaround Available:** {{YES|NO}}

## Root Cause Analysis

{{TO_BE_FILLED_DURING_INVESTIGATION}}

## Fix Verification

- [ ] Fix implemented
- [ ] Unit tests added
- [ ] Regression tests passing
- [ ] Verified in staging
- [ ] Production fix deployed
```

**Severity Definitions:**
- **Critical (P0):** Production down, data loss, security breach
- **High (P1):** Major feature broken, significant user impact
- **Medium (P2):** Minor feature broken, workaround exists
- **Low (P3):** Cosmetic issue, minimal impact

**Agent Integration:**
- Triaged by: `qa-engineer`
- Fixed by: `feature-developer`, `refactoring-specialist`
- Validated by: `test-strategist`

---

### 1.4 Sprint Retrospective Template

**File:** `.claude/templates/agile/retrospective.md`

**Purpose:** Capture sprint learnings and action items

**Structure:**
```markdown
---
type: retrospective
sprint: {{SPRINT_NUMBER}}
date: {{DATE}}
participants: {{TEAM_MEMBERS}}
facilitator: {{FACILITATOR}}
---

# Sprint {{SPRINT_NUMBER}} Retrospective

## Sprint Metrics

| Metric | Target | Actual | Variance |
|--------|--------|--------|----------|
| Story Points Committed | {{TARGET}} | {{ACTUAL}} | {{VARIANCE}} |
| Story Points Completed | {{TARGET}} | {{ACTUAL}} | {{VARIANCE}} |
| Velocity | {{TARGET}} | {{ACTUAL}} | {{VARIANCE}} |
| Bug Escape Rate | {{TARGET}} | {{ACTUAL}} | {{VARIANCE}} |

## What Went Well 🟢

1. {{POSITIVE_1}}
2. {{POSITIVE_2}}
3. {{POSITIVE_3}}

## What Could Improve 🟡

1. {{IMPROVEMENT_1}}
2. {{IMPROVEMENT_2}}
3. {{IMPROVEMENT_3}}

## Action Items 🔴

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| {{ACTION_1}} | {{OWNER_1}} | {{DATE_1}} | {{STATUS_1}} |
| {{ACTION_2}} | {{OWNER_2}} | {{DATE_2}} | {{STATUS_2}} |

## Team Morale

{{TEAM_SENTIMENT_AND_FEEDBACK}}

## Blocked Items

1. {{BLOCKER_1}} - Resolution: {{RESOLUTION_1}}
2. {{BLOCKER_2}} - Resolution: {{RESOLUTION_2}}

## Process Improvements

{{SUGGESTED_PROCESS_CHANGES}}
```

**Agent Integration:**
- Facilitated by: `scrum-master`
- Data collected by: `sprint-story-manager`
- Actions tracked by: `debt-paydown-manager`

---

### 1.5 Spike Template

**File:** `.claude/templates/agile/spike.md`

**Purpose:** Document research and technical investigation

**Structure:**
```markdown
---
type: spike
id: SPIKE-{{SPIKE_ID}}
sprint: {{SPRINT_NUMBER}}
time_box: {{HOURS}}
researcher: {{ASSIGNEE}}
status: {{STATUS}}
---

# Spike: {{TITLE}}

## Research Question

{{WHAT_NEEDS_TO_BE_ANSWERED}}

## Context

{{WHY_THIS_RESEARCH_IS_NEEDED}}

## Approach

1. {{INVESTIGATION_STEP_1}}
2. {{INVESTIGATION_STEP_2}}
3. {{INVESTIGATION_STEP_3}}

## Findings

{{RESEARCH_RESULTS}}

## Recommendation

{{RECOMMENDED_APPROACH_AND_JUSTIFICATION}}

## Alternatives Considered

| Option | Pros | Cons | Estimated Effort |
|--------|------|------|------------------|
| {{OPTION_1}} | {{PROS_1}} | {{CONS_1}} | {{EFFORT_1}} |
| {{OPTION_2}} | {{PROS_2}} | {{CONS_2}} | {{EFFORT_2}} |

## Next Steps

- [ ] {{ACTION_1}}
- [ ] {{ACTION_2}}

## References

- {{LINK_1}}
- {{LINK_2}}
```

**Agent Integration:**
- Conducted by: `technical-architect`, `application-architect`
- Reviewed by: `scrum-master`, `product-owner`

---

## 2. Code Templates

### 2.1 REST Controller Template

**File:** `.claude/templates/code/rest-controller.java`

**Purpose:** Standardize REST API controller structure

**Structure:**
```java
package {{PACKAGE_NAME}}.controller;

import {{PACKAGE_NAME}}.dto.{{ENTITY}}CreateDto;
import {{PACKAGE_NAME}}.dto.{{ENTITY}}ResponseDto;
import {{PACKAGE_NAME}}.dto.{{ENTITY}}UpdateDto;
import {{PACKAGE_NAME}}.service.{{ENTITY}}Service;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * REST Controller for {{ENTITY}} operations.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@RestController
@RequestMapping("/api/v1/{{RESOURCE_PATH}}")
@RequiredArgsConstructor
@Tag(name = "{{ENTITY}} Management", description = "APIs for {{ENTITY}} CRUD operations")
public class {{ENTITY}}Controller {

    private final {{ENTITY}}Service {{ENTITY_LOWER}}Service;

    /**
     * Create a new {{ENTITY}}.
     *
     * @param createDto the {{ENTITY}} creation data
     * @return the created {{ENTITY}}
     */
    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(summary = "Create {{ENTITY}}", description = "Creates a new {{ENTITY}} with the provided data")
    public ResponseEntity<{{ENTITY}}ResponseDto> create(@Valid @RequestBody {{ENTITY}}CreateDto createDto) {
        {{ENTITY}}ResponseDto response = {{ENTITY_LOWER}}Service.create(createDto);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    /**
     * Get {{ENTITY}} by ID.
     *
     * @param id the {{ENTITY}} ID
     * @return the {{ENTITY}} if found
     */
    @GetMapping("/{id}")
    @Operation(summary = "Get {{ENTITY}} by ID", description = "Retrieves a {{ENTITY}} by its unique identifier")
    public ResponseEntity<{{ENTITY}}ResponseDto> getById(@PathVariable Long id) {
        return {{ENTITY_LOWER}}Service.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    /**
     * Get all {{ENTITY}}s with pagination.
     *
     * @param pageable pagination parameters
     * @return paginated list of {{ENTITY}}s
     */
    @GetMapping
    @Operation(summary = "Get all {{ENTITY}}s", description = "Retrieves a paginated list of all {{ENTITY}}s")
    public ResponseEntity<Page<{{ENTITY}}ResponseDto>> getAll(Pageable pageable) {
        Page<{{ENTITY}}ResponseDto> page = {{ENTITY_LOWER}}Service.findAll(pageable);
        return ResponseEntity.ok(page);
    }

    /**
     * Update {{ENTITY}}.
     *
     * @param id the {{ENTITY}} ID
     * @param updateDto the update data
     * @return the updated {{ENTITY}}
     */
    @PutMapping("/{id}")
    @Operation(summary = "Update {{ENTITY}}", description = "Updates an existing {{ENTITY}} with the provided data")
    public ResponseEntity<{{ENTITY}}ResponseDto> update(
            @PathVariable Long id,
            @Valid @RequestBody {{ENTITY}}UpdateDto updateDto) {
        {{ENTITY}}ResponseDto response = {{ENTITY_LOWER}}Service.update(id, updateDto);
        return ResponseEntity.ok(response);
    }

    /**
     * Delete {{ENTITY}}.
     *
     * @param id the {{ENTITY}} ID
     * @return no content
     */
    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    @Operation(summary = "Delete {{ENTITY}}", description = "Deletes a {{ENTITY}} by its ID")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        {{ENTITY_LOWER}}Service.delete(id);
        return ResponseEntity.noContent().build();
    }
}
```

**Variable Substitutions:**
- `{{PACKAGE_NAME}}`: Base package (e.g., com.example.app)
- `{{ENTITY}}`: Entity name (e.g., Product, User)
- `{{ENTITY_LOWER}}`: Lowercase entity (e.g., product, user)
- `{{RESOURCE_PATH}}`: API path (e.g., products, users)
- `{{AUTHOR}}`: Developer name
- `{{DATE}}`: Creation date

**Agent Integration:**
- Generated by: `feature-developer`, `code-generation-assistant`
- Reviewed by: `code-reviewer`, `api-design-assistant`

---

### 2.2 Service Layer Template

**File:** `.claude/templates/code/service.java`

**Purpose:** Business logic service implementation

**Structure:**
```java
package {{PACKAGE_NAME}}.service;

import {{PACKAGE_NAME}}.dto.{{ENTITY}}CreateDto;
import {{PACKAGE_NAME}}.dto.{{ENTITY}}ResponseDto;
import {{PACKAGE_NAME}}.dto.{{ENTITY}}UpdateDto;
import {{PACKAGE_NAME}}.entity.{{ENTITY}};
import {{PACKAGE_NAME}}.exception.ResourceNotFoundException;
import {{PACKAGE_NAME}}.mapper.{{ENTITY}}Mapper;
import {{PACKAGE_NAME}}.repository.{{ENTITY}}Repository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

/**
 * Service layer for {{ENTITY}} business logic.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@Service
@RequiredArgsConstructor
@Transactional
@Slf4j
public class {{ENTITY}}Service {

    private final {{ENTITY}}Repository {{ENTITY_LOWER}}Repository;
    private final {{ENTITY}}Mapper {{ENTITY_LOWER}}Mapper;

    /**
     * Create a new {{ENTITY}}.
     *
     * @param createDto the creation data
     * @return the created {{ENTITY}}
     */
    public {{ENTITY}}ResponseDto create({{ENTITY}}CreateDto createDto) {
        log.info("Creating new {{ENTITY}}: {}", createDto);

        {{ENTITY}} entity = {{ENTITY_LOWER}}Mapper.toEntity(createDto);
        validate{{ENTITY}}(entity);

        {{ENTITY}} saved = {{ENTITY_LOWER}}Repository.save(entity);
        log.info("Created {{ENTITY}} with ID: {}", saved.getId());

        return {{ENTITY_LOWER}}Mapper.toDto(saved);
    }

    /**
     * Find {{ENTITY}} by ID.
     *
     * @param id the {{ENTITY}} ID
     * @return the {{ENTITY}} if found
     */
    @Transactional(readOnly = true)
    public Optional<{{ENTITY}}ResponseDto> findById(Long id) {
        log.debug("Finding {{ENTITY}} by ID: {}", id);
        return {{ENTITY_LOWER}}Repository.findById(id)
            .map({{ENTITY_LOWER}}Mapper::toDto);
    }

    /**
     * Find all {{ENTITY}}s with pagination.
     *
     * @param pageable pagination parameters
     * @return paginated {{ENTITY}}s
     */
    @Transactional(readOnly = true)
    public Page<{{ENTITY}}ResponseDto> findAll(Pageable pageable) {
        log.debug("Finding all {{ENTITY}}s with pagination: {}", pageable);
        return {{ENTITY_LOWER}}Repository.findAll(pageable)
            .map({{ENTITY_LOWER}}Mapper::toDto);
    }

    /**
     * Update existing {{ENTITY}}.
     *
     * @param id the {{ENTITY}} ID
     * @param updateDto the update data
     * @return the updated {{ENTITY}}
     */
    public {{ENTITY}}ResponseDto update(Long id, {{ENTITY}}UpdateDto updateDto) {
        log.info("Updating {{ENTITY}} ID {}: {}", id, updateDto);

        {{ENTITY}} existing = {{ENTITY_LOWER}}Repository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("{{ENTITY}} not found with ID: " + id));

        {{ENTITY_LOWER}}Mapper.updateEntityFromDto(updateDto, existing);
        validate{{ENTITY}}(existing);

        {{ENTITY}} updated = {{ENTITY_LOWER}}Repository.save(existing);
        log.info("Updated {{ENTITY}} with ID: {}", updated.getId());

        return {{ENTITY_LOWER}}Mapper.toDto(updated);
    }

    /**
     * Delete {{ENTITY}}.
     *
     * @param id the {{ENTITY}} ID
     */
    public void delete(Long id) {
        log.info("Deleting {{ENTITY}} with ID: {}", id);

        if (!{{ENTITY_LOWER}}Repository.existsById(id)) {
            throw new ResourceNotFoundException("{{ENTITY}} not found with ID: " + id);
        }

        {{ENTITY_LOWER}}Repository.deleteById(id);
        log.info("Deleted {{ENTITY}} with ID: {}", id);
    }

    /**
     * Validate {{ENTITY}} business rules.
     *
     * @param entity the entity to validate
     */
    private void validate{{ENTITY}}({{ENTITY}} entity) {
        // Add custom validation logic here
        log.debug("Validating {{ENTITY}}: {}", entity);
    }
}
```

**Agent Integration:**
- Generated by: `feature-developer`, `backend-developer`
- Reviewed by: `code-reviewer`, `application-architect`

---

### 2.3 Repository Template

**File:** `.claude/templates/code/repository.java`

**Purpose:** Data access layer with Spring Data JPA

**Structure:**
```java
package {{PACKAGE_NAME}}.repository;

import {{PACKAGE_NAME}}.entity.{{ENTITY}};
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Repository interface for {{ENTITY}} entity.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@Repository
public interface {{ENTITY}}Repository extends JpaRepository<{{ENTITY}}, Long>, JpaSpecificationExecutor<{{ENTITY}}> {

    /**
     * Find {{ENTITY}} by {{FIELD}}.
     *
     * @param {{FIELD_LOWER}} the {{FIELD}} value
     * @return the {{ENTITY}} if found
     */
    Optional<{{ENTITY}}> findBy{{FIELD}}(String {{FIELD_LOWER}});

    /**
     * Find all {{ENTITY}}s by {{CRITERIA}}.
     *
     * @param {{CRITERIA_LOWER}} the search criteria
     * @return list of matching {{ENTITY}}s
     */
    List<{{ENTITY}}> findBy{{CRITERIA}}ContainingIgnoreCase(String {{CRITERIA_LOWER}});

    /**
     * Check if {{ENTITY}} exists by {{FIELD}}.
     *
     * @param {{FIELD_LOWER}} the {{FIELD}} value
     * @return true if exists
     */
    boolean existsBy{{FIELD}}(String {{FIELD_LOWER}});

    /**
     * Custom query example.
     *
     * @param param the query parameter
     * @return list of results
     */
    @Query("SELECT e FROM {{ENTITY}} e WHERE e.{{FIELD}} = :param")
    List<{{ENTITY}}> findByCustomQuery(@Param("param") String param);
}
```

**Agent Integration:**
- Generated by: `feature-developer`, `database-schema-manager`
- Reviewed by: `code-reviewer`

---

### 2.4 Entity/Model Template

**File:** `.claude/templates/code/entity.java`

**Purpose:** JPA entity with validation

**Structure:**
```java
package {{PACKAGE_NAME}}.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;

/**
 * Entity representing {{ENTITY}}.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@Entity
@Table(name = "{{TABLE_NAME}}",
       indexes = {
           @Index(name = "idx_{{ENTITY_LOWER}}_{{FIELD}}", columnList = "{{FIELD_COLUMN}}")
       })
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class {{ENTITY}} {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank(message = "{{FIELD}} is required")
    @Size(max = 100, message = "{{FIELD}} must not exceed 100 characters")
    @Column(name = "{{FIELD_COLUMN}}", nullable = false, length = 100)
    private String {{FIELD_LOWER}};

    @NotNull(message = "{{NUMERIC_FIELD}} is required")
    @Min(value = 0, message = "{{NUMERIC_FIELD}} must be non-negative")
    @Column(name = "{{NUMERIC_FIELD_COLUMN}}", nullable = false)
    private Integer {{NUMERIC_FIELD_LOWER}};

    @Size(max = 500, message = "Description must not exceed 500 characters")
    @Column(name = "description", length = 500)
    private String description;

    @Column(name = "is_active", nullable = false)
    private Boolean isActive = true;

    @CreationTimestamp
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;

    @Version
    @Column(name = "version", nullable = false)
    private Long version;

    // Relationships
    // @ManyToOne
    // @JoinColumn(name = "{{RELATED_ENTITY_LOWER}}_id", foreignKey = @ForeignKey(name = "fk_{{ENTITY_LOWER}}_{{RELATED_ENTITY_LOWER}}"))
    // private {{RELATED_ENTITY}} {{RELATED_ENTITY_LOWER}};

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof {{ENTITY}})) return false;
        {{ENTITY}} that = ({{ENTITY}}) o;
        return id != null && id.equals(that.getId());
    }

    @Override
    public int hashCode() {
        return getClass().hashCode();
    }
}
```

**Agent Integration:**
- Generated by: `feature-developer`, `database-schema-manager`
- Reviewed by: `code-reviewer`, `application-architect`

---

### 2.5 DTO Templates

**File:** `.claude/templates/code/dto-request.java`

**Purpose:** Request DTOs for API input

**Structure:**
```java
package {{PACKAGE_NAME}}.dto;

import jakarta.validation.constraints.*;
import lombok.*;

/**
 * DTO for {{ENTITY}} creation request.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class {{ENTITY}}CreateDto {

    @NotBlank(message = "{{FIELD}} is required")
    @Size(max = 100, message = "{{FIELD}} must not exceed 100 characters")
    private String {{FIELD_LOWER}};

    @NotNull(message = "{{NUMERIC_FIELD}} is required")
    @Min(value = 0, message = "{{NUMERIC_FIELD}} must be non-negative")
    private Integer {{NUMERIC_FIELD_LOWER}};

    @Size(max = 500, message = "Description must not exceed 500 characters")
    private String description;
}
```

**File:** `.claude/templates/code/dto-response.java`

**Purpose:** Response DTOs for API output

**Structure:**
```java
package {{PACKAGE_NAME}}.dto;

import lombok.*;

import java.time.LocalDateTime;

/**
 * DTO for {{ENTITY}} response.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class {{ENTITY}}ResponseDto {

    private Long id;
    private String {{FIELD_LOWER}};
    private Integer {{NUMERIC_FIELD_LOWER}};
    private String description;
    private Boolean isActive;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
```

**Agent Integration:**
- Generated by: `feature-developer`, `api-design-assistant`
- Reviewed by: `code-reviewer`

---

## 3. Testing Templates

### 3.1 Unit Test Template

**File:** `.claude/templates/testing/unit-test.java`

**Purpose:** Standardize unit test structure with JUnit 5

**Structure:**
```java
package {{PACKAGE_NAME}}.service;

import {{PACKAGE_NAME}}.dto.{{ENTITY}}CreateDto;
import {{PACKAGE_NAME}}.dto.{{ENTITY}}ResponseDto;
import {{PACKAGE_NAME}}.entity.{{ENTITY}};
import {{PACKAGE_NAME}}.exception.ResourceNotFoundException;
import {{PACKAGE_NAME}}.mapper.{{ENTITY}}Mapper;
import {{PACKAGE_NAME}}.repository.{{ENTITY}}Repository;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.assertj.core.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

/**
 * Unit tests for {{ENTITY}}Service.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@ExtendWith(MockitoExtension.class)
@DisplayName("{{ENTITY}}Service Tests")
class {{ENTITY}}ServiceTest {

    @Mock
    private {{ENTITY}}Repository {{ENTITY_LOWER}}Repository;

    @Mock
    private {{ENTITY}}Mapper {{ENTITY_LOWER}}Mapper;

    @InjectMocks
    private {{ENTITY}}Service {{ENTITY_LOWER}}Service;

    private {{ENTITY}} testEntity;
    private {{ENTITY}}CreateDto createDto;
    private {{ENTITY}}ResponseDto responseDto;

    @BeforeEach
    void setUp() {
        testEntity = {{ENTITY}}.builder()
            .id(1L)
            .{{FIELD_LOWER}}("Test {{FIELD}}")
            .{{NUMERIC_FIELD_LOWER}}(100)
            .description("Test description")
            .isActive(true)
            .build();

        createDto = {{ENTITY}}CreateDto.builder()
            .{{FIELD_LOWER}}("Test {{FIELD}}")
            .{{NUMERIC_FIELD_LOWER}}(100)
            .description("Test description")
            .build();

        responseDto = {{ENTITY}}ResponseDto.builder()
            .id(1L)
            .{{FIELD_LOWER}}("Test {{FIELD}}")
            .{{NUMERIC_FIELD_LOWER}}(100)
            .description("Test description")
            .isActive(true)
            .build();
    }

    @Nested
    @DisplayName("Create {{ENTITY}} Tests")
    class CreateTests {

        @Test
        @DisplayName("Should create {{ENTITY}} successfully")
        void shouldCreate{{ENTITY}}Successfully() {
            // Given
            when({{ENTITY_LOWER}}Mapper.toEntity(createDto)).thenReturn(testEntity);
            when({{ENTITY_LOWER}}Repository.save(testEntity)).thenReturn(testEntity);
            when({{ENTITY_LOWER}}Mapper.toDto(testEntity)).thenReturn(responseDto);

            // When
            {{ENTITY}}ResponseDto result = {{ENTITY_LOWER}}Service.create(createDto);

            // Then
            assertThat(result).isNotNull();
            assertThat(result.getId()).isEqualTo(1L);
            assertThat(result.get{{FIELD}}()).isEqualTo("Test {{FIELD}}");

            verify({{ENTITY_LOWER}}Repository).save(testEntity);
            verify({{ENTITY_LOWER}}Mapper).toDto(testEntity);
        }

        @Test
        @DisplayName("Should throw exception when validation fails")
        void shouldThrowExceptionWhenValidationFails() {
            // Given
            {{ENTITY}}CreateDto invalidDto = {{ENTITY}}CreateDto.builder().build();

            // When & Then
            assertThatThrownBy(() -> {{ENTITY_LOWER}}Service.create(invalidDto))
                .isInstanceOf(ValidationException.class);
        }
    }

    @Nested
    @DisplayName("Find {{ENTITY}} Tests")
    class FindTests {

        @Test
        @DisplayName("Should find {{ENTITY}} by ID successfully")
        void shouldFind{{ENTITY}}ByIdSuccessfully() {
            // Given
            when({{ENTITY_LOWER}}Repository.findById(1L)).thenReturn(Optional.of(testEntity));
            when({{ENTITY_LOWER}}Mapper.toDto(testEntity)).thenReturn(responseDto);

            // When
            Optional<{{ENTITY}}ResponseDto> result = {{ENTITY_LOWER}}Service.findById(1L);

            // Then
            assertThat(result).isPresent();
            assertThat(result.get().getId()).isEqualTo(1L);

            verify({{ENTITY_LOWER}}Repository).findById(1L);
        }

        @Test
        @DisplayName("Should return empty when {{ENTITY}} not found")
        void shouldReturnEmptyWhen{{ENTITY}}NotFound() {
            // Given
            when({{ENTITY_LOWER}}Repository.findById(999L)).thenReturn(Optional.empty());

            // When
            Optional<{{ENTITY}}ResponseDto> result = {{ENTITY_LOWER}}Service.findById(999L);

            // Then
            assertThat(result).isEmpty();
        }
    }

    @Nested
    @DisplayName("Delete {{ENTITY}} Tests")
    class DeleteTests {

        @Test
        @DisplayName("Should delete {{ENTITY}} successfully")
        void shouldDelete{{ENTITY}}Successfully() {
            // Given
            when({{ENTITY_LOWER}}Repository.existsById(1L)).thenReturn(true);

            // When
            {{ENTITY_LOWER}}Service.delete(1L);

            // Then
            verify({{ENTITY_LOWER}}Repository).deleteById(1L);
        }

        @Test
        @DisplayName("Should throw exception when {{ENTITY}} not found")
        void shouldThrowExceptionWhen{{ENTITY}}NotFound() {
            // Given
            when({{ENTITY_LOWER}}Repository.existsById(999L)).thenReturn(false);

            // When & Then
            assertThatThrownBy(() -> {{ENTITY_LOWER}}Service.delete(999L))
                .isInstanceOf(ResourceNotFoundException.class)
                .hasMessageContaining("{{ENTITY}} not found");
        }
    }
}
```

**Testing Standards:**
- Use JUnit 5 (Jupiter)
- Use AssertJ for fluent assertions
- Use Mockito for mocking
- Organize tests with @Nested classes
- Use @DisplayName for readable test names
- Follow Given-When-Then pattern
- Target >80% code coverage

**Agent Integration:**
- Generated by: `test-strategist`, `feature-developer`
- Reviewed by: `qa-engineer`

---

### 3.2 Integration Test Template

**File:** `.claude/templates/testing/integration-test.java`

**Purpose:** End-to-end API integration tests

**Structure:**
```java
package {{PACKAGE_NAME}}.controller;

import {{PACKAGE_NAME}}.dto.{{ENTITY}}CreateDto;
import {{PACKAGE_NAME}}.dto.{{ENTITY}}ResponseDto;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.transaction.annotation.Transactional;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;
import static org.hamcrest.Matchers.*;

/**
 * Integration tests for {{ENTITY}}Controller.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
@Transactional
@DisplayName("{{ENTITY}} API Integration Tests")
class {{ENTITY}}ControllerIntegrationTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    private {{ENTITY}}CreateDto createDto;

    @BeforeEach
    void setUp() {
        createDto = {{ENTITY}}CreateDto.builder()
            .{{FIELD_LOWER}}("Integration Test {{FIELD}}")
            .{{NUMERIC_FIELD_LOWER}}(200)
            .description("Integration test description")
            .build();
    }

    @Nested
    @DisplayName("POST /api/v1/{{RESOURCE_PATH}}")
    class CreateEndpointTests {

        @Test
        @DisplayName("Should create {{ENTITY}} and return 201")
        void shouldCreate{{ENTITY}}AndReturn201() throws Exception {
            mockMvc.perform(post("/api/v1/{{RESOURCE_PATH}}")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(objectMapper.writeValueAsString(createDto)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id").exists())
                .andExpect(jsonPath("$.{{FIELD_LOWER}}").value(createDto.get{{FIELD}}()))
                .andExpect(jsonPath("$.{{NUMERIC_FIELD_LOWER}}").value(createDto.get{{NUMERIC_FIELD}}()))
                .andExpect(jsonPath("$.createdAt").exists());
        }

        @Test
        @DisplayName("Should return 400 when validation fails")
        void shouldReturn400WhenValidationFails() throws Exception {
            {{ENTITY}}CreateDto invalidDto = {{ENTITY}}CreateDto.builder().build();

            mockMvc.perform(post("/api/v1/{{RESOURCE_PATH}}")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(objectMapper.writeValueAsString(invalidDto)))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.errors").isArray());
        }
    }

    @Nested
    @DisplayName("GET /api/v1/{{RESOURCE_PATH}}/{id}")
    class GetByIdEndpointTests {

        @Test
        @DisplayName("Should get {{ENTITY}} by ID and return 200")
        void shouldGet{{ENTITY}}ByIdAndReturn200() throws Exception {
            // First create a {{ENTITY}}
            String createResponse = mockMvc.perform(post("/api/v1/{{RESOURCE_PATH}}")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(objectMapper.writeValueAsString(createDto)))
                .andReturn()
                .getResponse()
                .getContentAsString();

            {{ENTITY}}ResponseDto created = objectMapper.readValue(createResponse, {{ENTITY}}ResponseDto.class);

            // Then retrieve it
            mockMvc.perform(get("/api/v1/{{RESOURCE_PATH}}/{id}", created.getId()))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(created.getId()))
                .andExpect(jsonPath("$.{{FIELD_LOWER}}").value(createDto.get{{FIELD}}()));
        }

        @Test
        @DisplayName("Should return 404 when {{ENTITY}} not found")
        void shouldReturn404When{{ENTITY}}NotFound() throws Exception {
            mockMvc.perform(get("/api/v1/{{RESOURCE_PATH}}/{id}", 99999L))
                .andExpect(status().isNotFound());
        }
    }

    @Nested
    @DisplayName("DELETE /api/v1/{{RESOURCE_PATH}}/{id}")
    class DeleteEndpointTests {

        @Test
        @DisplayName("Should delete {{ENTITY}} and return 204")
        void shouldDelete{{ENTITY}}AndReturn204() throws Exception {
            // First create a {{ENTITY}}
            String createResponse = mockMvc.perform(post("/api/v1/{{RESOURCE_PATH}}")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(objectMapper.writeValueAsString(createDto)))
                .andReturn()
                .getResponse()
                .getContentAsString();

            {{ENTITY}}ResponseDto created = objectMapper.readValue(createResponse, {{ENTITY}}ResponseDto.class);

            // Then delete it
            mockMvc.perform(delete("/api/v1/{{RESOURCE_PATH}}/{id}", created.getId()))
                .andExpect(status().isNoContent());

            // Verify it's deleted
            mockMvc.perform(get("/api/v1/{{RESOURCE_PATH}}/{id}", created.getId()))
                .andExpect(status().isNotFound());
        }
    }
}
```

**Agent Integration:**
- Generated by: `test-strategist`, `qa-engineer`
- Reviewed by: `code-reviewer`

---

### 3.3 Performance Test Template

**File:** `.claude/templates/testing/performance-test.java`

**Purpose:** Load and performance testing with JMeter or Gatling

**Structure:**
```java
package {{PACKAGE_NAME}}.performance;

import io.gatling.javaapi.core.*;
import io.gatling.javaapi.http.*;

import static io.gatling.javaapi.core.CoreDsl.*;
import static io.gatling.javaapi.http.HttpDsl.*;

/**
 * Performance test for {{ENTITY}} API endpoints.
 *
 * @author {{AUTHOR}}
 * @version 1.0
 * @since {{DATE}}
 */
public class {{ENTITY}}PerformanceTest extends Simulation {

    private HttpProtocolBuilder httpProtocol = http
        .baseUrl("{{BASE_URL}}")
        .acceptHeader("application/json")
        .contentTypeHeader("application/json");

    private ScenarioBuilder scn = scenario("{{ENTITY}} Performance Test")
        .exec(
            http("Create {{ENTITY}}")
                .post("/api/v1/{{RESOURCE_PATH}}")
                .body(StringBody("""
                    {
                        "{{FIELD_LOWER}}": "Performance Test",
                        "{{NUMERIC_FIELD_LOWER}}": 100
                    }
                    """))
                .check(status().is(201))
                .check(jsonPath("$.id").saveAs("entityId"))
        )
        .pause(1)
        .exec(
            http("Get {{ENTITY}}")
                .get("/api/v1/{{RESOURCE_PATH}}/#{entityId}")
                .check(status().is(200))
        )
        .pause(1)
        .exec(
            http("Update {{ENTITY}}")
                .put("/api/v1/{{RESOURCE_PATH}}/#{entityId}")
                .body(StringBody("""
                    {
                        "{{FIELD_LOWER}}": "Updated Performance Test",
                        "{{NUMERIC_FIELD_LOWER}}": 200
                    }
                    """))
                .check(status().is(200))
        )
        .pause(1)
        .exec(
            http("Delete {{ENTITY}}")
                .delete("/api/v1/{{RESOURCE_PATH}}/#{entityId}")
                .check(status().is(204))
        );

    {
        setUp(
            scn.injectOpen(
                rampUsers(100).during(60),  // Ramp up 100 users over 60 seconds
                constantUsersPerSec(10).during(120)  // Sustained load
            )
        ).protocols(httpProtocol)
         .assertions(
             global().responseTime().percentile3().lt(2000),  // 95th percentile < 2s
             global().successfulRequests().percent().gt(95.0)  // >95% success rate
         );
    }
}
```

**Performance Targets:**
- Response time: p95 < 2000ms, p99 < 5000ms
- Throughput: >100 requests/second
- Success rate: >95%
- Concurrent users: 100+

**Agent Integration:**
- Generated by: `test-strategist`, `performance-specialist`
- Reviewed by: `qa-engineer`, `deployment-manager`

---

## 4. Documentation Templates

### 4.1 API Documentation Template

**File:** `.claude/templates/docs/api-documentation.md`

**Purpose:** Comprehensive REST API documentation

**Structure:**
```markdown
---
api_name: {{API_NAME}}
version: {{VERSION}}
base_url: {{BASE_URL}}
last_updated: {{DATE}}
owner: {{OWNER}}
---

# {{API_NAME}} API Documentation

## Overview

{{API_DESCRIPTION}}

**Base URL:** `{{BASE_URL}}`
**Version:** {{VERSION}}
**Authentication:** {{AUTH_TYPE}}

## Authentication

{{AUTHENTICATION_DETAILS}}

### Example Request with Auth
```bash
curl -X GET "{{BASE_URL}}/api/v1/{{RESOURCE}}" \
  -H "Authorization: Bearer {token}"
```

## Endpoints

### 1. Create {{ENTITY}}

**Endpoint:** `POST /api/v1/{{RESOURCE_PATH}}`
**Description:** Creates a new {{ENTITY}}

#### Request Body
```json
{
  "{{FIELD_LOWER}}": "string",
  "{{NUMERIC_FIELD_LOWER}}": 0,
  "description": "string"
}
```

#### Response (201 Created)
```json
{
  "id": 1,
  "{{FIELD_LOWER}}": "string",
  "{{NUMERIC_FIELD_LOWER}}": 0,
  "description": "string",
  "isActive": true,
  "createdAt": "2025-10-01T12:00:00Z",
  "updatedAt": "2025-10-01T12:00:00Z"
}
```

#### Error Responses

**400 Bad Request**
```json
{
  "timestamp": "2025-10-01T12:00:00Z",
  "status": 400,
  "error": "Bad Request",
  "message": "Validation failed",
  "errors": [
    {
      "field": "{{FIELD_LOWER}}",
      "message": "{{FIELD}} is required"
    }
  ]
}
```

#### Example
```bash
curl -X POST "{{BASE_URL}}/api/v1/{{RESOURCE_PATH}}" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "{{FIELD_LOWER}}": "Example",
    "{{NUMERIC_FIELD_LOWER}}": 100,
    "description": "Example description"
  }'
```

### 2. Get {{ENTITY}} by ID

**Endpoint:** `GET /api/v1/{{RESOURCE_PATH}}/{id}`
**Description:** Retrieves a {{ENTITY}} by ID

#### Path Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| id | Long | {{ENTITY}} ID |

#### Response (200 OK)
```json
{
  "id": 1,
  "{{FIELD_LOWER}}": "string",
  "{{NUMERIC_FIELD_LOWER}}": 0,
  "description": "string",
  "isActive": true,
  "createdAt": "2025-10-01T12:00:00Z",
  "updatedAt": "2025-10-01T12:00:00Z"
}
```

#### Error Responses

**404 Not Found**
```json
{
  "timestamp": "2025-10-01T12:00:00Z",
  "status": 404,
  "error": "Not Found",
  "message": "{{ENTITY}} not found with ID: 1"
}
```

## Data Models

### {{ENTITY}}CreateDto
| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| {{FIELD_LOWER}} | String | Yes | Max 100 chars | {{FIELD_DESCRIPTION}} |
| {{NUMERIC_FIELD_LOWER}} | Integer | Yes | Min 0 | {{NUMERIC_FIELD_DESCRIPTION}} |
| description | String | No | Max 500 chars | Optional description |

### {{ENTITY}}ResponseDto
| Field | Type | Description |
|-------|------|-------------|
| id | Long | Unique identifier |
| {{FIELD_LOWER}} | String | {{FIELD_DESCRIPTION}} |
| {{NUMERIC_FIELD_LOWER}} | Integer | {{NUMERIC_FIELD_DESCRIPTION}} |
| description | String | Description |
| isActive | Boolean | Active status |
| createdAt | DateTime | Creation timestamp |
| updatedAt | DateTime | Last update timestamp |

## Rate Limiting

{{RATE_LIMIT_DESCRIPTION}}

## Pagination

All list endpoints support pagination with the following query parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | Integer | 0 | Page number (0-indexed) |
| size | Integer | 20 | Page size |
| sort | String | id,asc | Sort criteria |

### Example
```bash
GET /api/v1/{{RESOURCE_PATH}}?page=0&size=20&sort=createdAt,desc
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Validation error |
| 401 | Unauthorized - Missing/invalid auth |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 409 | Conflict - Duplicate resource |
| 500 | Internal Server Error |

## Changelog

### Version {{VERSION}} ({{DATE}})
- {{CHANGE_1}}
- {{CHANGE_2}}
```

**Agent Integration:**
- Generated by: `documentation-specialist`, `api-design-assistant`
- Reviewed by: `technical-architect`

---

### 4.2 Technical Specification Template

**File:** `.claude/templates/docs/technical-spec.md`

**Purpose:** Detailed technical design document

**Structure:**
```markdown
---
title: {{FEATURE_NAME}} Technical Specification
version: {{VERSION}}
status: {{DRAFT|REVIEW|APPROVED}}
authors: {{AUTHORS}}
reviewers: {{REVIEWERS}}
created: {{DATE}}
updated: {{DATE}}
---

# {{FEATURE_NAME}} Technical Specification

## 1. Overview

### 1.1 Purpose
{{FEATURE_PURPOSE}}

### 1.2 Scope
{{WHAT_IS_IN_SCOPE}}

### 1.3 Goals
- {{GOAL_1}}
- {{GOAL_2}}
- {{GOAL_3}}

### 1.4 Non-Goals
- {{NON_GOAL_1}}
- {{NON_GOAL_2}}

## 2. Background

### 2.1 Current State
{{DESCRIBE_CURRENT_IMPLEMENTATION}}

### 2.2 Problem Statement
{{PROBLEM_BEING_SOLVED}}

### 2.3 Success Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| {{METRIC_1}} | {{TARGET_1}} | {{HOW_TO_MEASURE_1}} |
| {{METRIC_2}} | {{TARGET_2}} | {{HOW_TO_MEASURE_2}} |

## 3. Architecture

### 3.1 High-Level Design

```
[Architecture Diagram]
```

### 3.2 Component Diagram

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│  Controller │─────▶│   Service   │─────▶│ Repository  │
└─────────────┘      └─────────────┘      └─────────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │  External   │
                     │   Service   │
                     └─────────────┘
```

### 3.3 Data Model

```sql
CREATE TABLE {{TABLE_NAME}} (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    {{FIELD_COLUMN}} VARCHAR(100) NOT NULL,
    {{NUMERIC_FIELD_COLUMN}} INT NOT NULL,
    description VARCHAR(500),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    version BIGINT DEFAULT 0,
    INDEX idx_{{FIELD_COLUMN}} ({{FIELD_COLUMN}})
);
```

### 3.4 API Design

#### Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | /api/v1/{{RESOURCE}} | Create {{ENTITY}} |
| GET | /api/v1/{{RESOURCE}}/{id} | Get {{ENTITY}} by ID |
| GET | /api/v1/{{RESOURCE}} | List {{ENTITY}}s |
| PUT | /api/v1/{{RESOURCE}}/{id} | Update {{ENTITY}} |
| DELETE | /api/v1/{{RESOURCE}}/{id} | Delete {{ENTITY}} |

## 4. Implementation Details

### 4.1 Technology Stack
- **Framework:** {{FRAMEWORK}}
- **Language:** {{LANGUAGE}}
- **Database:** {{DATABASE}}
- **Cache:** {{CACHE_LAYER}}
- **Message Queue:** {{MESSAGE_QUEUE}}

### 4.2 Key Classes

#### {{ENTITY}}Controller
- Handles HTTP requests
- Validates input
- Returns appropriate HTTP status codes

#### {{ENTITY}}Service
- Business logic
- Transaction management
- Validation rules

#### {{ENTITY}}Repository
- Data access layer
- Custom queries
- Database operations

### 4.3 Algorithms
{{DESCRIBE_KEY_ALGORITHMS}}

### 4.4 Security Considerations
- {{SECURITY_CONCERN_1}}
- {{SECURITY_CONCERN_2}}
- {{AUTHENTICATION_APPROACH}}
- {{AUTHORIZATION_RULES}}

## 5. Testing Strategy

### 5.1 Unit Tests
- Service layer: {{COVERAGE_TARGET}}%
- Repository layer: {{COVERAGE_TARGET}}%

### 5.2 Integration Tests
- API endpoints: All CRUD operations
- Database transactions
- Error scenarios

### 5.3 Performance Tests
- Load test: {{USERS}} concurrent users
- Response time: p95 < {{TIME}}ms
- Throughput: >{{RPS}} requests/second

## 6. Deployment

### 6.1 Deployment Steps
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

### 6.2 Rollback Plan
{{ROLLBACK_PROCEDURE}}

### 6.3 Monitoring
- Metrics: {{METRICS_TO_MONITOR}}
- Alerts: {{ALERT_CONDITIONS}}
- Dashboards: {{DASHBOARD_LINKS}}

## 7. Dependencies

### 7.1 External Services
- {{SERVICE_1}}: {{PURPOSE_1}}
- {{SERVICE_2}}: {{PURPOSE_2}}

### 7.2 Libraries
| Library | Version | Purpose |
|---------|---------|---------|
| {{LIB_1}} | {{VERSION_1}} | {{PURPOSE_1}} |
| {{LIB_2}} | {{VERSION_2}} | {{PURPOSE_2}} |

## 8. Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| {{RISK_1}} | {{IMPACT_1}} | {{PROB_1}} | {{MITIGATION_1}} |
| {{RISK_2}} | {{IMPACT_2}} | {{PROB_2}} | {{MITIGATION_2}} |

## 9. Timeline

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Design | {{DAYS}} days | Tech spec, API design |
| Implementation | {{DAYS}} days | Feature complete |
| Testing | {{DAYS}} days | All tests passing |
| Deployment | {{DAYS}} days | Production release |

## 10. Open Questions

- [ ] {{QUESTION_1}}
- [ ] {{QUESTION_2}}

## 11. References

- {{REFERENCE_1}}
- {{REFERENCE_2}}
```

**Agent Integration:**
- Generated by: `technical-architect`, `documentation-specialist`
- Reviewed by: `application-architect`, `feature-developer`

---

### 4.3 User Guide Template

**File:** `.claude/templates/docs/user-guide.md`

**Purpose:** End-user documentation

**Structure:**
```markdown
---
title: {{FEATURE_NAME}} User Guide
version: {{VERSION}}
audience: {{END_USERS|DEVELOPERS|ADMINS}}
last_updated: {{DATE}}
---

# {{FEATURE_NAME}} User Guide

## Introduction

{{BRIEF_DESCRIPTION_OF_FEATURE}}

## Prerequisites

- {{PREREQUISITE_1}}
- {{PREREQUISITE_2}}

## Getting Started

### Step 1: {{FIRST_STEP_TITLE}}

{{STEP_1_DESCRIPTION}}

**Example:**
```
{{EXAMPLE_COMMAND_OR_ACTION}}
```

### Step 2: {{SECOND_STEP_TITLE}}

{{STEP_2_DESCRIPTION}}

[Screenshot or diagram]

## Common Tasks

### Task 1: {{TASK_TITLE}}

**Goal:** {{WHAT_USER_WANTS_TO_ACHIEVE}}

**Steps:**
1. {{ACTION_1}}
2. {{ACTION_2}}
3. {{ACTION_3}}

**Result:** {{EXPECTED_OUTCOME}}

## Troubleshooting

### Issue: {{COMMON_PROBLEM_1}}

**Symptoms:** {{WHAT_USER_SEES}}

**Solution:**
1. {{FIX_STEP_1}}
2. {{FIX_STEP_2}}

### Issue: {{COMMON_PROBLEM_2}}

**Symptoms:** {{WHAT_USER_SEES}}

**Solution:** {{FIX_DESCRIPTION}}

## FAQ

**Q: {{QUESTION_1}}**
A: {{ANSWER_1}}

**Q: {{QUESTION_2}}**
A: {{ANSWER_2}}

## Additional Resources

- {{LINK_1}}
- {{LINK_2}}

## Support

For additional help, contact: {{SUPPORT_CONTACT}}
```

**Agent Integration:**
- Generated by: `documentation-specialist`
- Reviewed by: `product-owner`, `business-analyst`

---

## 5. Architecture Templates

### 5.1 Architectural Decision Record (ADR) Template

**File:** `.claude/templates/architecture/adr-template.md`

**Purpose:** Document significant architectural decisions

**Structure:**
```markdown
---
adr_number: {{ADR_NUMBER}}
title: {{DECISION_TITLE}}
status: {{PROPOSED|ACCEPTED|DEPRECATED|SUPERSEDED}}
date: {{DATE}}
deciders: {{DECISION_MAKERS}}
supersedes: {{ADR_NUMBER_IF_APPLICABLE}}
superseded_by: {{ADR_NUMBER_IF_APPLICABLE}}
---

# ADR-{{ADR_NUMBER}}: {{DECISION_TITLE}}

## Status

{{PROPOSED|ACCEPTED|DEPRECATED|SUPERSEDED}}

**Date:** {{DATE}}

## Context

{{WHAT_IS_THE_ISSUE_THAT_IS_MOTIVATING_THIS_DECISION}}

### Background
{{ADDITIONAL_CONTEXT}}

### Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}

### Assumptions
- {{ASSUMPTION_1}}
- {{ASSUMPTION_2}}

## Decision

{{WHAT_IS_THE_CHANGE_THAT_WE_ARE_PROPOSING}}

### Rationale
{{WHY_DID_WE_CHOOSE_THIS_APPROACH}}

## Consequences

### Positive
- {{BENEFIT_1}}
- {{BENEFIT_2}}

### Negative
- {{DRAWBACK_1}}
- {{DRAWBACK_2}}

### Neutral
- {{NEUTRAL_IMPACT_1}}
- {{NEUTRAL_IMPACT_2}}

## Alternatives Considered

### Option 1: {{ALTERNATIVE_NAME_1}}

**Description:** {{DESCRIPTION_1}}

**Pros:**
- {{PRO_1}}
- {{PRO_2}}

**Cons:**
- {{CON_1}}
- {{CON_2}}

**Rejected because:** {{REASON_1}}

### Option 2: {{ALTERNATIVE_NAME_2}}

**Description:** {{DESCRIPTION_2}}

**Pros:**
- {{PRO_1}}
- {{PRO_2}}

**Cons:**
- {{CON_1}}
- {{CON_2}}

**Rejected because:** {{REASON_2}}

## Implementation

### Migration Strategy
{{HOW_WILL_WE_IMPLEMENT_THIS_DECISION}}

### Affected Components
- {{COMPONENT_1}}
- {{COMPONENT_2}}

### Effort Estimate
{{TIME_AND_RESOURCES_REQUIRED}}

## Compliance

### Standards
- {{STANDARD_1}}: {{COMPLIANCE_STATUS_1}}
- {{STANDARD_2}}: {{COMPLIANCE_STATUS_2}}

### Security Considerations
{{SECURITY_IMPLICATIONS}}

## Monitoring & Validation

### Success Criteria
- {{CRITERION_1}}
- {{CRITERION_2}}

### Metrics
- {{METRIC_1}}: {{TARGET_1}}
- {{METRIC_2}}: {{TARGET_2}}

## References

- {{LINK_1}}
- {{LINK_2}}
- Related ADRs: ADR-XXX, ADR-YYY

## Notes

{{ADDITIONAL_NOTES_OR_DISCUSSION_POINTS}}
```

**ADR Status Workflow:**
- **Proposed** → **Accepted** → **Deprecated** → **Superseded**

**Agent Integration:**
- Created by: `application-architect`, `technical-architect`
- Reviewed by: `scrum-master`, `feature-developer`

---

### 5.2 Architecture Review Template

**File:** `.claude/templates/architecture/architecture-review.md`

**Purpose:** Systematic architecture evaluation

**Structure:**
```markdown
---
review_type: {{INITIAL|PERIODIC|PRE_RELEASE}}
date: {{DATE}}
reviewers: {{REVIEWERS}}
components_reviewed: {{COMPONENTS}}
---

# Architecture Review: {{SYSTEM_NAME}}

## Review Summary

**Date:** {{DATE}}
**Reviewers:** {{REVIEWERS}}
**Scope:** {{WHAT_WAS_REVIEWED}}

**Overall Assessment:** {{PASS|PASS_WITH_CONCERNS|FAIL}}

## Layer Analysis

### Controller Layer

**Compliance:** {{SCORE}}/10

**Findings:**
- ✅ {{POSITIVE_FINDING_1}}
- ⚠️ {{CONCERN_1}}
- ❌ {{VIOLATION_1}}

**Recommendations:**
1. {{RECOMMENDATION_1}}
2. {{RECOMMENDATION_2}}

### Service Layer

**Compliance:** {{SCORE}}/10

**Findings:**
- {{FINDINGS}}

**Recommendations:**
- {{RECOMMENDATIONS}}

### Repository Layer

**Compliance:** {{SCORE}}/10

**Findings:**
- {{FINDINGS}}

**Recommendations:**
- {{RECOMMENDATIONS}}

## Pattern Compliance

### Dependency Injection

**Status:** {{PASS|FAIL}}

| Issue | Location | Severity | Recommendation |
|-------|----------|----------|----------------|
| Field injection used | {{CLASS}}:{{LINE}} | Medium | Use constructor injection |

### Transaction Management

**Status:** {{PASS|FAIL}}

**Findings:**
- {{FINDING_1}}
- {{FINDING_2}}

### Exception Handling

**Status:** {{PASS|FAIL}}

**Findings:**
- {{FINDING_1}}

## Anti-Patterns Detected

| Anti-Pattern | Location | Impact | Fix Priority |
|--------------|----------|--------|--------------|
| {{PATTERN_1}} | {{FILE}}:{{LINE}} | High | P0 |
| {{PATTERN_2}} | {{FILE}}:{{LINE}} | Medium | P1 |

## Security Assessment

### Authentication/Authorization

**Status:** {{PASS|FAIL}}

**Findings:**
- {{SECURITY_FINDING_1}}
- {{SECURITY_FINDING_2}}

### Data Protection

**Status:** {{PASS|FAIL}}

**Findings:**
- {{FINDING_1}}

## Performance Considerations

| Concern | Impact | Recommendation |
|---------|--------|----------------|
| {{CONCERN_1}} | {{IMPACT_1}} | {{RECOMMENDATION_1}} |
| {{CONCERN_2}} | {{IMPACT_2}} | {{RECOMMENDATION_2}} |

## Technical Debt

| Debt Item | Interest Rate | Remediation Effort |
|-----------|---------------|---------------------|
| {{DEBT_1}} | {{IMPACT_1}} | {{EFFORT_1}} |

## Action Items

| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| {{ACTION_1}} | {{OWNER_1}} | P0 | {{DATE_1}} |
| {{ACTION_2}} | {{OWNER_2}} | P1 | {{DATE_2}} |

## Architecture Decision Records

**ADRs Reviewed:**
- ADR-XXX: {{STATUS}}
- ADR-YYY: {{STATUS}}

**New ADRs Needed:**
- {{TOPIC_1}}
- {{TOPIC_2}}

## Conclusion

{{OVERALL_ASSESSMENT_AND_NEXT_STEPS}}
```

**Agent Integration:**
- Conducted by: `application-architect`, `technical-architect`
- Executed via: `/architecture-review` command

---

## 6. Template Usage Guidelines

### 6.1 Template Discovery

Templates are stored in `.claude/templates/` and organized by category:

```
.claude/templates/
├── agile/              # User stories, epics, bugs, retrospectives
├── code/               # Controllers, services, entities, DTOs
├── testing/            # Unit tests, integration tests, performance tests
├── docs/               # API docs, technical specs, user guides
└── architecture/       # ADRs, architecture reviews
```

### 6.2 Template Invocation

**Via Commands:**
```bash
/generate-feature Product     # Uses code templates
/test-strategy               # Uses testing templates
/sprint-planning             # Uses agile templates
/architecture-review         # Uses architecture templates
```

**Via Agents:**
- `feature-developer`: Uses code + testing templates
- `sprint-story-manager`: Uses agile templates
- `test-strategist`: Uses testing templates
- `documentation-specialist`: Uses docs templates
- `application-architect`: Uses architecture templates

### 6.3 Variable Substitution

All templates use `{{VARIABLE}}` notation for placeholders:

**Naming Conventions:**
- `{{ENTITY}}`: PascalCase entity name (e.g., Product, User)
- `{{ENTITY_LOWER}}`: camelCase entity name (e.g., product, user)
- `{{ENTITY_UPPER}}`: UPPER_SNAKE_CASE (e.g., PRODUCT, USER)
- `{{FIELD}}`: Field name in PascalCase
- `{{FIELD_LOWER}}`: Field name in camelCase
- `{{FIELD_COLUMN}}`: Database column name (snake_case)

### 6.4 Customization

Templates can be customized per project:

1. **Copy template** from default location
2. **Modify** to match project standards
3. **Save** in `.claude/templates/custom/`
4. **Configure** in `.claude/claude-config.yaml`:

```yaml
templates:
  custom_dir: .claude/templates/custom
  priority: custom  # Use custom templates first
```

### 6.5 Validation

Templates should be validated before use:

**Required Fields Check:**
```bash
# Verify all {{VARIABLES}} are substituted
grep -r "{{.*}}" <generated-file>
```

**Compilation Check:**
```bash
# For Java files
mvn compile

# For tests
mvn test-compile
```

### 6.6 Best Practices

1. **Consistency:** Use templates for all new code
2. **Evolution:** Update templates as standards evolve
3. **Documentation:** Document custom variables in template headers
4. **Review:** Review generated code, don't blindly accept
5. **Feedback:** Report template issues to improve quality

---

## 7. Template Maintenance

### 7.1 Version Control

All templates are versioned with the project:

```bash
git add .claude/templates/
git commit -m "Update templates for {{CHANGE}}"
```

### 7.2 Update Process

**When to Update Templates:**
- New framework version with breaking changes
- Updated coding standards
- Improved best practices discovered
- Security patterns updated
- Team retrospective feedback

**Update Procedure:**
1. Create branch: `git checkout -b update-templates`
2. Modify templates
3. Test with sample generation
4. Review with team
5. Merge to main

### 7.3 Template Testing

Before committing template changes:

```bash
# Generate sample code from template
/generate-feature SampleEntity --template-test

# Verify compilation
mvn clean compile

# Run tests
mvn test

# Check code quality
mvn checkstyle:check
```

### 7.4 Ownership

| Template Category | Owner | Review Cadence |
|-------------------|-------|----------------|
| Agile | Scrum Master, Product Owner | Quarterly |
| Code | Technical Architect | Bi-monthly |
| Testing | QA Engineer | Quarterly |
| Documentation | Documentation Specialist | Bi-monthly |
| Architecture | Application Architect | Quarterly |

### 7.5 Metrics

**Template Effectiveness Metrics:**
- Time saved per use: Target 30-40 minutes
- Code quality: 0 checkstyle violations
- Test coverage: >80% out of the box
- Developer satisfaction: >4/5 rating

**Collection Method:**
```bash
# Track usage
grep -r "template:" .claude/logs/ | wc -l

# Measure time savings
echo "Stories completed with templates: X"
echo "Time saved: X * 35 minutes"
```

---

## Appendices

### A. Template Variable Reference

| Variable | Example Value | Usage |
|----------|---------------|-------|
| `{{PACKAGE_NAME}}` | com.example.app | Java package |
| `{{ENTITY}}` | Product | Entity class name |
| `{{ENTITY_LOWER}}` | product | Variable name |
| `{{TABLE_NAME}}` | products | Database table |
| `{{RESOURCE_PATH}}` | products | API path |
| `{{AUTHOR}}` | John Doe | Code author |
| `{{DATE}}` | 2025-10-01 | Creation date |
| `{{VERSION}}` | 1.0 | Version number |

### B. Framework-Specific Variables

**Spring Boot:**
- `{{SPRING_VERSION}}`: Spring Boot version (e.g., 3.2.0)
- `{{JAVA_VERSION}}`: Java version (e.g., 17)

**Testing:**
- `{{TEST_FRAMEWORK}}`: JUnit 5, TestNG
- `{{MOCK_FRAMEWORK}}`: Mockito, EasyMock

### C. Template Composition

Templates can reference other templates:

```java
// In controller template
@Autowired
private {{ENTITY}}Service {{ENTITY_LOWER}}Service;  // References service template
```

This creates dependency chains: Controller → Service → Repository

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-10-01 | Claude Code | Initial template specifications |

**Next Review Date:** 2025-12-01

**Approval:**
- Technical Architect: _________________
- Scrum Master: _________________
- QA Engineer: _________________
