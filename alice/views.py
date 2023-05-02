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
    return render(request, 'reservation:reserve_table')


def reservation_details(request):
    return render(request, 'reservation:reservation_details')


def search_reservation(request):
    return render(request, 'reservation:search_reservation')


def update_reservation(request):
    return render(request, 'reservation:update_reservation')


def delete_reservation(request):
    return render(request, 'reservation:delete_reservation')


def success(request):
    return render(request, 'success.html')
    

def failure(request):
    return render(request, 'failure.html')
