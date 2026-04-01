# greencity5307 - Docker setup

This repository contains the "greencity5307" test automation project, fully containerized with Docker. All tests (Pytest + Behave) and Allure reporting run **inside Docker**, ensuring consistent behavior across machines.

---

## 🐳 Quick start

1. Clone the repository:

```bash
git clone https://github.com/UA-5307-TAQC/greencity5307.git
cd greencity5307
```
Run all tests and generate Allure report with a single command:
```bash
docker-compose up --build
```
This will:

- Build the Docker image
- Install all dependencies
- Run all Pytest and Behave tests
- Save Allure results to a Docker volume (allure-results)

Stop and remove containers:
```bash
docker-compose down
```
📂 Viewing Allure Report

After tests finish, serve the Allure report directly from the volume:
```bash
docker run --rm -v $(pwd)/allure-results:/app/allure-results -p 8080:8080 allure/allure serve /app/allure-results
```

⚙️ Running specific tests

Override the default command to run a specific test suite or file:
```bash
docker-compose run test pytest tests/ui -q
docker-compose run test pytest tests/api/test_example.py -q
docker-compose run test behave tests/bdd/features/ui -q
```
