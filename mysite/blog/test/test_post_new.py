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

    # Make a POST request to the view
    response = client.post(reverse('blog:post_new'), form_data)

    # Verify if the request was successful
    assert response.status_code == 302

    # Verify if the post was created
    assert Post.objects.filter(title='Test Title', text='Test Content').exists()

    # Check the behavior when the request method is not "POST"
    response_get = client.get(reverse('blog:post_new'))
    assert response_get.status_code == 200

    # Verifica o comportamento quando o método da requisição não é "POST"
    response_get = client.get(reverse('blog:post_new'))
    assert response_get.status_code == 200 
    