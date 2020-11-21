from django.db import models

class Cv(models.Model):
  contact = models.CharField(max_length=50)
  education = models.CharField(max_length=50)
  professional_experience = models.CharField(max_length=50)
  skills = models.CharField(max_length=50)
  organizations = models.CharField(max_length=50)
  coding_projects = models.CharField(max_length=50)
