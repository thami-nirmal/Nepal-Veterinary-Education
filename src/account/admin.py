from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','email','profile_image','updated_at','created_at']
    
admin.site.register(Profile, ProfileAdmin)

