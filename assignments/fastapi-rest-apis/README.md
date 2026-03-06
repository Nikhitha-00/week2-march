# 🚀 Building REST APIs with FastAPI

## 🎯 Objective
Learn how to design, build, and test RESTful APIs using the FastAPI framework in Python. By the end of this assignment, you will understand the basics of API endpoints, request/response handling, and data validation.

## 📝 Tasks

### 1. Set Up FastAPI Project
- **Description:** Initialize a new FastAPI project and run a basic server.
- **Requirements:**
  - Install FastAPI and Uvicorn
  - Create a main.py file with a simple root endpoint (`/`) that returns a welcome message
  - Run the server locally and verify it works
- **Example:**
  ```bash
  uvicorn main:app --reload
  ```

### 2. Create CRUD Endpoints
- **Description:** Implement RESTful endpoints for a simple resource (e.g., `items`).
- **Requirements:**
  - Implement endpoints: GET `/items`, GET `/items/{item_id}`, POST `/items`, PUT `/items/{item_id}`, DELETE `/items/{item_id}`
  - Use Pydantic models for request/response validation
  - Store items in an in-memory dictionary
- **Example:**
  ```json
  {"id": 1, "name": "Book", "price": 12.99}
  ```

### 3. Add Data Validation and Error Handling
- **Description:** Ensure your API validates input and handles errors gracefully.
- **Requirements:**
  - Validate that item names are not empty and prices are positive
  - Return appropriate HTTP status codes for errors (e.g., 404 for not found)
  - Add error messages in JSON responses
- **Example:**
  ```json
  {"detail": "Item not found"}
  ```

### 4. Test Your API
- **Description:** Write and run tests for your API endpoints.
- **Requirements:**
  - Use HTTP client tools (e.g., curl, httpie, or Python requests) to test all endpoints
  - Document example requests and responses in your README

## ✅ Submission Checklist
- [ ] All endpoints implemented and tested
- [ ] Code is well-organized and commented
- [ ] README includes setup and usage instructions
- [ ] Example requests and responses provided
