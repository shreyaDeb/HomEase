from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success'),

    # Add other URL patterns as needed
]
