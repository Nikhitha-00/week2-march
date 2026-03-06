# 🚀 Building REST APIs with FastAPI

## 🎯 Objective
Learn how to design and implement RESTful APIs using the FastAPI framework in Python. By the end of this assignment, you will understand the basics of FastAPI, how to define endpoints, handle requests, and return responses in a modern web API.

## 📝 Tasks

### 1. Set Up FastAPI Project
**Description:**
- Initialize a new Python project and install FastAPI and Uvicorn.

**Requirements:**
- Create a virtual environment
- Install FastAPI and Uvicorn
- Create a main.py file with a basic FastAPI app

```python
# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

### 2. Create API Endpoints
**Description:**
- Add endpoints for basic CRUD operations on a resource (e.g., items).

**Requirements:**
- Implement GET, POST, PUT, DELETE endpoints for `/items`
- Use Pydantic models for request/response validation
- Return appropriate status codes and JSON responses

### 3. Test Your API
**Description:**
- Run your FastAPI app locally and test endpoints using a tool like curl or Postman.

**Requirements:**
- Start the server with Uvicorn
- Test all endpoints for correct behavior
- Document example requests and responses in your README

---

**Example:**

```bash
uvicorn main:app --reload
```

```bash
curl http://127.0.0.1:8000/items
```

