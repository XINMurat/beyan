# Module: API Design Analysis

**Priority**: P1 (High for Backend/API Projects)  
**Tokens**: ~2000  
**Analysis Time**: 8-12 minutes  

---

## Purpose

Evaluate REST/GraphQL API design quality, consistency, documentation, error handling, versioning, and adherence to industry standards.

---

## REST API Standards

```yaml
http_methods:
  GET: "Retrieve data (idempotent, safe)"
  POST: "Create new resource"
  PUT: "Replace entire resource"
  PATCH: "Partial update"
  DELETE: "Remove resource"
  
scoring:
  excellent: "Proper HTTP verbs, 100% consistent"
  good: "90% correct usage"
  attention: "70-90% correct"
  critical: "<70% or major violations"

confidence: "high_92%"
```

### 1. URL Structure & Naming

```yaml
best_practices:
  resource_names: "Plural nouns (/users, /orders)"
  hierarchical: "/users/123/orders/456"
  lowercase: "/api/products (not /api/Products)"
  kebab_case: "/user-profiles (not /user_profiles)"
  no_verbs: "❌ /getUsers, ✅ GET /users"

anti_patterns:
  - "❌ /getUserById?id=123"
  - "✅ GET /users/123"
  - "❌ /createOrder (verb in URL)"
  - "✅ POST /orders"
  - "❌ /API/Users/GetAll" 
  - "✅ GET /api/users"

confidence: "high_95%"
```

**Detection**:
```bash
# Find verb-based endpoints
grep -r "get\|create\|update\|delete" routes/ controllers/
```

### 2. Status Codes

```yaml
correct_usage:
  200_OK: "Successful GET, PUT, PATCH"
  201_Created: "Successful POST (with Location header)"
  204_No_Content: "Successful DELETE"
  400_Bad_Request: "Invalid input (validation errors)"
  401_Unauthorized: "Missing/invalid authentication"
  403_Forbidden: "Authenticated but no permission"
  404_Not_Found: "Resource doesn't exist"
  409_Conflict: "Business rule violation (duplicate)"
  422_Unprocessable: "Semantic errors"
  500_Internal_Error: "Server bug"
  503_Service_Unavailable: "Temporary outage"

common_mistakes:
  - "Returning 200 for errors (with error in body)"
  - "Using 401 for authorization (should be 403)"
  - "Generic 400 for everything"

confidence: "high_90%"
```

### 3. Request/Response Consistency

```yaml
json_standards:
  property_naming: "camelCase (JS/TS) or snake_case (Python)"
  consistency: "One convention throughout API"
  dates: "ISO 8601 (2024-12-15T10:30:00Z)"
  booleans: "true/false (not 1/0 or 'true'/'false')"

response_envelope:
  option_1_no_envelope:  # Preferred for simple APIs
    success: |
      { "id": 1, "name": "John" }
    error: |
      { "error": "Not found", "code": "USER_NOT_FOUND" }
  
  option_2_envelope:  # For complex APIs
    success: |
      { "data": {...}, "meta": {...} }
    error: |
      { "error": {...}, "meta": {...} }

pagination:
  style_1_offset: |
    {
      "data": [...],
      "total": 150,
      "page": 1,
      "pageSize": 20
    }
  
  style_2_cursor: |
    {
      "data": [...],
      "nextCursor": "eyJpZCI6MTIzfQ==",
      "hasMore": true
    }

confidence: "high_88%"
```

### 4. Error Response Format

```yaml
good_error_format:
  structure: |
    {
      "error": {
        "code": "VALIDATION_ERROR",
        "message": "Validation failed",
        "details": [
          {
            "field": "email",
            "message": "Invalid email format"
          }
        ],
        "timestamp": "2024-12-15T10:30:00Z",
        "path": "/api/users",
        "requestId": "abc-123"
      }
    }

bad_formats:
  - "❌ Just a string: 'Error occurred'"
  - "❌ No error codes: { 'message': 'Bad request' }"
  - "❌ No field-level details for validation"

confidence: "high_92%"
```

### 5. Versioning Strategy

