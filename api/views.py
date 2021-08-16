from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

@api_view(['GET'])
def post(request):
    empo=posts.objects.all();
    serializers=postSerializer(empo,many=True);
    return Response(serializers.data)

@api_view(['GET'])
def employee(request):
    empo=employeemodels.objects.all();
    serializers=employeeSerializer(empo,many=True);
    return Response(serializers.data)

@api_view(['GET'])
def companygeter(request):
    empo=company.objects.all();
    serializers=companySerializer(empo,many=True);
    return Response(serializers.data)
