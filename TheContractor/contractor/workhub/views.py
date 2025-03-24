from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm  # Ensure this exists
from .models import CustomUser, Job, Review  # Ensure these exist
import json
from django.shortcuts import get_object_or_404


# 🔹 Homepage View
def home(request):
    # ✅ Fetch jobs from DB
    jobs = Job.objects.all()[:5]  # Get top 5 jobs for display

    # ✅ Fetch reviews from DB
    reviews = Review.objects.all()[:3]  # Get top 3 reviews

    return render(request, 'workhub/home.html', {"jobs": jobs, "reviews": reviews})

# 🔹 Signup View
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def search(request):
    query = request.GET.get("q", "").strip()  # Get search term and remove spaces

    jobs = Job.objects.filter(
        title__icontains=query
    ) | Job.objects.filter(
        description__icontains=query
    ) if query else Job.objects.none()

    reviews = Review.objects.filter(
        company__icontains=query
    ) | Review.objects.filter(
        review_text__icontains=query
    ) if query else Review.objects.none()

    return render(request, "workhub/search_results.html", {"jobs": jobs, "reviews": reviews, "query": query})


# 🔹 Get all jobs
def job_list(request):
    jobs = Job.objects.all()
    return render(request, "workhub/jobs.html", {"jobs": jobs})

# 🔹 Create a new job (Fixing error handling)
@csrf_exempt
def job_create(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            job = Job.objects.create(
                title=data["title"],
                company=data["company"],
                location=data["location"],
                description=data["description"],
                salary=data["salary"]
            )
            return JsonResponse({"message": "Job created successfully", "job_id": job.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"message": "Send a POST request to create a job."}, status=400)

from django.shortcuts import render


# ✅ Job Detail
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "workhub/job_detail.html", {"job": job})

def reviews(request):
    all_reviews = Review.objects.all()  # Fetch all reviews from DB
    return render(request, "workhub/reviews.html", {"reviews": all_reviews})

# ✅ Review List
def review_list(request):
    reviews = Review.objects.all()
    return render(request, "workhub/reviews.html", {"reviews": reviews})

# Placeholder view for My Jobs & Reviews
def my_jobs_reviews(request):
    return render(request, "workhub/my_jobs_reviews.html")  # Ensure this file exists


# Placeholder view for Profile Page
def profile(request):
    return render(request, "workhub/profile.html") 

def feedback(request):
    return render(request, "workhub/feedback.html")

def contact(request):
    return render(request, "workhub/contact.html")

def privacy(request):
    return render(request, "workhub/privacy.html")

def terms(request):
    return render(request, "workhub/terms.html")

def bootstrap_template(request):
    return render(request, 'bootstrap_template/index.html')  # Load Bootstrap template