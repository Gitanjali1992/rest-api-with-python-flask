# REST APIs with Flask and Python

<p align = "center">💡 A full project to use Flask and Python to make REST APIs using multiple Flask extensions and PostgreSQL.</p>

## Highlighters: Things achieved in this project

1. **Docker** used to run the REST API.

2. Used the **Flask-Smorest** extension, a library that greatly simplifies writing REST APIs using Flask. 
    - Also automated **Swagger** documentation generation.

3. Data storage achieved with **SQLAlchemy**, an ORM (Object-Relational Mapping which simplifies connecting to and interacting with a database. 

4. Implemented many-to-many relationships using **SQLAlchemy**.

5. Performed user authentication using JWTs and the **Flask-JWT-Extended** library. Used access token JWTs, as well as refresh tokens, JWT claims, blocklists, password hashing, and more.

6. After deploying your apps, making changes to the database can be really tricky because you have to log in to the database server and manually update the database tables using SQL commands. **Flask-Migrate** and the **Alembic** libraries used for creating migration scripts.

7. Used **Render.com** for deployments and also deployed a **PostgreSQL** database.

8. Using **gunicorn** to deploy app on **Render.com** for performance reasons