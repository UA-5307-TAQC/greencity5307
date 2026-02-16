<!--
Updated pull request template for an automated testing repository.
Please fill all required fields before requesting a review.
-->

# Pull Request

## Summary
Briefly describe the change and why it was made.
- What: (short description)
- Why: (context / motivation / related issue)

## Link to issue / task (required)
Provide a direct link to the issue or task this branch addresses. Example:
- Issue / Task: https://github.com/<org>/<repo>/issues/123

Note: PRs without a valid issue/task link may be closed without review.

## Link to Allure results for this PR (required)
Provide a URL to the Allure report or CI artifact that contains the test results for this PR. Examples:
- Allure server: https://allure.example.com/reports/<project>/pr-123
- CI artifact: https://github.com/<org>/<repo>/actions/runs/<run-id>/artifacts

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
pytest --alluredir=allure-results
# then (if you have allure CLI installed):
allure serve allure-results
```
6. Example of selecting browser via environment variable
```powershell
$env:BROWSER = 'chrome'; pytest -q
# or for Firefox
$env:BROWSER = 'firefox'; pytest -q
```

## CI / Allure guidance for PR authors
- Ensure CI run for the PR produces `allure-results` and that a link to the report or artifact is added to the "Allure results" field above.
- If your CI publishes Allure to a server, paste the public URL.
- If CI attaches `allure-results` as an artifact, paste the artifact link (GitHub Actions / GitLab CI artifact URL).

## Notes for reviewers
- Test intent: does the test verify the intended behavior?
- Reliability: are waits, locators, and assertions robust (minimize flakiness)?
- CI: did the pipeline run, and are Allure results available?
- Security: no secrets, tokens, or credentials are included in the PR.

## Author checklist (before requesting review)
- [ ] I added a link to the issue/task (required)
- [ ] I added a link to the Allure results for this PR (required)
- [ ] I ran tests locally: `pytest -q`
- [ ] I ran linting: `pylint .` (or the project's configured linter)
- [ ] I updated documentation if needed (tests, configs, or setup)
- [ ] No secrets or credentials are included in this PR
- [ ] If browser tests were added, I listed which browsers to run on

## Reviewer checklist
- [ ] Issue/task matches the changes in the PR
- [ ] Allure results are present and show passed/failed tests
- [ ] Tests are meaningful and do not duplicate existing coverage
- [ ] CI is green or there is an explained reason for failures

## Files changed (high level)
List the main files changed and a short note about the change. Example:
- `tests/...` - added/changed tests
- `components/...` - updated helpers/selectors

---
Thank you for your contribution! Please ensure required fields (issue link and Allure results) are provided before requesting a review.
