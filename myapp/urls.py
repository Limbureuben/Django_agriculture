from .views import *
from django.urls import path

urlpatterns = [
    path('farm-report/', FarmReportView.as_view(), name='farm-report')
]
