# Juice Shop Test Automation

[![tests](https://github.com/hananva2-blip/juice-shop-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/hananva2-blip/juice-shop-automation/actions/workflows/tests.yml)
[![Allure report](https://img.shields.io/badge/Allure-live%20report-orange)](https://hananva2-blip.github.io/juice-shop-automation/)

UI, API and security tests for [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), a deliberately insecure web shop.

**Stack:** Python · pytest · Playwright · requests · Allure · Docker · GitHub Actions · Jenkins

## Project structure
```
pages/            Page Objects (locators + actions)
api_client.py     Small API client that keeps the login token
tests/
  conftest.py     Fixtures: API client, new user per test, banner-free page
  ui/             Login, search (data-driven), basket
  api/            Products, users, basket
  security/       Security headers + SQL injection check
```

## Highlights
- Every test creates its own user through the API, so tests are independent and can run in any order
- UI tests use Playwright auto-waiting with `expect`, no sleeps
- Screenshots and traces are saved automatically when a test fails
- A known SQL injection is documented with `xfail(strict=True)`: the test fails as soon as the bug is fixed, reminding us to update it
- Runs in parallel (`pytest-xdist`) on Chromium and Firefox
- CI on every push and every night: lint (`ruff`) → tests → [live Allure report](https://hananva2-blip.github.io/juice-shop-automation/) on GitHub Pages
- Nightly Jenkins pipeline defined as code (`Jenkinsfile` + Jenkins Configuration as Code)

## Run locally
```bash
docker compose up -d
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest                    # all tests
pytest tests/api          # API tests only
pytest --headed           # watch the browser
allure serve allure-results
```

## Nightly run in Jenkins
`Jenkinsfile` runs the suite every night at ~02:00 and publishes the results with the JUnit plugin.
The `jenkins/` folder starts a ready Jenkins (job created as code) next to Juice Shop:
```bash
cd jenkins
docker compose up -d --build   # Jenkins on http://localhost:8080
```
