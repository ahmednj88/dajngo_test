from rest_framework.serializers import ModelSerializer
from .models import *

class postSerializer(ModelSerializer):
   class Meta:
             model=posts
             fields='__all__'
             depth = 1

class employeeSerializer(ModelSerializer):
   class Meta:
             model=employeemodels
             fields='__all__'
             depth = 1



class companySerializer(ModelSerializer):
   class Meta:
             model=company
             fields='__all__'
             depth = 1
