import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from mysite.blog.models import Post


@pytest.fixture
def client():
    from django.test import Client
    return Client()


def test_blog_post_render(client, db):
    user = User.objects.create(username="testuser")

    # Create a sample blog post
    post = Post.objects.create(
        author=user,
        title="Test Blog Post",
        text="This is the content of the test blog post.",
        published_date=datetime(2023, 5, 24)

    )

    url = reverse('blog:post_detail', kwargs={'pk': post.pk})
    response = client.get(url)

    assert response.status_code == 200
    # assert b"user" in response.content
    assert b"Test Blog Post" in response.content  # Check for the post title in the response
    assert b"This is the content of the test blog post." in response.content  # Check for the post content
    assert b"24 de Maio de 2023" in response.content  # Check for the post author
