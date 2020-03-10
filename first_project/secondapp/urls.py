from django.urls import path
from secondapp.views import index

urlpatterns = [ 
    path('secondapp/index/', index)      
]