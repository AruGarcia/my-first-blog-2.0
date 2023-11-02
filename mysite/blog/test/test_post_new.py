import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from mysite.blog.models import Post


@pytest.mark.django_db
def test_post_new_view(client):
    # Bild a user for the test
    User.objects.create_user(username='testuser', password='testpass')

    # log in of the user
    client.login(username='testuser', password='testpass')

    # Define the form data
    form_data = {
        'title': 'Test Title',
        'text': 'Test Content',
    }

    # Faz uma requisição POST para a view
    response = client.post(reverse('blog:post_new'), form_data)

    # Verifica se a requisição foi bem-sucedida
    assert response.status_code == 302

    # Verifica se o post foi criado
    assert Post.objects.filter(title='Test Title', text='Test Content').exists()

    # Verifica o comportamento quando o método da requisição não é "POST"
    response_get = client.get(reverse('blog:post_new'))
    assert response_get.status_code == 200  # Ou o código de status adequado para visualização do formulário de criação
    # Adicione outras asserções relacionadas à visualização do formulário aqui
