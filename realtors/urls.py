from django.urls import path
from .views import realtors_index, realtor_detail

urlpatterns = [
    path('', realtors_index, name='realtors'), 
    path('<int:realtor_id>', realtor_detail, name='realtor')
]
