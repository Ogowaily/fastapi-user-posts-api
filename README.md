# FastAPI Learning Project 🚀

This project was built as part of my learning journey with **FastAPI**.  
It includes basic implementations of authentication, user management, and posting functionality using Python and the FastAPI framework.

---

## 📁 Project Structure

```bash
app/
│
├── routers/                 # API route handlers
│   ├── auth.py             # Login & Token authentication
│   ├── post.py             # Endpoints related to posts
│   └── user.py             # Endpoints related to user actions
│
├── auth2.py                # Additional authentication logic
├── database.py             # Database connection and setup
├── dependencies.py         # Dependency injection functions
├── generateSecretKey.py    # Script to generate JWT secret key
├── main.py                 # Main entry point of the FastAPI app
├── models.py               # SQLAlchemy ORM models
├── schema.py               # Pydantic models for request/response validation
├── utils.py                # Helper and utility functions
└── __init__.py             # Makes the 'app' directory a Python package



 
````

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **JWT (JSON Web Tokens)**

---

## 🔐 Features

- User registration and login
- JWT-based authentication
- Post creation and management
- Modular structure for scalability

---

## 🧪 How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-learning-project.git
   cd fastapi-learning-project
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

5. Visit the interactive docs at:

   ```
   http://localhost:8000/docs
   ```

---
````
## 🧠 Notes

This project was built purely for practice and educational purposes.
It’s not intended for production use but rather to demonstrate how a FastAPI app is structured.

---
 
