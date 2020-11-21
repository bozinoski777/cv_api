from rest_framework import serializers
from .models import Language

class CvSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cv
    fields = ('id', 'contact', 'education', 'professional_experience', 'skills', 'organizations', 'coding_projects')
