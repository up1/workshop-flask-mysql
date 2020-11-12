def test_root(client) -> None:
    rv = client.get("/")
    assert rv.status_code == 200
    assert rv.json == [{"username": "test user", "email": "some@email.co"}]
