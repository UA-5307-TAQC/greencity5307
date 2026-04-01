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
