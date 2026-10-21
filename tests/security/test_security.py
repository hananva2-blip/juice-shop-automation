import pytest


@pytest.mark.parametrize("header, value", [
    ("X-Content-Type-Options", "nosniff"),
    ("X-Frame-Options", "SAMEORIGIN"),
])
def test_security_headers(api, header, value):
    response = api.get("/")
    assert response.headers.get(header) == value


@pytest.mark.xfail(reason="Known vulnerability: Juice Shop login is open to SQL injection", strict=True)
def test_login_blocks_sql_injection(api):
    response = api.post("/rest/user/login", json={"email": "' OR 1=1--", "password": "x"})
    assert response.status_code == 401
