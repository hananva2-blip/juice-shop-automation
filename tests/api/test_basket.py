def test_add_product_to_basket(api, user):
    basket_id = api.login(user["email"], user["password"])["bid"]

    response = api.post("/api/BasketItems", json={"ProductId": 1, "BasketId": basket_id, "quantity": 2})
    assert response.status_code == 200

    products = api.get(f"/rest/basket/{basket_id}").json()["data"]["Products"]
    assert products[0]["id"] == 1
    assert products[0]["BasketItem"]["quantity"] == 2


def test_basket_requires_login(api):
    response = api.get("/rest/basket/1")
    assert response.status_code == 401
