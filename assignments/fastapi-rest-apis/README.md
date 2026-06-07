# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. In this assignment, you will create endpoints, validate request data, and return useful HTTP responses for common CRUD operations.

## 📝 Tasks

### 🛠️ Build the FastAPI App and First Endpoint

#### Description
Set up a FastAPI application and create a basic health-check route so you can verify the server is running correctly.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app in `starter-code.py`.
- Create a `GET /health` endpoint that returns JSON like `{ "status": "ok" }`.
- Run successfully with `uvicorn starter-code:app --reload`.


### 🛠️ Create Item Endpoints with Validation

#### Description
Add endpoints for creating and listing items. Use a Pydantic model to validate incoming data for new items.

#### Requirements
Completed program should:

- Define an `Item` model with `id`, `name`, and `price` fields.
- Create a `POST /items` endpoint that accepts JSON and stores a new item in memory.
- Create a `GET /items` endpoint that returns all stored items as JSON.
- Return status code `201` when a new item is created.


### 🛠️ Add Read, Update, and Delete by ID

#### Description
Complete the API by handling single-item operations and correct error responses when an item is not found.

#### Requirements
Completed program should:

- Create a `GET /items/{item_id}` endpoint to return one item.
- Create a `PUT /items/{item_id}` endpoint to update an existing item.
- Create a `DELETE /items/{item_id}` endpoint to remove an item.
- Return status code `404` with a clear message when `item_id` does not exist.
