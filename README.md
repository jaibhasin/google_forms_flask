# Gougon Forms Flask

This project contains a lightweight form builder written with [Flask](https://flask.palletsprojects.com/). It allows you to create simple web forms, collect responses and review submissions. Data is stored locally in SQLite and the user interface uses Bootstrap for styling.

## Features

- Create forms with a title
- Add text or multiple choice questions to each form
- Mark questions as required or optional
- Fill out forms and store responses with an email address
- View aggregated results including pie charts for choice questions
- Export responses to an Excel file

## Project layout

```
├── app.py                 # Entry point running the Flask application
├── myproject/             # Package with application code
│   ├── __init__.py        # Routes and application configuration
│   ├── models.py          # SQLAlchemy models
│   └── templates/         # Jinja templates for the UI
├── migrations/            # Alembic database migration scripts
├── requirements.txt       # Python dependencies
└── robots.txt             # Robots policy for crawlers
```

## Installation

1. Ensure Python 3.8 or later is installed.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

The application uses SQLite by default so no additional database setup is required.

## Running the server

From the repository root run:

```bash
python app.py
```

The server listens on `http://localhost:8000`. Visit that URL in your browser to access the home page and start creating forms.

## Database migrations

Schema changes are managed with [Flask-Migrate](https://flask-migrate.readthedocs.io/). Migration scripts live in the `migrations/` directory. Typical commands are:

```bash
flask db migrate -m "description"
flask db upgrade
```

## Exporting responses

Results for each form can be downloaded as an Excel workbook by visiting `/form/<id>/export` in your browser. The exported file contains one sheet with emails and answers for each question.

## Development notes

- HTML templates and static assets live under `myproject/templates`.
- See `robots.txt` for paths that are disallowed to crawlers.
- Descriptive commit messages help track changes when updating this repository.

## License

This project is provided as-is under the MIT License.
