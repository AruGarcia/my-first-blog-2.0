import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('blog:post_list'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    content = resp.content.decode("utf-8")
    assert "Django Girls blog" in content
