# AGENTS

This repository contains a simple forms web application built with Flask. It allows users to create forms, add questions, submit answers and view results.

## Structure
- `app.py` - entry point that runs the Flask app.
- `myproject/` - package containing models, routes and Jinja templates.
- `migrations/` - database migration scripts managed by Flask-Migrate.
- `requirements.txt` - Python dependencies.

The app uses SQLite for storage and serves HTML templates from the `myproject/templates` directory.

## How to run
1. Install dependencies with `pip install -r requirements.txt`.
2. Set the working directory to the repository root.
3. Start the server using `python app.py`.
4. Visit `http://localhost:8000` in a browser.

## Guidelines
- Keep templates and static assets under `myproject`.
- Use Alembic/Flask-Migrate for schema changes.
- Provide descriptive commit messages when updating the repository.

