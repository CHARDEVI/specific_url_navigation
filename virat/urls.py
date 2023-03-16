from django.urls import path
from virat.views import *
app_name='cherry'

urlpatterns=[
    path('rcb/',rcb,name='rcb'),
]