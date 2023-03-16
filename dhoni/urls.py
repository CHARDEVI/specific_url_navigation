from django.urls import path
from dhoni.views import *
app_name='devi'

urlpatterns=[
    path('csk/',csk,name='csk'),
]