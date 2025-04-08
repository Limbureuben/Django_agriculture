
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class FarmSerializer(serializers.Modelserializer):
    class Meta:
        model = FarmReport
        fields = '__all__'

