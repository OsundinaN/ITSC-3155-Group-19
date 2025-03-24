from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone  # ✅ Import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100, default="Negotiable")  # ✅ Default salary
    contract_time = models.CharField(max_length=100, default="Unknown")  
    meets = models.CharField(max_length=100, default="Not specified")  
    start_date = models.DateField(default=timezone.now)  # ✅ Default start date
    end_date = models.DateField(default=timezone.now)  # ✅ Default end date
    description = models.TextField()
    skills = models.TextField(default="No skills specified")  # ✅ Default skills

    def __str__(self):
        return f"{self.title} at {self.company}"
    
    from django.db import models

class Review(models.Model):
    company = models.CharField(max_length=255)
    reviewer = models.CharField(max_length=255)  # Name of the reviewer
    rating = models.FloatField()  # Example: 4.5 out of 5
    role = models.CharField(max_length=255)  # Example: "Web Developer"
    review_text = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} - {self.company} ({self.rating}/5)"

