from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact_us2.html', views.contact, name="contact"),
    path('about_us.html', views.about, name="about"),
]