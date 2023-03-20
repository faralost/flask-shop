def test_index_page_status_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_new_item(item):
    assert item.name == 'Test Item'
    assert item.price == 1.99
