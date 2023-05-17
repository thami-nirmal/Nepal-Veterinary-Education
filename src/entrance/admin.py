from django.contrib import admin
from entrance.models import Entrance, GK, SyllabusInfo, CollegeInfo
# Register your models here.

class EntranceAdmin(admin.ModelAdmin):
    list_display = ['year','is_shown','pdf_url','is_pdf','content']
admin.site.register(Entrance, EntranceAdmin)

class GKAdmin(admin.ModelAdmin):
    list_display = ['is_shown','pdf_url','is_pdf','content']
admin.site.register(GK, GKAdmin)

class SyllabusInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','subject','marks','is_shown']
admin.site.register(SyllabusInfo, SyllabusInfoAdmin)

class CollegeInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','department','no_of_student','is_shown']
admin.site.register(CollegeInfo, CollegeInfoAdmin)