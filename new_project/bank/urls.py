from django.urls import path, include
from .views import *

urlpatterns = [
    path('customers', get_customers, name='get_customers'),
]


