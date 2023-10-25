# Django User Authentication API

Welcome to the Django User Authentication API project! This API is built using Django and Django Rest Framework, designed for user authentication. It includes Docker and Docker Compose for easy setup and deployment, uses PostgreSQL as the database, and follows Test Driven Development (TDD) practices. Additionally, we've customized the Django base user model to use email as the unique identifier instead of the username.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Linting](#linting)
- [Contact](#contact)

## Getting Started

These instructions will help you set up and run the Django User Authentication API on your local development environment.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.8 or higher
- PostgreSQL

## Project Structure

The project's directory structure is organized as follows:

```
user-authentication/
│
├── .github/
│   ├── workflows/
│   │   ├── checks.yml
├── app/
│   ├── app/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── core/
│   │   ├── management/
│   |   |       ├── Commands/
│   |   |           ├── wait_for_db.py
│   │   ├── migrations/
│   │   ├── tests/
│   |   |       ├── test_admin.py
│   |   |       ├── test_command.py
│   |   |       ├── test_models.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   ├── user/
│   │   ├── migrations/
│   │   ├── tests/
│   |   |       ├── test_user_api.py
│   │   ├── apps.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── .flake8
│   ├── manage.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── requirements.dev.txt

```

- The `app` directory contains the Django app responsible for authentication.
- The `app/app` directory contains the configuration related settings.
- The `Dockerfile` and `docker-compose.yml` files are used for Docker containerization.
- The `requirements.txt` and `requirements.dev.txt` files specify the project's dependencies.

## Installation

 Clone the repository:

   ```bash
   git clone https://github.com/Ravipoo1319/user-authentication.git
   cd user-authentication
   ```

## Running the API

To run the API using Docker Compose, execute the following commands:

```bash
docker-compose build
docker-compose up
```

The API will be available at `http://localhost:8000/api/`.

## API Endpoints

- `docs/`: To explore and test Swagger web interface.
- `user/create/`: Create a new user.
- `user/token/`: Obtain an authentication token (login).
- `user/me/`: Retrieve and update the authenticated user's information.

## API Documentation

API documentation is generated using the drf-spectacular library and is available at `http://localhost:8000/api/docs/`. You can explore and test the API using the Swagger interface provided.

## Testing

Tests are written following Test Driven Development (TDD) techniques and are located in the `api` app. You can run the tests using the following command:

```bash
docker-compose run --rm app sh -c "python manage.py test"
```

## Linting

We use flake8 for code linting. You can check for code formatting issues with the following command:

```bash
docker-compose run --rm app sh -c "flake8"
```

## Contact

If you have any questions or suggestions regarding this project, feel free to contact:

- Ravindra Pawar
- ravindrapawar1315@gmail.com
- Project Repository: [Link to GitHub Repository](https://github.com/Ravipoo1319/user-authentication)

Thank you for checking out this Django User Authentication API! We hope it helps you in your Django development journey.