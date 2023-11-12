from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]