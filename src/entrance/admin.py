from django.contrib import admin
from entrance.models import PastQuestion, GK, ModelQuestion, SyllabusInfo, CollegeInfo

# Register your models here.

class PastQuestionAdmin(admin.ModelAdmin):
    list_display = ['year','is_shown','pdf_url','is_pdf','content']

admin.site.register(PastQuestion, PastQuestionAdmin)

class GKAdmin(admin.ModelAdmin):
    list_display = ['name','is_shown','pdf_url','is_pdf','content']

admin.site.register(GK, GKAdmin)

class ModelQuestionAdmin(admin.ModelAdmin):
    list_display = ['name','is_shown','pdf_url','is_pdf','content']

admin.site.register(ModelQuestion, ModelQuestionAdmin)

class SyllabusInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','subject','marks','is_shown']

admin.site.register(SyllabusInfo, SyllabusInfoAdmin)

class CollegeInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','department','no_of_student','is_shown']
    
admin.site.register(CollegeInfo, CollegeInfoAdmin)