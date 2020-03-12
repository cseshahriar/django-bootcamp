from django.urls import path
from basicform.views import index, form_name_view

urlpatterns = [
    path('form/index', index, name='form-index'),
    path('form/create', form_name_view, name='form-create')
]
