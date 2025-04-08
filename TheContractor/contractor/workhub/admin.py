from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Job
from .models import ContractorOfTheMonth


admin.site.register(CustomUser, UserAdmin)
admin.site.register(ContractorOfTheMonth)

