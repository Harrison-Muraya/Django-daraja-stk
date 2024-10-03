from django.urls import path
from . import views

urlpatterns = [
    path('', views.initiate_payment, name='pay'),
]
