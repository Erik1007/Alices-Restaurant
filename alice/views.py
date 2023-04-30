from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
    

def menu(request):
    return render(request, 'foodmenu.html')


def barmenu(request):
    return render(request, 'barmenu.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def reserve_table(request):
    return render(request, 'reservation:reserve_table')


def success(request):
    return render(request, 'success.html')
    

def failure(request):
    return render(request, 'failure.html')
