# **Tuko App Clone** - *Backend*

## Description

- This project aims to clone the [Tuko](https://tuko.co.ke/) news app.

- It is a simple CRUD API built with Django and Django Rest Framework. Users can read articles. However, only authenticated users can create, update and delete them.

---

## Setup/Installation Instructions

1. Clone the repository

2. Install the project requirements using the command below:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file at the root of the project and add the following configurations:

    ```bash
    SECRET_KEY='<your_secret_key>'
    DEBUG=True
    ```

4. Run the migrations using the following commands:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser account using the command below: (follow the prompts)

    ```bash
    python manage.py createsuperuser
    ```

6. Run the server using the command below:

    ```bash
    python manage.py runserver
    ```

7. Open the browser and navigate to [`localhost:8000/admin`](localhost:8000/admin) to access the admin site (login with your superuser credentials) and [`localhost:8000/api/`](localhost:8000/api/) to access the API endpoints on the browsable API.

8. On the browsable API, users can read the posts and authenticated users can create, update and delete posts.
