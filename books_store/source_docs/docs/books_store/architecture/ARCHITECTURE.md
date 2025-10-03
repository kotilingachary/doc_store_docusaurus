# Architecture Documentation

## Overview

This is a **Spring Boot 2.1.2 REST API** that demonstrates a simple book management system. The application follows a simplified 3-layer architecture pattern optimized for learning and demonstration purposes.

## Technology Stack

- **Framework**: Spring Boot 2.1.2
- **Java Version**: Java 8
- **Web Layer**: Spring MVC with REST controllers
- **Data Layer**: Spring Data JPA with Hibernate
- **Database**: H2 in-memory database
- **File Processing**: Apache Commons CSV, Apache POI (Excel)
- **Testing**: Spring Boot Test with MockMvc and Mockito
- **Build Tool**: Maven
- **Hot Reload**: Spring Boot DevTools

## Architectural Pattern

The project follows a **simplified 3-layer Spring MVC architecture**:

```
┌─────────────────────┐
│   REST Controller   │  ← BookController.java
│   (Presentation)    │
└─────────────────────┘
           │
           ▼
┌─────────────────────┐
│    Repository       │  ← BookRepository.java
│   (Data Access)     │
└─────────────────────┘
           │
           ▼
┌─────────────────────┐
│     Database        │  ← H2 In-Memory
│     (Storage)       │
└─────────────────────┘
```

**Note**: This architecture intentionally omits a traditional service layer for simplicity. In production applications, a service layer would typically handle business logic between the controller and repository.

## Core Components

### Application Entry Point
- **`StartBookApplication.java`**
  - Main Spring Boot application class with `@SpringBootApplication`
  - Contains `CommandLineRunner` bean for demo data initialization
  - Uses `@Profile("demo")` to conditionally load sample data
  - Seeds 3 books on startup when demo profile is active

### Domain Model
- **`Book.java`**
  - JPA entity representing the book domain object
  - Fields: `id` (auto-generated), `name`, `author`, `price` (BigDecimal)
  - Multiple constructors for different use cases
  - Standard getters/setters and toString implementation

### Data Access Layer
- **`BookRepository.java`**
  - Interface extending `JpaRepository<Book, Long>`
  - Provides automatic CRUD operations without custom implementation
  - Leverages Spring Data JPA conventions
  - No custom queries needed for basic operations

### REST API Layer
- **`BookController.java`**
  - Single `@RestController` handling all book-related endpoints
  - Direct repository injection via `@Autowired`
  - Implements full CRUD operations with proper HTTP semantics
  - Returns appropriate HTTP status codes (201 for creation, etc.)

### Error Handling
- **`error/` package**
  - `CustomGlobalExceptionHandler.java` - Global exception handler using `@ControllerAdvice`
  - `BookNotFoundException.java` - Custom exception for missing books
  - `BookUnSupportedFieldPatchException.java` - Exception for invalid PATCH operations
  - Centralized error handling with appropriate HTTP status codes

## API Design

### Endpoints
All endpoints follow REST conventions under the `/books` resource:

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| GET | `/books` | List all books | 200 |
| POST | `/books` | Create new book | 201 |
| POST | `/books/bulk` | **Bulk upload books from file** | 200/400 |
| GET | `/books/bulk/status/{id}` | **Get bulk operation status** | 200/404 |
| GET | `/books/{id}` | Get book by ID | 200/404 |
| PUT | `/books/{id}` | Update/create book | 200 |
| PATCH | `/books/{id}` | Partial update (author only) | 200/405 |
| DELETE | `/books/{id}` | Delete book | 200 |

### Request/Response Format
- **Content-Type**: `application/json`
- **Request Body**: JSON representation of Book object
- **Response**: JSON representation of Book object or list of books
- **Error Responses**: Standard HTTP error codes with minimal error information

