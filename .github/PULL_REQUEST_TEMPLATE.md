# Pull Request

## Summary
Briefly describe the change and why it was made.
- What: (short description)
- Why: (context / motivation / related issue)

## Link to issue / task (required)
Provide a direct link to the issue or task this branch addresses. Example:
- Issue / Task / TestCase : https://github.com/UA-5307-TAQC/greencity5307/issues/{id}

Note: PRs without a valid issue/task/testcase link may be closed without review.

## Link to Allure results for this PR (required)
Provide a URL to the Allure report or CI artifact that contains the test results for this PR. Examples:
- Allure server: https://ua-5307-taqc.github.io/greencity5307/{pr-id}
- CI artifact: https://github.com/UA-5307-TAQC/greencity5307/actions?query=branch%{branch-name}

If CI produces `allure-results` as an artifact, include a direct link to the artifact or to the published Allure report.

## Type of change
- [ ] Bug fix
- [ ] New test(s)
- [ ] Test refactor / cleanup
- [ ] CI / pipeline change
- [ ] Documentation
- [ ] Other: ________

## Environment & Configuration
- Browsers to run tests on (must be listed in PR): e.g. Chrome, Firefox
- Optional runtime flags: e.g. BROWSER=chrome, HEADLESS=true

## How to run tests locally (PowerShell)
1. Create and activate a virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
2. Install dependencies
```powershell
pip install -r requirements.txt
```
3. Run the full test suite
```powershell
pytest -q
```
4. Run a single test
```powershell
pytest tests/path/to/test_module.py::test_name -q
```
5. Generate Allure results locally
```powershell
allure serve allure-results
```
6. Example of selecting browser via environment variable
```powershell
$env:BROWSER = 'chrome'; pytest -q
# or for Firefox
$env:BROWSER = 'firefox'; pytest -q
```

## Notes for reviewers
- Test intent: does the test verify the intended behavior?
- Reliability: are waits, locators, and assertions robust (minimize flakiness)?
- CI: did the pipeline run, and are Allure results available?
- Security: no secrets, tokens, or credentials are included in the PR.

## Author checklist (before requesting review)
- [ ] I added a link to the issue/task/testcase (required)
- [ ] I added a link to the Allure results for this PR (required)
- [ ] I ran tests locally: `pytest -q`
- [ ] I ran linting: `pylint .` (or the project's configured linter)
- [ ] I updated documentation if needed (tests, configs, or setup)
- [ ] No secrets or credentials are included in this PR
- [ ] If browser tests were added, I listed which browsers to run on

## Reviewer checklist
- [ ] Issue/task/testcase matches the changes in the PR
- [ ] Allure results are present and show passed/failed tests
- [ ] Tests are meaningful and do not duplicate existing coverage
- [ ] CI is green or there is an explained reason for failures

## Files changed (high level)
List the main files changed and a short note about the change. Example:
- `tests/...` - added/changed tests
- `components/...` - updated helpers/selectors

---
Thank you for your contribution! Please ensure required fields (issue link and Allure results) are provided before requesting a review.
