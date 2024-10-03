from django.urls import path
from . import views

urlpatterns = [
    path('', views.lipa_na_mpesa, name='lipa_na_mpesa'),
]