```yaml
approaches:
  url_versioning:  # Most common
    example: "/api/v1/users, /api/v2/users"
    pros: "Clear, easy to route"
    cons: "URL duplication"
    
  header_versioning:
    example: "Accept: application/vnd.api+json;version=1"
    pros: "Clean URLs"
    cons: "Less discoverable"
    
  query_param:
    example: "/api/users?version=1"
    pros: "Simple"
    cons: "Considered anti-pattern"

recommendation:
  - URL versioning for public APIs
  - Major versions only (v1, v2, not v1.2.3)
  - Maintain backwards compatibility within major version

confidence: "medium_75%"  # Strategy depends on context
```

---

## Analysis Protocol

### Step 1: Endpoint Discovery (2 min)

```bash
# Find all API routes
grep -r "@Get\|@Post\|@Put\|@Delete" src/
# or
grep -r "app.get\|app.post" routes/
# or
find . -name "*Controller.cs" -exec grep -H "Route\|HttpGet" {} \;
```

### Step 2: Consistency Check (5 min)

```yaml
analyze:
  1. Naming conventions
     - All plural nouns?
     - Consistent case?
     - No verbs in URLs?
  
  2. HTTP methods
     - Proper verb usage?
     - Idempotency respected?
  
  3. Response formats
     - Consistent structure?
     - Same envelope across endpoints?
     - Pagination format consistent?
  
  4. Error handling
     - Proper status codes?
     - Structured error responses?
     - Field-level validation details?
  
  5. Documentation
     - OpenAPI/Swagger present?
     - Request/response examples?
     - Authentication documented?
```

### Step 3: Generate Report

```markdown
# API Design Analysis

## Overall Score: 7/10 🟡

### Summary
- ✅ Good: RESTful structure
- 🟡 Attention: Inconsistent naming (30% violations)
- 🔴 Critical: Poor error responses
- ❌ Missing: API documentation

---

## Findings

### 1. URL Structure: 7/10 🟡

**Issues**:

#### 🔴 Verb-based URLs (8 endpoints)
```csharp
// Bad
[HttpGet("getUserById")]  ❌
[HttpPost("createOrder")]  ❌

// Good
[HttpGet("{id}")]  ✅
[HttpPost]  ✅
```
- Impact: Violates REST conventions
- Effort: 2 hours (refactor 8 endpoints)
- Risk: Breaking change (requires versioning)

#### 🟡 Inconsistent casing
```
/api/Users  ❌ (PascalCase)
/api/orders  ✅ (lowercase)
/api/user-profiles  ✅ (kebab-case)
/api/productCategories  ❌ (camelCase)
```
- Impact: Confusing for API consumers
- Effort: 1 hour
- Risk: Breaking change

**Recommendation**: 
```yaml
standard: "/api/[lowercase-with-hyphens]"
examples:
  - "/api/users"
  - "/api/product-categories"
  - "/api/user-profiles"
```

---

### 2. HTTP Status Codes: 6/10 🟡

#### Issues:

1. **Returning 200 for errors** 🔴
   ```csharp
   // Bad: UserController.cs line 45
   return Ok(new { error = "User not found" });  ❌
   
   // Good
   return NotFound(new { error = "User not found" });  ✅
   ```
   - Found in: 12 endpoints
   - Effort: 3 hours

2. **Missing 201 Created** 🟡
   ```csharp
   // Bad
   [HttpPost]
   public IActionResult CreateUser(UserDto dto) {
       var user = _service.Create(dto);
       return Ok(user);  ❌ Should be 201
   }
   
   // Good
   [HttpPost]
   public IActionResult CreateUser(UserDto dto) {
       var user = _service.Create(dto);
       return CreatedAtAction(
           nameof(GetUser), 
           new { id = user.Id }, 
           user
       );  ✅
   }
   ```

---

### 3. Error Responses: 4/10 🔴

**Current State**: Inconsistent, unhelpful

#### Example 1: Validation Errors
```json
// Current: OrderController.cs
{
  "message": "Bad request"  ❌
}

// Should be:
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Order validation failed",
    "details": [
      { "field": "quantity", "message": "Must be greater than 0" },
      { "field": "productId", "message": "Product does not exist" }
    ]
  }
}  ✅
```

#### Example 2: Not Found
```json
// Current: Generic
{ "error": "Not found" }  ❌

// Better: Specific
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with ID 123 does not exist",
    "timestamp": "2024-12-15T10:30:00Z",
    "path": "/api/users/123"
  }
}  ✅
```

**Recommendation**: Create ErrorResponse DTO
```csharp
public class ErrorResponse {
    public string Code { get; set; }
    public string Message { get; set; }
    public List<FieldError> Details { get; set; }
    public DateTime Timestamp { get; set; }
    public string Path { get; set; }
}

