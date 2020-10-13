from django.urls import path
from CFD import views

urlpatterns = [
    path('', views.get_name, name='get_name'),
]