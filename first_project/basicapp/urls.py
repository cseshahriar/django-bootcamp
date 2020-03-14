from django.urls import path
from basicapp.views import index, others  

urlpatterns = [
    path('basicapp/index', index, name='basicapp-index'),
    path('basicapp/others', others, name='basicapp-others')
]
