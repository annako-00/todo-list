from .models import *
from rest_framework import serializers

class projectSerializer(serializers.ModelSerializer):
     class Meta:
          model=Project
          fields='__all__'

class todoSerializer(serializers.ModelSerializer):
     class Meta:
          model=Todo
          fields='__all__'