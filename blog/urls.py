from . import views
from django.urls import path
from .views import PostList, AddComment


urlpatterns = [
    path('reviews/', views.PostList.as_view(), name='post_list'),
    path('add_comment/', views.AddComment.as_view(), name='add_comment'),  
    path('', views.HomeScreen.as_view(), name='home'),
]