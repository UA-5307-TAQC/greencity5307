<!--
Please fill out this template to help reviewers quickly understand your change.
Remove any sections that are not relevant.
-->

# Pull Request

## Summary

Briefly describe the change and why it was made.

- What: (short description)
- Why: (context / motivation / issue)

## Related issue / ticket

Link to the issue or task number if applicable: e.g. Fixes #123

## Type of change

- [ ] Bug fix
- [ ] New feature
- [ ] Refactor / code cleanup
- [ ] Tests added or updated
- [ ] Documentation changes
- [ ] CI / build changes

## Checklist for authors (before requesting review)

- [ ] I ran the test suite locally: `pytest -q`
- [ ] I ran linting: `pylint .` (or the project's linter configuration)
- [ ] I formatted code where needed: `black .` (if the project uses black)
- [ ] I updated or added relevant documentation
- [ ] I added tests for new behavior (unit / integration)
- [ ] No sensitive data or credentials are included in this PR

## How to test / reproduce

Provide step-by-step instructions so reviewers can verify the change locally.
Include commands and any required environment setup. Example:

1. Create and activate virtual environment
    - `python -m venv .venv` ; `.\.venv\Scripts\Activate.ps1` (Windows PowerShell)
2. Install dependencies
    - `pip install -r requirements.txt`
3. Run tests
    - `pytest tests/path_to_test.py::test_name -q`
4. Optional: lint
    - `pylint .`

If the change involves browser automation, include which browsers/configs to test (e.g. Chrome, Firefox).

## Files changed (high level)

List the main files changed and a short note about the change. Example:

- `pages/create_habit_page.py` - added X
- `components/header_component.py` - fixed Y

## Screenshots / recordings

If the change affects UI, attach screenshots or short recordings showing before/after.

## Notes for reviewers

Anything special to pay attention to (performance, edge cases, risky parts).

## Reviewer checklist

- [ ] Code follows project style and conventions
- [ ] Tests cover new or changed behavior
- [ ] No obvious security issues
- [ ] All CI checks pass (if configured)

## Merge strategy / post-merge steps

- Preferred merge method: `Squash and merge` / `Rebase and merge` / `Create a merge commit`
- If applicable, update changelog or release notes
- If this change requires DB migrations or infrastructure changes, mention how they will be applied

---
Thank you for the contribution! Please ensure the checklist is completed before requesting a review.
