from django.urls import path
from fourthapp.views import index 
 
# fourthapp urls 
urlpatterns = [
    path('fourthapp/index', index, name='fourthapp-index')  
]
