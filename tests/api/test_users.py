from tests.conftest import PASSWORD


def test_register_duplicate_email(api, user):
    response = api.post("/api/Users", json={"email": user["email"], "password": PASSWORD, "passwordRepeat": PASSWORD})
    assert response.status_code == 400


def test_login_success(api, user):
    auth = api.login(user["email"], user["password"])
    assert auth["token"]
    assert auth["umail"] == user["email"]


def test_login_wrong_password(api, user):
    response = api.post("/rest/user/login", json={"email": user["email"], "password": "wrong-password"})
    assert response.status_code == 401
