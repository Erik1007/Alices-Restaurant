from django.shortcuts import render, get_object_or_404
from django.views import generic, View


class HomeScreen(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


def menu(request):
    return render(request, 'foodmenu.html')


def barmenu(request):
    return render(request, 'barmenu.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def reserve_table(request):
    return render(request, 'reservation/reservation.html')


def my_booking(request):
    return render(request, 'search_reservation.html')


def confirm_reservation(request, reservation_id):
    return render(request, 'success.html', {'reservation_id': reservation_id})


def reservation_details(request, reservation_id):
    return render(request, 'reservation_details.html', {'reservation_id': reservation_id})


def search_reservation(request, reservation_id):
    pass


def update_reservation(request, reservation_id):
    return render(request, 'update_reservation.html', {'reservation_id': reservation_id})


def delete_reservation(request, reservation_id):
    return render(request, 'delete_reservation.html', {'reservation_id': reservation_id})


def success(request):
    return render(request, 'success.html')
  

def failure(request):
    return render(request, 'failure.html')
