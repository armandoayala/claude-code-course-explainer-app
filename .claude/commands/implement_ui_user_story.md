# Custom command: /implement_ui_user_story

Implement a UI user story end-to-end for this Flask course-explainer app by running three agents in sequence.

## User Story

$ARGUMENTS

## Steps

### Step 1 — UX Design
Use the `ux-design-planner` agent to translate the user story above into a structured UX design spec:
- Page layout and component list
- Interaction flow and states
- Data requirements
- Hand-off checklist for the coding agent

### Step 2 — Implementation
Use the `general-purpose` agent to implement the design spec produced in Step 1:
- Follow the existing Flask MVC structure (app.py, models.py, views.py, templates/, static/css/styles.css)
- Add or update routes, models, templates, and CSS as needed
- Write unit tests in tests/test_app.py and confirm they pass

### Step 3 — Visual Verification
Use the `flask-feature-verifier` agent to start the Flask app, navigate to the new feature, take a screenshot, and confirm it renders correctly.
