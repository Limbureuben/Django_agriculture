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
    
    def get(self, request):
        report = FarmReport.objects.all().order_by('-id')
        serializers = FarmSerializer(report, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    