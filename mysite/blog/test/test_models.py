# Define a fixture to create a random 'Post' object
import pytest
from mysite.blog.models import Post
from model_bakery import baker


@pytest.fixture
def random_post():
    post = baker.make(Post)
    return post


@pytest.mark.django_db
def test_post_publish(random_post):
    # Publish the random 'Post' object
    random_post.publish()

    # Check if the 'published_date' field is not None
    assert random_post.published_date is not None

    # Check if the __str__ method returns the expected result using the attributes created by Model Bakery
    assert str(random_post) == f'{random_post.title}'