### PATCH Operation Limitation
The PATCH endpoint only supports updating the `author` field. Attempting to update other fields throws a `BookUnSupportedFieldPatchException` (HTTP 405).

## Configuration

### Profile-Based Configuration
- **Demo Profile**: Loads sample data via `CommandLineRunner`
- **Test Profile**: Skips demo data initialization
- **Application Properties**: Minimal logging and error configuration

### Database Configuration
- **H2 In-Memory Database**: Automatic setup via Spring Boot auto-configuration
- **JPA/Hibernate**: Automatic table creation from entity definitions
- **No explicit database configuration required**

## Key Architectural Decisions

### 1. **Simplified Architecture**
- **Decision**: No service layer between controller and repository
- **Rationale**: Reduces complexity for demonstration/learning purposes
- **Trade-off**: Business logic mixed with presentation logic

### 2. **In-Memory Database**
- **Decision**: Use H2 in-memory database
- **Rationale**: Easy setup, no external dependencies, suitable for demos
- **Trade-off**: Data doesn't persist between application restarts

### 3. **Direct Repository Access**
- **Decision**: Controller directly injects and uses repository
- **Rationale**: Simplified data flow for basic CRUD operations
- **Trade-off**: Violates separation of concerns for complex business logic

### 4. **Exception-Driven Flow**
- **Decision**: Use exceptions for business logic (e.g., entity not found)
- **Rationale**: Leverages Spring's exception handling mechanisms
- **Trade-off**: Control flow via exceptions can be harder to follow

### 5. **Profile-Based Data Loading**
- **Decision**: Use Spring profiles to control demo data initialization
- **Rationale**: Separates test and demo environments cleanly
- **Trade-off**: Additional configuration complexity

## Testing Strategy

### Unit Testing
- **MockMvc**: For testing REST endpoints without starting full server
- **Mockito**: For mocking repository layer in controller tests
- **@SpringBootTest**: Integration testing with Spring context
- **Profile Isolation**: Tests use separate profile to avoid demo data interference

### Test Structure
- Controller tests focus on HTTP request/response handling
- Repository testing relies on Spring Data JPA test slices
- No service layer tests due to simplified architecture

## Bulk Upload Architecture

### Enhanced Architecture for Bulk Operations

The bulk upload feature introduces a more sophisticated architecture while maintaining the existing simplicity for individual operations:

```
┌─────────────────────┐    ┌─────────────────────┐
│   REST Controller   │    │  Bulk Upload API    │  ← BookController.java
│   (Individual)      │    │   (Batch Ops)       │     + bulk endpoints
└─────────────────────┘    └─────────────────────┘
           │                          │
           ▼                          ▼
┌─────────────────────┐    ┌─────────────────────┐
│   Direct Repository │    │   Bulk Service      │  ← BulkBookService.java
│   (CRUD Operations) │    │  (File Processing)  │     (NEW)
└─────────────────────┘    └─────────────────────┘
           │                          │
           │              ┌─────────────────────┐
           │              │  File Parser Utils  │  ← FileParserUtil.java
           │              │ (CSV/Excel Reader)  │     (NEW)
           │              └─────────────────────┘
           │                          │
           ▼                          ▼
┌─────────────────────────────────────────────────┐
│              Repository Layer                    │  ← BookRepository.java
│              (Data Access)                      │     + bulk operations
└─────────────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────┐
│                Database                         │  ← H2 In-Memory
│                (Storage)                        │
└─────────────────────────────────────────────────┘
```

### New Components for Bulk Operations

#### 1. **BulkBookService.java** (NEW)
- **Purpose**: Business logic for bulk file processing
- **Responsibilities**:
  - File format validation and parsing coordination
  - Batch validation of book records
  - Transaction management for bulk operations
  - Error collection and reporting
  - Progress tracking for large files

#### 2. **FileParserUtil.java** (NEW)
- **Purpose**: Utility for parsing CSV and Excel files
- **Responsibilities**:
  - CSV parsing with configurable delimiters
  - Excel worksheet reading (.xlsx, .xls support)
  - Data type conversion and formatting
  - Stream processing for memory efficiency

