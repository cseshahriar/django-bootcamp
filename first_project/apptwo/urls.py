from django.urls import path
from apptwo.views import index, users

urlpatterns = [
    path('apptwo/index/', index),
    path('apptwo/users/', users), 
] 