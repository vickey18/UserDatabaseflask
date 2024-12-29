# User Database Flask Application

This repository contains a Flask application to manage user data, including their ID, name, email, and roll number. The app is connected to a MySQL database and provides functionality for adding, retrieving, and displaying user data.

## Home Page
![image alt](https://github.com/vickey18/User-Database-flask/blob/7de4c6590517772e5f5f5ecaa49731c633055477/homepage.PNG)

## Users Page
![image alt](
https://github.com/vickey18/User-Database-flask/blob/62b486674a0f385fde3cb34acda14daddbb1937a/all_users.PNG)

## New User Page
![image alt](https://github.com/vickey18/User-Database-flask/blob/0ab5b8f7fe2c30064ad1831b740b7e4a0841d3c3/new_user.PNG)


## Specific user Page
![image alt](https://github.com/vickey18/User-Database-flask/blob/ae23e90d2a4107252a324c2030d215687193e03d/specific_user.PNG)



---

## Table of Contents
1. [Setup Instructions](#setup-instructions)  
2. [Database Schema](#database-schema)  
3. [Populating Sample Data](#populating-sample-data)  
4. [Dependencies](#dependencies)  
5. [Git Workflow](#git-workflow)  
6. [Contributing](#contributing)  

---

## Setup Instructions

### Prerequisites:
- **Python 3.10 or later**
- **MySQL database**
- **Git installed** on your system

### Steps to Set Up the Project:
1. Clone the repository:
   ```bash
   git clone https://github.com/vickey18/User-Database-flask.git
   cd User-Database-flask
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the MySQL database:
   - Create a MySQL database named `users`.
   - Update the `app.py` file with your database credentials:
     ```python
     app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://<username>:<password>@localhost/users"
     ```
   - Replace `<username>` and `<password>` with your MySQL credentials.

5. Initialize the database:
   ```bash
   flask shell
   
   >>> from app import db, app
   >>> with app.app_context():
        db.create_all()
   ```

6. Run the Flask application:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://127.0.0.1:8000`.

---

## Database Schema

The application uses the following schema:

| Field   | Type          | Attributes          |
|---------|---------------|---------------------|
| `id`    | Integer       | Primary Key         |
| `name`  | String (200)  | Not Null            |
| `email` | String (500)  | Not Null            |
| `roll`  | String (500)  | Not Null            |

---
# Database Operations using SQLAlchemy

## Insert a User
```bash
from app import db, Users

# Create a new user
new_user = Users(id=1, name="John Doe", email="john.doe@example.com", roll="12345")

# Add the user to the session and commit to the database
db.session.add(new_user)
db.session.commit()
```

## Retrieve All Users
To retrieve all users from the Users table, use:
```bash
# Query all users from the Users table
all_users = Users.query.all()
```


## Retrieve a User by ID
```
To retrieve a user by their unique ID, you can either use get() or filter_by() method:

# Retrieve a user by ID using get()
user = Users.query.get(user_id)

# Or using filter_by() to get the first match
user = Users.query.filter_by(id=user_id).first()

```

## Populating Sample Data

To add sample data:
1. Run the `/hello` route in the browser (`http://127.0.0.1:5000/hello`) or modify the route to include your sample data:
   ```python
   user = Users(id=1, name="John Doe", email="john@example.com", roll="A123")
   db.session.add(user)
   db.session.commit()
   ```

2. You can also add users using the "Add New User" form in the app.

---

## Dependencies

The project uses the following Python packages:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PyMySQL
- Bootstrap 5 (for frontend styling)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Git Workflow

### Branching:
- The main branch is `main`.
- For new features or bug fixes, create a new branch:
  ```bash
  git checkout -b feature/branch-name
  ```

### Commiting Changes:
- Ensure changes are tested before committing.
- Write meaningful commit messages:
  ```bash
  git commit -m "Add feature X"
  ```

### Pushing Changes:
- Push changes to your branch:
  ```bash
  git push origin feature/branch-name
  ```

### Creating Pull Requests:
- Open a pull request on GitHub to merge your branch into `main`.

---

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch with your changes.
3. Submit a pull request with a clear description of your changes.

For significant contributions, please discuss them via issues before starting work.

---

Feel free to reach out if you encounter any issues!
