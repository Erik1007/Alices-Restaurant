from . import views
from django.urls import path

urlpatterns = [
    path('reviews.html', views.PostList.as_view(), name='review')
]