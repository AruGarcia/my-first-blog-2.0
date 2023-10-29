from django.test import Client


def test_status_code(client: Client, db):
    resp = client.get('/')
    assert resp.status_code == 200
