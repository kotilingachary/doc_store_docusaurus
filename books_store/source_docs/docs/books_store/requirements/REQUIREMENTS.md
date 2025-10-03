# Requirements Documentation

## Product Overview

The Book Management System is a REST API designed to provide basic CRUD operations for managing a library or bookstore inventory. The system allows users to create, read, update, and delete book records through a RESTful interface.

## Target Users

- **API Consumers**: Developers building front-end applications, mobile apps, or integrating with other systems
- **Library Staff**: Personnel managing book inventories
- **Bookstore Managers**: Staff tracking book information and pricing
- **Students/Learners**: Individuals learning REST API development with Spring Boot

## Core User Stories

### Epic 1: Book Information Management

#### US-001: View All Books
**As an** API consumer
**I want to** retrieve a list of all books in the system
**So that** I can display the complete inventory to users

**Acceptance Criteria:**
- Given the system contains books in the database
- When I send a GET request to `/books`
- Then I receive a 200 OK response
- And the response contains a JSON array of all book objects
- And each book object includes id, name, author, and price fields

**API Details:**
- Endpoint: `GET /books`
- Response: `200 OK` with JSON array
- No authentication required

---

#### US-002: View Individual Book Details
**As an** API consumer
**I want to** retrieve detailed information about a specific book
**So that** I can display complete book information to users

**Acceptance Criteria:**
- Given a book exists with a specific ID
- When I send a GET request to `/books/{id}` with that ID
- Then I receive a 200 OK response
- And the response contains the complete book object with all fields
- Given a book does not exist with the requested ID
- When I send a GET request to `/books/{id}` with that ID
- Then I receive a 404 Not Found response

**API Details:**
- Endpoint: `GET /books/{id}`
- Response: `200 OK` with book JSON object or `404 Not Found`
- Path parameter: `id` (Long)

---

#### US-003: Add New Book to Inventory
**As a** library staff member
**I want to** add new books to the system
**So that** the inventory reflects current available books

**Acceptance Criteria:**
- Given I have valid book information (name, author, price)
- When I send a POST request to `/books` with book data
- Then I receive a 201 Created response
- And the response contains the created book object with generated ID
- And the book is persisted in the database
- Given I send invalid or incomplete book data
- When I send a POST request to `/books`
- Then I receive an appropriate error response

**API Details:**
- Endpoint: `POST /books`
- Request Body: JSON book object (name, author, price)
- Response: `201 Created` with created book object
- Content-Type: `application/json`

---

### Epic 2: Book Information Updates

#### US-004: Update Complete Book Information
**As a** bookstore manager
**I want to** update all information for an existing book
**So that** I can correct errors or update pricing and details

**Acceptance Criteria:**
- Given a book exists with a specific ID
- When I send a PUT request to `/books/{id}` with complete book data
- Then I receive a 200 OK response
- And the response contains the updated book object
- And all fields are updated with the new values
- Given a book does not exist with the requested ID
- When I send a PUT request to `/books/{id}` with book data
- Then a new book is created with the specified ID
- And I receive a 200 OK response with the created book

**API Details:**
- Endpoint: `PUT /books/{id}`
- Request Body: Complete JSON book object
- Response: `200 OK` with updated/created book object
- Behavior: Update existing or create new (upsert)

---

#### US-005: Update Book Author Information
**As a** library staff member
**I want to** update only the author information for a book
**So that** I can correct author names without changing other details

**Acceptance Criteria:**
- Given a book exists with a specific ID
- When I send a PATCH request to `/books/{id}` with author field only
- Then I receive a 200 OK response
- And the response contains the book with updated author
- And other fields (name, price) remain unchanged
- Given I attempt to update fields other than author
- When I send a PATCH request to `/books/{id}` with other fields
- Then I receive a 405 Method Not Allowed response
- Given a book does not exist with the requested ID
- When I send a PATCH request to `/books/{id}`
- Then I receive a 404 Not Found response

**API Details:**
- Endpoint: `PATCH /books/{id}`
- Request Body: JSON object with "author" field only
- Response: `200 OK`, `404 Not Found`, or `405 Method Not Allowed`
- Limitation: Only author field updates supported

---

### Epic 3: Book Removal

#### US-006: Remove Book from Inventory
**As a** bookstore manager
**I want to** remove books from the system
**So that** discontinued or damaged books are no longer in inventory

**Acceptance Criteria:**
- Given a book exists with a specific ID
- When I send a DELETE request to `/books/{id}`
- Then I receive a 200 OK response
- And the book is removed from the database
- And subsequent GET requests for that ID return 404
- Given a book does not exist with the requested ID
- When I send a DELETE request to `/books/{id}`
- Then the operation completes without error (idempotent)

**API Details:**
- Endpoint: `DELETE /books/{id}`
- Response: `200 OK` (regardless of book existence)
- Behavior: Idempotent operation

---

### Epic 4: Bulk Operations

#### US-007: Bulk Book Upload via CSV/Excel Files
**As a** library staff member or bookstore manager
**I want to** upload multiple books at once using a CSV or Excel file
**So that** I can efficiently add large numbers of books to the inventory without manual entry

