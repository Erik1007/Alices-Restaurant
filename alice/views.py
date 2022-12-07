from django.shortcuts import render


def menu(request):
    return render(request, 'foodmenu.html')


def barmenu(request):
    return render(request, 'barmenu.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def reviews(request):
    return render(request, 'reviews.html')


def signup(request):
    return render(request, 'signup.html')
