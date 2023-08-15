from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_contractor, name='add_contractor'),
    path('success/', views.success, name='success'),
]
