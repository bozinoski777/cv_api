from django.shortcuts import render
from rest_framework import viewsets
from .models import CvSerializer
from .serializers import CvSerializer

class CvView(viewsets.ModelViewSet):
  queryset = Cv.objects.all()
  serializer_class = CvSerializer
# Create your views here.
