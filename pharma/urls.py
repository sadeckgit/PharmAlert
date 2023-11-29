from django.urls import path
from .views import index, localisation

urlpatterns = [
    path('', index, name='index'),
    path('localisation/<str:slug>/', localisation, name='localisation_detail'),
]
