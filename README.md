# a-REST-API-with-Flask
A simple RESTful API built with Flask to manage users with in-memory storage. Supports CRUD operations via JSON endpoints.

# 🧑‍💻 Flask User API

This is a simple RESTful API built with [Flask](https://flask.palletsprojects.com/) for managing users in memory. It's great for learning how APIs work, testing front-end connections, or using as a starter project for more complex applications.

## 🚀 Features

- Create, read, update, and delete (CRUD) users
- Simple in-memory storage (no database)
- JSON-based API responses
- Clean and easy-to-extend structure
- Perfect for beginners learning Flask and REST APIs

## 📚 Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| GET    | `/users`            | List all users           |
| GET    | `/users/<id>`       | Get a single user        |
| POST   | `/users`            | Create a new user        |
| PUT    | `/users/<id>`       | Update an existing user  |
| DELETE | `/users/<id>`       | Delete a user            |

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/a-REST-API-with-Flask.git
cd a-REST-API-with-Flask

Example Usage (with curl)
# Create a user
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"name\":\"Alice\",\"email\":\"alice@example.com\"}"

# Get all users
curl http://127.0.0.1:5000/users
