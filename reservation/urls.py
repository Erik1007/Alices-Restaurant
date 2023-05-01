from django.urls import path
from . import views
from .views import search_reservation, delete_reservation, update_reservation


app_name = "reservation/"

urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
    path('search_reservation/', search_reservation, name='search_reservation'),
    path('update_reservation/', update_reservation, name='update_reservation'),
    path('delete_reservation/<uuid:reservation_id>/', delete_reservation, name='delete_reservation'),
]