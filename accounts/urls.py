from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard , name='dashboard'),
    path('login/', login, name='login'),
    path('signin/',signin, name='signin'),
    path('logout/', logout, name='logout'),
]