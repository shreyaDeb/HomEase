from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('contact/', views.contact, name='contact'),
    # Other URL patterns...
]
