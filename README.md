
# 🎉 FastAPI CRUD Todo with SQLite

## Overview 📚
This project is a simple FastAPI application that demonstrates CRUD (Create, Read, Update, Delete) operations using an SQLite database. It's perfect for beginners who want to learn how to build web APIs with FastAPI, Python, and SQLAlchemy.

## Features 🔑
- **CRUD Operations**: Easily create, read, update, and delete Todo items using FastAPI endpoints.
- **SQLite Database**: Lightweight and easy-to-set-up database solution.
- **Interactive API Documentation**: Automatically generated with FastAPI and accessible via `/docs`.
- **Modular Structure**: Clean and modular project structure using routers, models, and schemas.

## Requirements 📋
- **Python 3.7+**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **Pydantic**

## Installation 📝

1. **Clone the repository**:
    ```bash
    git clone https://github.com/lymanny/FastAPI-CRUD-Todo.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd FastAPI-CRUD-Todo
    ```

## Create a Virtual Environment & Activate It 💻

Before running the project, it's best to use a virtual environment to manage dependencies.

1. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

2. **Activate the virtual environment**:

   - On **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

   - On **Windows**:
     ```bash
     .\env\Scripts\activate
     ```

3. **Install the project dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage 🚀
1. Start the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

### API Documentation Screenshot
Here’s an example of the interactive documentation generated by FastAPI:

<img src="https://github.com/user-attachments/assets/473c6d0f-c400-4630-8c3d-c7daa442fdec" alt="FastAPI Documentation"/>
   
## Project Structure 📂
```
FastAPI-CRUD-Todo/
├── database.py              # Database setup and connection
├── models.py                # SQLAlchemy models
├── schemas.py               # Pydantic schemas for validation
├── routers/
│   └── todo.py              # API endpoints for CRUD operations
├── main.py                  # Entry point for the FastAPI app
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
```

## Contributing 🤝
Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

## License 📄
This project is licensed under the [MIT License](LICENSE).

## Author 👩‍💻
lymanny - iOS Developer  
🌐 [Portfolio](https://lymanny.onrender.com)
