# Django Student Management

A small Django CRUD project with separate normal HTML routes and Django REST Framework APIs. SQLite is configured by default.

## Features

- Student model: name, unique email, age, course, created and updated timestamps.
- HTML CRUD using function-based views at `/` and class-based generic views at `/cbv/`.
- Compact DRF function APIs at `/api/fbv/students/` and `/api/fbv/students/<id>/`.
- A simple `ModelViewSet` with router-generated CRUD at `/api/viewset/students/`.
- Django admin at `/admin/`.

## Setup

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000/. Use `python manage.py createsuperuser` for admin access.

## API examples

```bash
curl http://127.0.0.1:8000/api/fbv/students/
curl -X POST http://127.0.0.1:8000/api/fbv/students/ -H "Content-Type: application/json" -d '{"name":"Asha Rao","email":"asha@example.com","age":20,"course":"Computing"}'
curl http://127.0.0.1:8000/api/viewset/students/
```

The FBV detail route supports GET, PUT, PATCH, DELETE. The ModelViewSet router exposes the standard list, create, retrieve, update, partial update, and delete actions.

## Tests

```bash
python manage.py test
```

Tests cover HTML FBV/CBV listing and CRUD, validation, and both API styles.

## Git history

This repository has chronological development commits: project scaffold, student model and migration, HTML CRUD views, REST APIs, tests, and documentation. Inspect with `git log --oneline --reverse`.
