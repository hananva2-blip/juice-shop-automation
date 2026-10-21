def test_get_all_products(api):
    response = api.get("/api/Products")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


def test_search_products(api):
    response = api.get("/rest/products/search", params={"q": "apple"})
    names = [product["name"] for product in response.json()["data"]]
    assert names and all("apple" in name.lower() for name in names)
