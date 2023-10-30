import pytest
from django.urls import reverse
from django.test import Client
from mysite.blog.models import Post


def create_post(title, published_date, text):
    # Crie um objeto Post com a data formatada corretamente
    post = Post(title=title, published_date=published_date, text=text)
    return post


@pytest.fixture
def posts():
    # Crie objetos Post usando a função auxiliar
    formatted_posts = [
        create_post('', '', ''),
        create_post('', '', ''),
    ]
    return formatted_posts


@pytest.mark.django_db
def test_render_posts_view(posts):
    client = Client()
    url = reverse('blog:post_list')

    response = client.get(url)

    assert response.status_code == 200

    response_text = response.content.decode('utf-8')

    for post in posts:
        if post.title:
            assert post.title in response_text
        if post.text:
            assert post.text in response_text
        if post.published_date:
            assert post.published_date.strftime('%d de %B de %Y às %H:%M') in response_text
