from django.contrib import admin
from post_graduate.models import CouncilAct, CouncilRegulation, CouncilModelQuestion, LoksewaModelQuestion, CouncilPastQuestion, LoksewaPastQuestion, LoksewaNotes, SyllabusInfo, CollegeInfo
# Register your models here.
class CouncilActAdmin(admin.ModelAdmin):
    list_display = ['name','pdf_url','is_shown']

admin.site.register(CouncilAct, CouncilActAdmin)

class CouncilRegulationAdmin(admin.ModelAdmin):
    list_display = ['name','pdf_url','is_shown']

admin.site.register(CouncilRegulation, CouncilRegulationAdmin)

class CouncilModelQuestionAdmin(admin.ModelAdmin):
    list_display = ['is_shown','pdf_url','is_pdf','content']

admin.site.register(CouncilModelQuestion, CouncilModelQuestionAdmin)

class LoksewaModelQuestionAdmin(admin.ModelAdmin):
    list_display = ['is_shown','pdf_url','is_pdf','content']

admin.site.register(LoksewaModelQuestion, LoksewaModelQuestionAdmin)

class CouncilPastQuestionAdmin(admin.ModelAdmin):
    list_display = ['is_shown','year','pdf_url','is_pdf','content']

admin.site.register(CouncilPastQuestion, CouncilPastQuestionAdmin)

class LoksewaPastQuestionAdmin(admin.ModelAdmin):
    list_display = ['is_shown','year','pdf_url','is_pdf','content']

admin.site.register(LoksewaPastQuestion, LoksewaPastQuestionAdmin)

class LoksewaNotesAdmin(admin.ModelAdmin):
    list_display = ['is_shown','pdf_url','is_pdf','content']

admin.site.register(LoksewaNotes, LoksewaNotesAdmin)

class SyllabusInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','subject','marks','is_shown']

admin.site.register(SyllabusInfo, SyllabusInfoAdmin)

class CollegeInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','department','no_of_student','is_shown']
    
admin.site.register(CollegeInfo, CollegeInfoAdmin)
