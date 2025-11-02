# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Setup and Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Initialize or upgrade database
flask db upgrade

# Run development server
python app.py
```

### Database Migrations
```bash
# Create a new migration after model changes
flask db migrate -m "Description of schema changes"

# Apply pending migrations
flask db upgrade

# Rollback last migration
flask db downgrade
```

## Project Architecture

### Core Components
- **Web Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Templating**: Jinja2
- **Frontend**: Bootstrap 5.3.2, Chart.js

### Key Architectural Patterns
- Cascading database relationships with automatic orphan deletion
- Lazy dynamic query loading
- Email-based response tracking
- Dynamic form and question creation

### Database Schema
- **Forms**: Root entity for survey/questionnaire
- **Questions**: Associated with Forms, support text and multiple-choice types
- **Options**: Linked to multiple-choice Questions
- **Answers**: Responses to Questions, tracked by email

### Routing Strategy
- RESTful routes in `myproject/__init__.py`
- CRUD operations for Forms, Questions, and Responses
- Export functionality for form results

## Security Considerations
- No built-in authentication
- Email used as sole identifier
- No CSRF protection (recommend adding Flask-WTF)
- Robots.txt restricts crawling of sensitive routes

## Testing and Debugging
```bash
# TODO: Add specific testing commands once test suite is established
# Example placeholder:
# python -m pytest tests/
```

## Performance Notes
- In-memory Excel export using BytesIO
- Chart.js for client-side result visualization
- Lazy loading of database relationships

## Deployment Recommendations
- Use production WSGI server (Gunicorn, uWSGI)
- Configure proper environment variables
- Implement authentication for production
- Add CSRF protection