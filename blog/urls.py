from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.showBlogs, name='showblogs'),
]