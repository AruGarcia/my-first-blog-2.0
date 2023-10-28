import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get(reverse('blog:post_list'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
