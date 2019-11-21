from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField()

class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField(max_length=70)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)