public class FieldError {
    public string Field { get; set; }
    public string Message { get; set; }
}
```
- Effort: 8 hours (standardize all error responses)
- Impact: Much better DX for API consumers

---

### 4. Pagination: 5/10 🟡

**Issues**:

1. **Inconsistent formats** 🟡
   ```csharp
   // Endpoint A
   { "data": [...], "page": 1, "total": 100 }
   
   // Endpoint B  
   { "items": [...], "currentPage": 1, "totalItems": 100 }
   
   // Endpoint C
   [...] // Raw array, no metadata ❌
   ```

2. **No default page size** 🟡
   - Can return 10,000+ items
   - Causes performance issues

**Recommendation**:
```csharp
public class PagedResult<T> {
    public List<T> Data { get; set; }
    public int Page { get; set; }
    public int PageSize { get; set; }
    public int TotalCount { get; set; }
    public int TotalPages => (int)Math.Ceiling(TotalCount / (double)PageSize);
    public bool HasNext => Page < TotalPages;
    public bool HasPrevious => Page > 1;
}

// Usage
[HttpGet]
public async Task<PagedResult<UserDto>> GetUsers(
    [FromQuery] int page = 1,
    [FromQuery] int pageSize = 20  // Default
) {
    if (pageSize > 100) pageSize = 100;  // Max limit
    // ...
}
```

---

### 5. API Documentation: 0/10 ❌

**Status**: No OpenAPI/Swagger setup

**Impact**:
- Developers must read code to understand API
- No request/response examples
- Authentication unclear

**Recommendation**: Add Swashbuckle
```csharp
// Program.cs
builder.Services.AddSwaggerGen(c => {
    c.SwaggerDoc("v1", new OpenApiInfo { 
        Title = "Your API", 
        Version = "v1",
        Description = "API for XYZ system"
    });
    
    // Include XML comments
    var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
    c.IncludeXmlComments(xmlPath);
});

// Controllers: Add XML comments
/// <summary>
/// Creates a new user
/// </summary>
/// <param name="dto">User creation data</param>
/// <returns>Created user with ID</returns>
/// <response code="201">User created successfully</response>
/// <response code="400">Invalid input</response>
[HttpPost]
[ProducesResponseType(typeof(UserDto), 201)]
[ProducesResponseType(typeof(ErrorResponse), 400)]
public async Task<IActionResult> CreateUser([FromBody] CreateUserDto dto) {
    // ...
}
```
- Effort: 6 hours (setup + document 20 endpoints)
- Impact: Much better onboarding for new developers

---

## Prioritized Recommendations

### 🔴 P0 - Critical

1. **Standardize error responses** (8 hours)
   - Create ErrorResponse DTO
   - Update all controllers
   - Add field-level validation details

2. **Fix status code misuse** (3 hours)
   - Return proper codes (201, 404, etc.)
   - Don't return 200 for errors

### 🟡 P1 - High

3. **Add Swagger documentation** (6 hours)
   - Setup Swashbuckle
   - Add XML comments to endpoints
   - Include request/response examples

4. **Standardize pagination** (4 hours)
   - Create PagedResult<T>
   - Add default page size (20)
   - Add max limit (100)

5. **Remove verb-based URLs** (2 hours)
   - Refactor 8 endpoints
   - Version API (v1 → v2) if breaking

### 🟢 P2 - Medium

6. **Consistent URL naming** (1 hour)
   - All lowercase-with-hyphens
   - Update route attributes

---

## Testing Checklist

```yaml
api_contract_tests:
  - [ ] Request validation (400 for invalid input)
  - [ ] Authentication (401 for missing token)
  - [ ] Authorization (403 for no permission)
  - [ ] Not found (404 for missing resource)
  - [ ] Status codes match semantics
  - [ ] Error responses structured
  - [ ] Pagination works (page, pageSize, total)
```

---

## Tools

```yaml
documentation:
  - Swashbuckle (C# .NET)
  - Swagger UI
  - Postman collections
  
validation:
  - FluentValidation (C#)
  - Joi (Node.js)
  
testing:
  - Postman / Insomnia
  - REST Client (VS Code)
  - xUnit integration tests
```

---

**Analysis Complete** | API Design Score: 7/10 | Confidence: High (88%)
