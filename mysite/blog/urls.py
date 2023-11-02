from django.urls import path

from .views import post_list, post_detail, post_new

app_name = 'blog'
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
]
