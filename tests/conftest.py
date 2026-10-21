import uuid

import pytest

from api_client import ApiClient

PASSWORD = "Passw0rd!"


@pytest.fixture
def api(base_url):
    return ApiClient(base_url)


@pytest.fixture
def user(api):
    """Registers a new unique user through the API."""
    email = f"user_{uuid.uuid4().hex[:8]}@test.com"
    response = api.post("/api/Users", json={"email": email, "password": PASSWORD, "passwordRepeat": PASSWORD})
    assert response.status_code == 201
    return {"email": email, "password": PASSWORD}


@pytest.fixture
def page(page, base_url):
    """Hides the welcome banner and the cookie message."""
    page.context.add_cookies([
        {"name": "welcomebanner_status", "value": "dismiss", "url": base_url},
        {"name": "cookieconsent_status", "value": "dismiss", "url": base_url},
    ])
    return page
