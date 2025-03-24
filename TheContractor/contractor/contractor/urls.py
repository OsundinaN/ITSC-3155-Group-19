from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView  
from workhub import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workhub.urls')),  # Loads URLs from workhub
    path("auth/", include("django.contrib.auth.urls")),  # Django built-in auth
    path("signup/", views.signup, name="signup"),  
    path("login/", LoginView.as_view(), name="login"),  
    path("logout/", LogoutView.as_view(), name="logout"),  
]
