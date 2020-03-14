from django.urls import path
from apptwo.views import index, users


urlpatterns = [
    path('apptwo/index/', index, name='apptwo-index'),
    path('apptwo/users/', users, name='apptwo-form'), 
] 