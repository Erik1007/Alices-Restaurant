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

from blog.views import HomeScreen


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path('reserve_table/', include(
        'reservation.urls', namespace='reservation')),
    path("reviews/", include("blog.urls"), name="blog"),
    path('menu/', views.menu, name='menu'),
    path('barmenu/', views.barmenu, name='barmenu'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('reviews/', views.reviews, name='reviews'),
    path('signup/', views.signup, name='signup'),
    path("", HomeScreen.as_view(), name="HomeScreen")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
