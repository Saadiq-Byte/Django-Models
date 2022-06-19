from django.db import models

# Create your models here.

class Title (models.Model):
    name = models.CharField(max_length=200)
class Text (models.Model):
    name = models.TextField()
class Created_Date (models.Model):
    name = models.DateTimeField()
class Published_date (models.Model):
    name = models.DateTimeField()