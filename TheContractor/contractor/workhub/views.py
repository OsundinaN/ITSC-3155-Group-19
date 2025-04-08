from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
import json

from .models import CustomUser, Job, Review, ContractorOfTheMonth
from .forms import CustomUserCreationForm, EditProfileForm

from django.contrib.auth import logout



def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')



# 🔹 Homepage
def home(request):
    jobs = Job.objects.all()[:6]
    reviews = Review.objects.all()[:4]
    contractor = ContractorOfTheMonth.objects.last()
    return render(request, "workhub/home.html", {
        "jobs": jobs,
        "reviews": reviews,
        "contractor": contractor
    })

# 🔹 Signup
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful! Welcome to The Contractor.")

            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# 🔹 Search
def search(request):
    query = request.GET.get("q", "").strip()
    jobs = Job.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(company__icontains=query)
    ) if query else Job.objects.none()

    reviews = Review.objects.filter(
        Q(company__icontains=query) |
        Q(review_text__icontains=query)
    ) if query else Review.objects.none()

    return render(request, "workhub/search_results.html", {
        "jobs": jobs,
        "reviews": reviews,
        "query": query
    })

# 🔹 Job Views
@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, "workhub/jobs.html", {"jobs": jobs})

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
            return JsonResponse({"message": "Job created", "job_id": job.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"message": "Send a POST request to create a job."}, status=400)

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "workhub/job_detail.html", {"job": job})

# 🔹 Review Views
@login_required
def reviews(request):
    all_reviews = Review.objects.all()
    return render(request, "workhub/reviews.html", {"reviews": all_reviews})

@login_required
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, "workhub/review_detail.html", {"review": review})

# (Redundant view – safe to remove if not needed)
def review_list(request):
    reviews = Review.objects.all()
    return render(request, "workhub/reviews.html", {"reviews": reviews})

# 🔹 Profile and Utilities
@login_required
def profile(request):
    return render(request, "workhub/profile.html")

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'workhub/edit_profile.html', {'form': form})


@login_required
def my_jobs_reviews(request):
    return render(request, "workhub/my_jobs_reviews.html")

# 🔹 Static Pages
def feedback(request):
    return render(request, "workhub/feedback.html")

def contact(request):
    return render(request, "workhub/contact.html")

def privacy(request):
    return render(request, "workhub/privacy.html")

def terms(request):
    return render(request, "workhub/terms.html")

def bootstrap_template(request):
    return render(request, 'bootstrap_template/index.html')
