from django.urls import path,include
from . import api
urlpatterns=[
    path('',api.properties_list,name='api_properties_list'),
    path('create/',api.create_property,name='api_create_property')
]
