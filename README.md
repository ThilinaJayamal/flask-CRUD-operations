# 🐍 Simple REST API Using Flask

A simple, RESTful API built with **Flask**, **Flask-RESTful**, and **SQLAlchemy** to manage users. Easily create, read, update, and delete users in a SQLite database.

## 📌 Features

* ✅ Create new users with name and email
* 🔍 Retrieve all users or a single user by ID
* ✏️ Update user information
* 🗑️ Delete users
* 💾 Persist data with a SQLite database
* ⚡ Input validation with Flask-RESTful reqparse
* 📦 JSON responses using marshal_with

## 🛠️ Tech Stack

* **Backend**: Python, Flask, Flask-RESTful
* **Database & ORM**: SQLite, SQLAlchemy
* **API Design**: RESTful

## 🧪 Getting Started (Development)

### Prerequisites

* Python 3.7 or higher
* pip (Python package installer)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/ThilinaJayamal/flask-CRUD-operations.git
cd flask-CRUD-operations
```

2. **Create a virtual environment (optional but recommended):**

```bash
# For Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

# For Windows (Command Prompt)
py -m venv .venv
.venv\Scripts\activate

# For Windows (Git Bash)
py -m venv .venv
source .venv/Scripts/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Initialize the database:**

```bash
python create_db.py
```

5. **Run the application:**

```bash
python api.py
```

6. **Access the API:**

Open your browser or API client to access the API at:
```
http://127.0.0.1:5000/
```

## 🗂️ API Endpoints

### Get all users
```http
GET /api/users/
```

**Response:**
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }
]
```

### Get user by ID
```http
GET /api/users/<id>
```

**Response:**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
}
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

**Response:**
```json
{
    "id": 1,
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

**Response:**
```json
{
    "id": 1,
    "name": "Jane Doe",
    "email": "jane@example.com"
}
```

### Delete user
```http
DELETE /api/users/<id>
```

**Response:**
```json
{
    "message": "User deleted successfully"
}
```

## 🗃️ Database Schema

### UserModel

| Field | Type    | Constraints        |
|-------|---------|-------------------|
| id    | Integer | Primary Key       |
| name  | String  | Not Null          |
| email | String  | Unique, Not Null  |

## 📁 Project Structure

```
flask-CRUD-operations/
├── api.py              # Main Flask application
├── create_db.py        # Database initialization script
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── instance/
    └── database.db    # SQLite database file (created after running)
```

## 📦 Requirements

```
Flask==3.0.0
Flask-RESTful==1.0.0
Flask-SQLAlchemy==3.0.0
```

## 🧪 Testing the API

You can test the API endpoints using various tools:

### Using curl

```bash
# Get all users
curl -X GET http://127.0.0.1:5000/api/users/

# Create a new user
curl -X POST http://127.0.0.1:5000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Get user by ID
curl -X GET http://127.0.0.1:5000/api/users/1

# Update user
curl -X PATCH http://127.0.0.1:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "email": "jane@example.com"}'

# Delete user
curl -X DELETE http://127.0.0.1:5000/api/users/1
```

### Using Postman

1. Import the collection or manually create requests
2. Set the base URL to `http://127.0.0.1:5000`
3. Add the appropriate headers and request bodies as shown above

## 🔧 Configuration

The application uses the following default configuration:

* **Database**: SQLite (`instance/database.db`)
* **Host**: 127.0.0.1
* **Port**: 5000
* **Debug Mode**: Enabled (for development)

To modify these settings, update the configuration in `api.py`.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 📧 Contact

**Thilina Jayamal** - [GitHub](https://github.com/ThilinaJayamal)

Project Link: [https://github.com/ThilinaJayamal/flask-CRUD-operations](https://github.com/ThilinaJayamal/flask-CRUD-operations)

## 🙏 Acknowledgments

* Flask documentation
* Flask-RESTful documentation
* SQLAlchemy documentation