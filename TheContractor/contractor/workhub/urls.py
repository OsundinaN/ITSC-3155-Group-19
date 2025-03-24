from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import bootstrap_template  # Import the bootstrap view

urlpatterns = [
    path('', views.home, name='home'),  
    path('jobs/', views.job_list, name='jobs'),  
    path('reviews/', views.reviews, name='reviews'),
    path('my-jobs-reviews/', views.my_jobs_reviews, name='my_jobs_reviews'),
    path('profile/', views.profile, name='profile'),
    path("search/", views.search, name="search"),
    path("jobs/<int:job_id>/", views.job_detail, name="job_detail"),
    path("feedback/", views.feedback, name="feedback"),
    path("contact/", views.contact, name="contact"),  # Removed duplicate
    path("privacy/", views.privacy, name="privacy"), 
    path("terms/", views.terms, name="terms"),
    path("bootstrap/", views.bootstrap_template, name='bootstrap_template'),  # Renders Bootstrap template
]

# ✅serve static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
