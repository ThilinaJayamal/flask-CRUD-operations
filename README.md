````markdown
# 🐍 Simple REST API Using Flask

A simple, RESTful API built with **Flask**, **Flask-RESTful**, and **SQLAlchemy** to manage users. Easily create, read, update, and delete users in a SQLite database.

---

## 📌 Features

- ✅ Create new users with name and email
- 🔍 Retrieve all users or a single user by ID
- ✏️ Update user information
- 🗑️ Delete users
- 💾 Persist data with SQLite database
- ⚡ Input validation with Flask-RESTful reqparse
- 📦 JSON responses using marshal_with

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask, Flask-RESTful
* **Database & ORM**: SQLite, SQLAlchemy
* **API Design**: RESTful
* **Testing Tools**: Postman


## 🧪 Getting Started (Development)

1. Clone the repository:

```bash
git clone https://github.com/ThilinaJayamal/flask-CRUD-operations.git
cd flask-CRUD-operations
```

2. Create a virtual environment (optional but recommended):

```bash
py -m venv .venv
source .venv/bin/activate   # Linux/Mac
source .venv\Scripts\activate      # Windows (Use Git Bash)
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
py create_db.py
```

```bash
py api.py
```

5. Open your browser or API client to access the API at:

```
http://127.0.0.1:5000/
```

---

## 🗂️ API Endpoints

### Get all users

```http
GET /api/users/
```

### Get user by ID

```http
GET /api/users/<id>
```

### Create a new user

```http
POST /api/users/
```

**Request Body:**

```json
{
    "name": "John Doe",
    "email": "john@example.com"
}
```

### Update user

```http
PATCH /api/users/<id>
```

**Request Body:**

```json
{
    "name": "Jane Doe",
    "email": "jane@example.com"
}
```

### Delete user

```http
DELETE /api/users/<id>
```

---

## 🗃️ Database Schema

**UserModel**:

| Field | Type    | Constraints      |
| ----- | ------- | ---------------- |
| id    | Integer | Primary Key      |
| name  | String  | Not Null         |
| email | String  | Unique, Not Null |

---

## 📦 Requirements

```
Flask==3.0.0
Flask-RESTful==1.0.0
Flask-SQLAlchemy==3.0.0
```

---

## ⚡ License

This project is licensed under the MIT License.

```