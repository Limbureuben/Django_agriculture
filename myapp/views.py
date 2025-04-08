from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
# Create your views here.

class FarmReportView(APIView):
    def post(self, request):
        serializers = FarmSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "success", "data": serializers.data})