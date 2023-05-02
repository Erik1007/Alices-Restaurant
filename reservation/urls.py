from django.urls import path
from . import views
from .views import search_reservation, delete_reservation, update_reservation


app_name = "reservation/"

urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
    path('reservation_details/<uuid:reservation_id>/', views.reservation_details, name='reservation_details'),
    path('search_reservation/<uuid:reservation_id>/', views.search_reservation, name='search_reservation'),
    path('update_reservation/<uuid:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('delete_reservation/<uuid:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    ]