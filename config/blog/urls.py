from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('blog/create', views.create, name='create'),
    path('blog/<int:blog_id>', views.detail, name='detail'),
     path('blog/delete/<int:blog_id>', views.delete, name='delete'),
]