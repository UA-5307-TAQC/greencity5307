# 🧠 TAQC Playbook – GreenCity 5307

This playbook defines **Test Automation & Quality Control (TAQC) standards** for the GreenCity 5307 project. It aligns with **ISTQB**, **SoftServe QA practices**, and an **automation-first mindset** using **Selenium + API testing** with **Allure reporting**.

---

## 🎯 Goals

* Ensure predictable, measurable quality
* Enforce automation as a quality gate
* Reduce flaky tests and MTTR
* Maintain full traceability: **Requirement → Test → Bug → Report**

---

## 🧪 Automation Stack

### UI Testing

* **Tool**: Selenium WebDriver
* **Language**: Python 3.10+
* **Test Framework**: pytest
* **Driver Management**: `webdriver-manager`
* **Pattern**: Page Object Model (POM)
* **Waits**: Explicit waits only

### API Testing

* **Tool**: `requests` (Python HTTP client for API testing)
* Contract-first mindset (request/response validation)

### Reporting

* **Allure Report** (single source of truth)

---

## 📊 Quality Metrics

### 1. Test Coverage

* Functional coverage per feature
* Reported in Allure as labels:

  * `feature`
  * `story`
  * `epic`

**Target:** ≥ 70% for critical flows

---

### 2. Flakiness Rate

**Definition:**

```
Flakiness (%) = (Unstable test runs / Total runs) * 100
```

**Quality Gate:**

* ⚠ Warning: > 5%
* ❌ Fail CI: > 10%

Flaky tests must be:

* Marked with `@pytest.mark.flaky` (requires `pytest-flaky` plugin)
* Linked to a BUG issue

---

### 3. MTTR (Mean Time To Repair)

**Definition:**
Time between defect detection and fix merged.

**Target:**

* Critical bugs: < 24h
* Major bugs: < 72h

---

## 📈 Quality Gates (CI)

CI pipeline **fails** if:

* ❌ Any **Critical** test fails
* ❌ Flakiness > **10%**
* ❌ No tests executed for changed feature

CI pipeline **warns** if:

* ⚠ Coverage decrease > 5%
* ⚠ New tests marked `@Flaky`

---

## 🤖 Allure Mapping Standards

### Labels (Mandatory)

```python
import allure


@allure.epic("GreenCity")
@allure.feature("Authentication")
@allure.story("User Login")
def test_user_login():
    ...
```

---

## 🐞 Bug → Allure → GitHub Mapping

| Source     | Mapping               |
| ---------- | --------------------- |
| GitHub Bug | Allure `@Link(issue)` |
| Test Case  | Allure `@Story`       |
| Feature    | Allure `@Feature`     |
| CI Job     | Allure Launch         |

---

## 🔁 Auto-Labeling Rules (GitHub)

| Condition           | Auto Label       |
| ------------------- | ---------------- |
| Selenium selected   | `ui-tests`       |
| API selected        | `api-tests`      |
| Flakiness > 5%      | `flaky`          |
| Severity = Critical | `critical`       |
| Automation missing  | `automation-gap` |

---

## 🧪 Test Case Rules (ISTQB)

Every automated test MUST:

* Have a clear objective
* Be deterministic
* Be isolated
* Have Allure metadata
* Be traceable to requirement

---

## 🚫 Anti-Patterns

❌ Fixed sleep/wait statements (e.g., time.sleep)
❌ Hardcoded test data
❌ Multiple assertions without context
❌ UI tests for API logic

---

## ✅ Definition of Done (TAQC)

A feature is DONE only if:

* Automated tests exist
* Tests are green in CI
* Allure report is generated
* No critical quality risks remain

---

**Owner:** TAQC Team
**Project:** GreenCity 5307
