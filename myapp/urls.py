from .views import *
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('farm-report/', FarmReportView.as_view(), name='farm-report')
]
