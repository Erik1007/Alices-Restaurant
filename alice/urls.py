"""alice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from alice.views import HomeScreen
from blog.views import HomeScreen, PostList, AddComment 

from . import views
from reservation import views as reservation_views
from reservation.views import confirm_reservation, search_reservation, reservation_details, delete_reservation, reserve_table, update_reservation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('reserve_table/', reserve_table, name='reserve_table'),
    path('reviews/', PostList.as_view(), name='reviews'),
    path('add_comment/', AddComment.as_view(), name='add_comment'),
    path('menu/', views.menu, name='menu'),
    path('barmenu/', views.barmenu, name='barmenu'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('signup/', views.signup, name='signup'),
    path('confirm_reservation/<str:reservation_id>/', confirm_reservation,
         name='confirm_reservation'),       
    path('search_reservation/', search_reservation,
         name='search_reservation'),
    path('reservation_details/<str:reservation_id>/',
         reservation_details, name='reservation_details'),
    path('update_reservation/<str:reservation_id>/', update_reservation,
         name='update_reservation'),
    path('delete_reservation/', delete_reservation, name='delete_reservation'),
    path('failure/', views.failure, name='failure'),
    path("", HomeScreen.as_view(), name="HomeScreen")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
