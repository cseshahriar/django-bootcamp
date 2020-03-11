from django.urls import path 
from thirdapp.views import index

urlpatterns = [
    path('thirdapp/index', index, name='thirdapp') 
]