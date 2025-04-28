from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone  # ✅ Import timezone
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

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
    

class Review(models.Model):
    company = models.CharField(max_length=255)
    reviewer_name = models.CharField(max_length=255)  # ✅ Use reviewer_name
    rating = models.FloatField()
    role = models.CharField(max_length=255)
    review_text = models.TextField()
    review_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)  # ✅ Optional image

    def __str__(self):
        return f"{self.reviewer_name} - {self.company} ({self.rating}/5)"


class ContractorOfTheMonth(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    salary = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.company}"
    

from django.db import models

class JobApplication(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True, null=True)

    location = models.CharField(max_length=255, blank=True)
    linkedin = models.URLField(blank=True)

    authorized = models.CharField(max_length=10)
    sponsorship = models.CharField(max_length=10)

    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(max_length=1000, blank=True)

    experience_title = models.CharField(max_length=255, blank=True)
    experience_company = models.CharField(max_length=255, blank=True)
    experience_details = models.TextField(blank=True)

    degree = models.CharField(max_length=255, blank=True)
    school = models.CharField(max_length=255, blank=True)
    field = models.CharField(max_length=255, blank=True)
    grad_year = models.PositiveIntegerField(blank=True, null=True)

    availability = models.CharField(max_length=255, blank=True)
    relocate = models.CharField(max_length=20, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    certifications = models.CharField(max_length=255, blank=True)

    consent_emails = models.BooleanField(default=False)
    confirm_truth = models.BooleanField(default=False)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"