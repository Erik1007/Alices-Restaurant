from django.urls import path
from . import views
from .views import search_reservation, delete_reservation, update_reservation


app_name = "reservation"

urlpatterns = [
    path('reservation_details/', views.reservation_details, name='reservation_details'),
    path('search_reservation/', views.search_reservation, name='search_reservation'),
    path('update_reservation/', views.update_reservation, name='update_reservation'),
    path('delete_reservation/', views.delete_reservation, name='delete_reservation'),
    path('', views.reserve_table, name='reserve_table'),
    ]