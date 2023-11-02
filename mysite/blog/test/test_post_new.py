import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from mysite.blog.models import Post


@pytest.mark.django_db
def test_post_new_view(client):
    # Cria um usuário de teste
    User.objects.create_user(username='testuser', password='testpass')

    # Faz login do usuário de teste
    client.login(username='testuser', password='testpass')

    # Define os dados do formulário
    form_data = {
        'title': 'Test Title',
        'text': 'Test Content',
        # Adicione outros campos do formulário aqui
    }

    # Faz uma requisição POST para a view
    response = client.post(reverse('blog:post_new'), form_data)

    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 302

    # Verifica se o post foi criado
    assert Post.objects.filter(title='Test Title', text='Test Content').exists()
