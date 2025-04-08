from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
# Create your views here.

class FarmReportView(APIView):
    def post(self, request):
        serializers = FarmSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Report submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)