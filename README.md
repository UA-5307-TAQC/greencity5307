# greencity5307

A lightweight pytest-based test automation scaffold for the "greencity5307" project. This repository contains a small, opinionated test framework organized around page/components/services abstractions and utilities for running API and UI tests with pytest.

Contents

- Project description
- Quick start (setup & run)
- Test and reporting workflows
- Repository structure
- Notes & next steps

Project goals

- Provide a reproducible pytest test scaffolding for UI and API tests.
- Use webdriver-manager for browser drivers and `requests` for API calls.
- Integrate with Allure for test reporting.

Prerequisites

- Python 3.10+ (3.12 recommended)
- Git (optional)
- (Optional) Allure CLI for serving reports locally

Dependencies

All project Python dependencies are listed in `requirements.txt`. Install them into a virtual environment (recommended).

Quick start (Windows PowerShell)

1. Create and activate a virtual environment

   ```powershell
   python -m venv .venv
   ```
   ```powershell
   .\.venv\Scripts\Activate
   ```

2. Install dependencies

   ```powershell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Run the test suite

   Run all tests:

   ```powershell
   pytest -q
   ```

   Run tests in a specific folder (example: UI tests):

   ```powershell
   pytest tests/ui -q
   ```

   Run a single test file or test function:

   ```powershell
   pytest tests/ui/test_example.py::test_name -q
   ```

Allure reporting (optional)

Generate an Allure result directory and serve the report (requires Allure CLI installed separately):

```powershell
pytest --alluredir=reports/allure
allure serve reports/allure
```

If you don't have Allure CLI installed, you can install it by following instructions at https://docs.qameta.io/allure/

Environment variables and configuration

- This project uses `python-dotenv` (if you place a `.env` file) or other config modules under `data/config.py` to provide environment-specific values such as base URLs or credentials.
- Before running tests, ensure any required environment variables are set (or add them to a `.env` file).

Repository layout

- `components/` - Reusable UI components (buttons, inputs, widgets).
- `pages/` - Page object models that compose components to represent application pages.
- `services/` - API client wrappers and backend service helpers.
- `data/` - Test data, configuration helpers (e.g. `config.py`).
- `utils/` - Utility modules (logging, helpers).
- `tests/` - Test suites organized by `api/` and `ui/` subfolders.
- `requirements.txt` - Pinned Python dependencies.
- `pytest.ini` - Pytest configuration.

Contributing

- Open an issue to discuss new features or bugs.
- Create feature branches and submit pull requests against `main`.
- Keep tests green and add unit/integration tests for new behavior.
