from . import views
from django.urls import path
from .views import PostDetail


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('reviews/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]