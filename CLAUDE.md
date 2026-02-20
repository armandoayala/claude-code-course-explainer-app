# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the app:**
```bash
python src/app.py
```
Starts the Flask dev server at `http://127.0.0.1:5000`.

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run all tests:**
```bash
python -m unittest discover -s tests
```

**Run a single test:**
```bash
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

Flask app with a simple MVC-style structure under `src/`:

- **app.py** — Creates the Flask app, registers routes (`/` and `/course/<course_id>`), and runs the dev server.
- **models.py** — Defines the `Course` dataclass and holds hardcoded sample course data (no database).
- **views.py** — Route handler functions (`index`, `course`) that render Jinja2 templates.
- **templates/** — Jinja2 templates using `layout.html` as the base via `{% extends %}`.
- **static/css/styles.css** — All styling; no build step required.

Tests in `tests/test_app.py` use Flask's built-in test client for integration-style tests against the running app routes.

## Add Unit tests
- Whenever you add any changes add unit tests and run and make sure the tests passes. 