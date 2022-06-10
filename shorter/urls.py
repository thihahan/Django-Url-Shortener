from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:url>', views.create, name='create')
]