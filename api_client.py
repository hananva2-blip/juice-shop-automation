import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, **kwargs):
        return self.session.get(self.base_url + path, **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(self.base_url + path, **kwargs)

    def login(self, email, password):
        """Logs in and saves the token for the next requests."""
        response = self.post("/rest/user/login", json={"email": email, "password": password})
        auth = response.json()["authentication"]
        self.session.headers["Authorization"] = f"Bearer {auth['token']}"
        return auth
