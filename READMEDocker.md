# Docker Setup for greencity5307 Test Automation

This document describes how to run the **pytest-based UI & API test framework** for the `greencity5307` project inside a Docker container.

The goal is to ensure tests run in a **fully reproducible, isolated environment**, independent of the local machine.

---

## What is included

* Containerized test execution using Docker
* Automatic dependency installation
* Pytest test execution inside container
* Optional Allure reporting support
* No local Python environment required

---

## Prerequisites

Make sure you have installed:

* Docker
* Docker Compose

---

## Quick Start

Run the following command in the project root:

```bash
docker-compose up --build
```

---

## What happens during startup

1. Docker builds an image based on Python
2. Installs dependencies from `requirements.txt`
3. Copies the project into the container
4. Runs all tests using pytest
5. Outputs logs directly to the console

---

## Running Tests

By default, all tests are executed:

```bash
pytest -v
```

To customize test execution, edit the `command` section in `docker-compose.yml`.

Examples:

Run only UI tests:

```yaml
command: pytest tests/ui -v
```

Run a specific test:

```yaml
command: pytest tests/ui/test_example.py::test_name -v
```

---

## Allure Reporting (Optional)

To enable Allure results, tests are executed with:

```bash
pytest --alluredir=allure-results
```

Results will be stored in:

```
allure-results/
```

To generate and view the report locally (requires Allure CLI):

```bash
allure serve allure-results
```

---

## 📁 Project Structure (Relevant for Docker)

```
.
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
├── tests/
├── pages/
├── components/
├── services/
├── utils/
└── data/
```

---

## Configuration

### Environment Variables

You can pass environment variables via:

* `.env` file
* `docker-compose.yml`

Example:

```yaml
environment:
  - BASE_URL=https://example.com
```

---

## Volumes

The following volumes are used:

* Project files mounted into container
* Allure results persisted locally

Example:

```yaml
volumes:
  - .:/app
  - ./allure-results:/app/allure-results
```

---

## Requirements Covered

✔ Tests run inside container
✔ No manual setup required
✔ Logs visible in console
✔ Works on any machine with Docker
✔ No dependency on local Python environment

---

## Troubleshooting

### Tests fail due to missing dependencies

➡ Ensure `requirements.txt` is complete

### Changes not applied

➡ Rebuild container:

```bash
docker-compose up --build
```

### Permission issues (Linux/Mac)

➡ Try:

```bash
sudo docker-compose up --build
```

---

## Possible Improvements

* Multi-stage Docker build for smaller image
* Parallel test execution (`pytest-xdist`)
* Allure report auto-generation in container
* CI/CD integration (GitHub Actions)
* Service containers (API, database)

---

## Summary

This Docker setup allows you to:

* Run tests consistently across environments
* Eliminate "works on my machine" issues
* Simplify onboarding and CI integration

---
