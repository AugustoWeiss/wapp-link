from django.urls import path
from . import views
from .models import QR_link


urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('<str:key>', views.create_redirect),
    path('create-link/', views.create_link, name='create-link'),
    path('contact-us/', views.contact_view, name='contact-page')
]
