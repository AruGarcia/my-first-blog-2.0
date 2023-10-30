import pytest
from django.template import Template, Context
from datetime import datetime
from mysite.blog.models import Post  # Substitua 'mysite.blog' pelo nome do seu aplicativo


@pytest.fixture
def posts():
    return [
        Post(title='Post 1', published_date=datetime(2023, 10, 23), text='Texto do Post 1'),
        Post(title='Post 2', published_date=datetime(2023, 10, 24), text='Texto do Post 2'),
    ]


def format_date(date):
    return date.strftime("%d de %B de %Y às %H:%M")


def test_render_posts_template(posts):
    template_code = """
    {% for post in posts %}
        <article>
            <time>published: {{ post.published_date }}</time>
            <h2><a href="">{{ post.title }}</a></h2>
            <p>{{ post.text|linebreaksbr }}</p>
        </article>
    {% endfor %}
    """

    template = Template(template_code)

    # Formate as datas no mesmo formato esperado pelo template
    formatted_posts = [
        {
            'title': post.title,
            'published_date': format_date(post.published_date),
            'text': post.text
        }
        for post in posts
    ]

    context = Context({'posts': formatted_posts})

    rendered_template = template.render(context)

    for post in formatted_posts:
        assert f"published: {post['published_date']}" in rendered_template
        assert f"<h2><a href=\"\">{post['title']}</a></h2>" in rendered_template
        assert f"<p>{post['text']}</p>" in rendered_template
