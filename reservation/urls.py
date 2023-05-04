from django.urls import path
from . import views
from .views import search_reservation, delete_reservation, update_reservation


app_name = "reservation"

urlpatterns = [
    
    path('', views.reserve_table, name='reserve_table'),
    ]