**Acceptance Criteria:**
- Given I have a valid CSV or Excel file with book data (name, author, price columns)
- When I send a POST request to `/books/bulk` with the file as multipart/form-data
- Then I receive a 200 OK response with detailed results
- And valid books are created in the database with auto-generated IDs
- And invalid books are reported with specific validation errors
- And the response includes counts of successful/failed operations
- Given I upload a file with mixed valid and invalid data
- When the bulk upload processes the file
- Then valid books are saved and invalid books are rejected
- And detailed error messages are provided for each validation failure
- Given I upload an invalid file format or corrupted file
- When I send the bulk upload request
- Then I receive a 400 Bad Request response with appropriate error message

**Technical Requirements:**
- File formats supported: CSV (.csv), Excel (.xlsx, .xls)
- Maximum file size: 10MB
- Maximum records per file: 10,000 books
- Required columns: name, author, price
- Optional columns: description, isbn, category
- Validation: Same rules as individual book creation
- Transaction handling: Partial success allowed (valid books saved despite invalid ones)
- Response format: JSON with success/failure counts and detailed error list

**API Details:**
- Endpoint: `POST /books/bulk`
- Request: multipart/form-data with file parameter
- Response: `200 OK` with bulk operation results or `400 Bad Request` for file errors
- Content-Type: multipart/form-data

---

#### US-008: Bulk Operation Status and Progress Tracking
**As a** user performing bulk operations
**I want to** track the progress and status of large file uploads
**So that** I know when the operation is complete and can see any issues

**Acceptance Criteria:**
- Given I upload a large file (>1000 records)
- When the bulk upload begins processing
- Then I receive an immediate response with operation ID
- And I can check operation status via GET `/books/bulk/status/{operationId}`
- And the status endpoint shows progress percentage and current status
- Given the bulk operation encounters validation errors
- When I check the operation status
- Then I see detailed validation errors for each failed record
- And I can download an error report with specific issues

**API Details:**
- Endpoint: `GET /books/bulk/status/{operationId}`
- Response: JSON with operation status, progress, and error details

---

### Epic 5: System Demonstration and Development

#### US-009: Demo Data for System Demonstration
**As a** developer or evaluator
**I want to** have sample data available when running in demo mode
**So that** I can immediately test and evaluate the system functionality

**Acceptance Criteria:**
- Given the application starts with "demo" profile active
- When the application initializes
- Then the database is populated with sample books
- And I can immediately test all API endpoints with existing data
- Given the application starts without "demo" profile
- When the application initializes
- Then the database starts empty
- And no sample data is loaded

**Configuration Details:**
- Profile: "demo" activates sample data loading
- Sample books: 3 different books with varying prices
- Automatic loading via CommandLineRunner

---
### Epic 6: UI Development

#### US-10: UI development
**As a** end user
**I want to** have a simple UI where I can browse and perform all the operations
**So that** I can immediately test and evaluate the system functionality

**Acceptance Criteria:**
-The user should be able to add
-User should be able to perform the CRUD operations


---
## Data Model Requirements

### Book Entity
**Required Fields:**
- `id`: Unique identifier (auto-generated Long)
- `name`: Book title (String, required)
- `author`: Book author (String, required)
- `price`: Book price (BigDecimal, required for monetary precision)

**Validation Rules:**
- ID must be unique and auto-generated
- Name and author cannot be null or empty
- Price must be a valid monetary value

## Technical Requirements

### Performance Requirements
- API response time: < 200ms for single book operations
- Support for concurrent requests
- Database operations must be transactional

### Error Handling Requirements
- Meaningful HTTP status codes for all operations
- Consistent error response format
- Graceful handling of invalid input data
- Proper exception handling for database errors

### Security Requirements
- Input validation for all API endpoints
- Protection against SQL injection (handled by JPA)
- No sensitive information in error messages

### Data Requirements
- In-memory database for demonstration purposes
- Data persistence during application runtime
- Automatic schema generation from entity definitions

## Non-Functional Requirements

### Reliability
- System should handle graceful shutdown
- Database integrity maintained during operations
- Proper transaction management

### Maintainability
- Clear separation of concerns in code architecture
- Comprehensive error handling
- Proper logging for debugging

### Usability
- RESTful API design following standard conventions
- Predictable endpoint patterns
- Clear and consistent response formats

## Future Enhancement Opportunities

### Potential User Stories for Next Releases
1. **Search and Filtering**: Find books by author, title, or price range
2. **Pagination**: Handle large book collections efficiently
3. **Book Categories**: Organize books by genre or category
4. **Advanced Validation**: ISBN validation, duplicate detection
5. **Bulk Export**: Export books to CSV/Excel formats
6. **User Management**: Authentication and authorization
7. **Audit Trail**: Track changes to book information
8. **Integration**: Connect with external book databases
9. **Reporting**: Generate inventory and sales reports
10. **API Documentation**: Interactive API documentation with Swagger

These enhancements would expand the system from a basic CRUD API to a comprehensive book management platform.
