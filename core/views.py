from http.client import HTTPResponse
import re
from django.db import reset_queries
# from django.http import HTTPResponse
from django.shortcuts import redirect, render
from django.views.generic.base import RedirectView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import DataFieldSerializer
from .models import DataField
# from core import serializers
# Create your views here.

def home(request):

    return render(request, 'core/index.html')

def cab1(request):

    return render(request, 'core/sharecab.html')

@api_view(["GET"])
def get_all_data(request):

    # For extracting information from the database

    data = DataField.objects.all()

    # many=True will serialize the entire data from the query than a single one which will happen in the 
    # other case
    serializer = DataFieldSerializer(data, many = True)
    return Response(serializer.data)


# Single data

@api_view(["GET"])
def get_data(request, pk):

    # For extracting information from the database

    data = DataField.objects.get(id=pk)

    # many=False will serialize only one data from the query than everything which will happen in the 
    # other case
    serializer = DataFieldSerializer(data, many = False)
    return Response(serializer.data)

# Saving new data
@api_view(["POST"])
def post_data(request):

    # Requesting the posted data
    data = request.data

    # Saving the data into the database
    DataField.objects.create(
        name = data['name'],
        ph_no = data['ph_no'],
        time = data['time'],
        start = data['start'],
        end = data['end'],
    )
    # Displaying the newly saved data (many=False as we're only displaying a single data)
    # serializer = DataFieldSerializer(data, many=False)
    return HttpResponse('User added')