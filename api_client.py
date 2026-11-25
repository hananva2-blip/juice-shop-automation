import requests


class ApiClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout  # a stuck server fails the test instead of hanging the run
        self.session = requests.Session()

    def get(self, path, **kwargs):
        return self.session.get(self.base_url + path, timeout=self.timeout, **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(self.base_url + path, timeout=self.timeout, **kwargs)

    def login(self, email, password):
        """Logs in and saves the token for the next requests."""
        response = self.post("/rest/user/login", json={"email": email, "password": password})
        assert response.status_code == 200, f"Login as {email} failed: {response.status_code} {response.text[:200]}"
        auth = response.json()["authentication"]
        self.session.headers["Authorization"] = f"Bearer {auth['token']}"
        return auth
