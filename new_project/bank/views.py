from django.shortcuts import render
# from rest_framework.views import APIView
from .serializers import *
from django.http import JsonResponse
from .models import *
from django.http import JsonResponse
from django.views import View
from django.db import transaction
import json

# Create your views here.

def get_customers(request):
    print(request, 'request')
    print(request.method, 'request.method')
    print(request.GET, 'request.GET')

    search_query = request.GET.get('search', None)
    print(search_query, 'search_query')

    limit = int(request.GET.get('limit', 10))
    print(limit, 'limit printed')
    page = int(request.GET.get('page', 1))
    print(page, 'page printed')

    start = (page - 1 ) * limit
    end = page * limit

    customer = Customer.objects.all()

    if search_query:
        customer = customer.filter(name__icontains=search_query)
        print(customer, 'customer printed')

    total_count = customer.count()
    print(total_count, 'total_count printed')

    paginated_customers = customer[start:end]
    print(paginated_customers, 'paginated_customers printed')

    sesrializers = CustomerSerializer(paginated_customers, many=True)
    print(sesrializers, 'sesrializers printed')

    data = {
        "message": "Customer list fetched successfully",   
        "limit": limit,
        "page": page,
        "total_count": total_count,
        "customers": sesrializers.data

    }
    return JsonResponse(data, status=200)