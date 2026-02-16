# greencity5307

A lightweight pytest-based test automation scaffold for the "greencity5307" project. This repository contains a small, opinionated test framework organized around page/components/services abstractions and utilities for running API and UI tests with pytest.

### 🔗 Main branch report
The current report for the main branch is available at the following link:

[![Allure Report](https://img.shields.io/badge/Allure%20Report-main-blue)](https://ua-5307-taqc.github.io/greencity5307)


In the report, you can find:
- ✅ results of all tests
- 📈 history and trends
- 🔁 flaky and retried tests
- ⏱️ execution duration
- 📊 test case statistics

### Contents

- Project description
- Quick start (setup & run)
- Test and reporting workflows
- Linting and pre-commit hooks
- Repository structure
- Notes & next steps

Project goals

- Provide a reproducible pytest test scaffolding for UI and API tests.
- Use webdriver-manager for browser drivers and `requests` for API calls.
- Integrate with Allure for test reporting.
- Provide linting and CI checks to keep code quality consistent.

Prerequisites

- Python 3.10+ (3.12 recommended)
- Git
- (Optional) Allure CLI for serving reports locally

Dependencies

All project Python dependencies are listed in `requirements.txt`. Install them into a virtual environment (recommended). The requirements include development tools such as `pylint` and `pre-commit`.

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

Linting and pre-commit hooks

This repository includes:
- `.pylintrc` — basic pylint configuration
- `.pre-commit-config.yaml` — pre-commit configuration to run formatting and lint checks on commit
- A GitHub Actions workflow at `.github/workflows/ci.yml` that runs linting and pytest on pull requests

Set up pre-commit locally (one-time):

```powershell
pre-commit install
```

Run pre-commit checks on all files (useful before pushing):
```powershell
pre-commit run --all-files
```

Run pylint locally:

```powershell
pylint .
```

GitHub pull request checks

A workflow `ci.yaml` runs on pull requests to:
- install dependencies
- run `pylint` across the repository (results will be reported in the job log)
- run `pytest` to execute tests

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
- `requirements.txt` - Pinned Python dependencies (includes dev tools).
- `pytest.ini` - Pytest configuration.
- `.pylintrc` - Pylint configuration.
- `.pre-commit-config.yaml` - Pre-commit config.
- `.github/workflows/ci.yml` - GitHub Actions PR checks.

Contributing

- Open an issue to discuss new features or bugs.
- Create feature branches and submit pull requests against `main`.
- Keep tests green and add unit/integration tests for new behavior.

Notes & next steps (suggested improvements)

- Add a `README`-level example test demonstrating both API and UI flows.
- Add CI workflow enhancements: cache pip dependencies, upload Allure artifacts, and annotate pylint failures.
- Add a basic `conftest.py` fixture set for browser/session management and for API client setup.
- Add a `Makefile` or `invoke` tasks to simplify common commands.

License

No license specified. Add a license file (e.g., MIT) if you intend to make this project public.
