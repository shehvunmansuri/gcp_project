from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from django.http import JsonResponse, request
from .models import *
from django.http import JsonResponse
from django.views import View
from django.db import transaction
import json

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
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

class CustomerPOSTAPI(View):
    sserialzier_class = CustomerPostSerializer

    @transaction.atomic
    def post(self, request, Format=None):
        response = {}
        print(request.body, 'request.body printed')

        data = json.loads(request.body)
        print(data, 'data printed')
        serializer = self.sserialzier_class(data=data)
        print(serializer, 'serializer printed')

        if serializer.is_valid():
            try:
                create_customer = serializer.save()
                print(create_customer, 'create_customer printed')
                return JsonResponse({"message": "Customer created successfully"}, status=200)
            except Exception as e:
                print(e, 'error while creating customer')
        return JsonResponse({"message": "Invalid data", "errors": serializer.errors}, status=400)
