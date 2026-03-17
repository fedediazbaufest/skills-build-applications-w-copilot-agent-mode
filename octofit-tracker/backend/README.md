# OctoFit Tracker Backend

Django REST API backend for the OctoFit Tracker application.

## Setup

### 1. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Navigate to Project Directory
```bash
cd octofit_tracker
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

## Running the Server

### Start Development Server
```bash
cd octofit_tracker
python manage.py runserver 0.0.0.0:8000
```

The API will be accessible at:
- Local: http://localhost:8000
- GitHub Codespace: https://{CODESPACE_NAME}-8000.app.github.dev
- Admin: http://localhost:8000/admin/
- API Root: http://localhost:8000/api/

## Admin Credentials
- **Username**: admin
- **Email**: admin@octofit.local
- **Password**: Set when running `createsuperuser`

## Available Endpoints

### Admin
- `GET/POST /admin/` - Django admin interface

### API
- `GET /api/` - API root endpoint with available endpoints documentation

## Project Structure

```
octofit_tracker/
├── config/           # Project settings and configuration
│   ├── settings.py   # Django settings
│   ├── urls.py       # URL routing
│   ├── wsgi.py       # WSGI application
│   └── asgi.py       # ASGI application
├── api/              # Main API application
│   ├── models.py     # Data models
│   ├── serializers.py # API serializers
│   ├── views.py      # API views
│   ├── urls.py       # API URL routing
│   └── admin.py      # Admin configuration
├── manage.py         # Django management script
└── db.sqlite3        # SQLite database (development)
```

## Technologies Used

- Django 4.1.7
- Django REST Framework 3.14.0
- django-cors-headers 4.5.0
- dj-rest-auth 2.2.6
- django-allauth 0.51.0
- djongo 1.3.6 (MongoDB support)
- pymongo 3.12

## Features

- User authentication and profiles (via django-allauth)
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions
- MongoDB support (via djongo)
- REST API with browsable interface

## Notes

- The database defaults to SQLite for development. To use MongoDB, update `DATABASES` in `settings.py`.
- CORS is configured to allow requests from localhost and Codespace domains.
- The API uses Django REST Framework's DefaultRouter for automatic URL generation.