#### 3. **BulkUploadResult.java** (NEW)
- **Purpose**: DTO for bulk operation responses
- **Fields**:
  - `operationId`: Unique identifier for the operation
  - `status`: Processing status (completed, failed, in_progress)
  - `summary`: Success/failure counts
  - `errors`: List of validation errors with row details
  - `processedAt`: Timestamp of completion

#### 4. **BulkOperationStatus.java** (NEW)
- **Purpose**: Entity for tracking long-running operations
- **Fields**:
  - `id`: Operation identifier
  - `status`: Current processing status
  - `progress`: Percentage complete
  - `totalRecords`: Total records in file
  - `processedRecords`: Records processed so far
  - `errors`: Accumulated error list

### Enhanced BookRepository

```java
// Additional methods for bulk operations
public interface BookRepository extends JpaRepository<Book, Long> {
    // Existing methods...
    List<Book> findByAuthorIgnoreCase(String author);
    List<Book> findByNameIgnoreCase(String name);

    // New bulk operation methods
    @Modifying
    @Query("INSERT INTO Book (name, author, price) VALUES ?1")
    void bulkInsert(List<Book> books);

    // For duplicate detection (future enhancement)
    boolean existsByNameAndAuthor(String name, String author);
}
```

### File Processing Flow

```
File Upload → Validation → Parsing → Batch Validation → Database Insert → Response
     │             │          │           │                  │             │
     ▼             ▼          ▼           ▼                  ▼             ▼
[multipart]   [format]   [CSV/Excel]  [business]      [transaction]   [results]
[size check]  [type]     [streaming]  [rules]         [bulk insert]   [errors]
```

### Memory Management Strategy

```java
// Stream processing for large files
public BulkUploadResult processBulkUpload(MultipartFile file) {
    try (Stream<BookRecord> recordStream = parseFileAsStream(file)) {
        return recordStream
            .batch(BATCH_SIZE) // Process in chunks of 1000
            .map(this::validateAndTransform)
            .collect(toBulkUploadResult());
    }
}
```

### Error Handling Strategy

#### Validation Levels
1. **File Level**: Format, size, structure validation
2. **Record Level**: Individual book validation
3. **Business Level**: Duplicate detection, complex rules

#### Error Collection
```java
public class BulkUploadResult {
    private List<ValidationError> errors;

    public static class ValidationError {
        private int row;
        private String field;
        private String value;
        private String message;
        private String errorCode;
    }
}
```

### Transaction Management

```java
@Service
@Transactional
public class BulkBookService {

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void processBatch(List<Book> validBooks) {
        // Each batch in separate transaction
        // Allows partial success on failures
        bookRepository.saveAll(validBooks);
    }
}
```

### Security Considerations

#### File Upload Security
- **File Type Validation**: Whitelist CSV/Excel extensions
- **Content-Type Verification**: Validate actual file headers
- **Size Limits**: Enforce maximum file size (10MB)
- **Malicious Content Scanning**: Check for embedded scripts

#### Input Sanitization
```java
public Book sanitizeBookInput(BookRecord record) {
    return new Book(
        sanitizeInput(record.getName()),
        sanitizeInput(record.getAuthor()),
        validatePrice(record.getPrice())
    );
}
```

## Extension Points

For production use, consider these enhancements:

1. **Add Service Layer**: Implement business logic separation
2. **Persistent Database**: Replace H2 with PostgreSQL/MySQL
3. **Validation**: Add input validation with Bean Validation
4. **Security**: Implement authentication/authorization
5. **API Documentation**: Add Swagger/OpenAPI documentation
6. **Enhanced Error Handling**: Detailed error responses with error codes
7. **Logging**: Structured logging with correlation IDs
8. **Metrics**: Add actuator endpoints for monitoring