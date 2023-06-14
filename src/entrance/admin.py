from django.contrib import admin
from entrance.models import PastQuestion, GK, ModelQuestion, SyllabusInfo, CollegeInfo
from django.utils.safestring import mark_safe

# Register your models here.
class PastQuestionAdmin(admin.ModelAdmin):
    list_display            = ['year','is_shown','pdf_url','is_pdf','formatted_content','types']
    list_filter             = ['is_shown', 'is_pdf']
    search_fields           = ['year']

    fieldsets = [
        (None, {'fields': ['year','is_shown','pdf_url','is_pdf','content','types']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(PastQuestion, PastQuestionAdmin)


class GKAdmin(admin.ModelAdmin):
    list_display          = ['name','is_shown','pdf_url','is_pdf','formatted_content']
    list_filter           = ['is_shown']
    search_fields         = ['name']

    fieldsets = [
        (None, {'fields': ['name','is_shown','pdf_url','is_pdf','content']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(GK, GKAdmin)


class ModelQuestionAdmin(admin.ModelAdmin):
    list_display            = ['name','model_code','is_shown','pdf_url','is_pdf','formatted_content']
    list_filter             = ['is_shown', 'is_pdf']
    search_fields           = ['name']


    fieldsets = [
        (None, {'fields': ['name','model_code','is_shown','pdf_url','is_pdf','content']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(ModelQuestion, ModelQuestionAdmin)

class SyllabusInfoAdmin(admin.ModelAdmin):
    list_display         = ['university_choices','faculty_choices','subject','no_of_question','marks','is_shown']
    list_filter          = ['is_shown', 'university_choices','faculty_choices']
    search_fields        = ['subject']

    fieldsets = [
        (None, {'fields': ['university_choices','faculty_choices','subject','no_of_question','marks','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(SyllabusInfo, SyllabusInfoAdmin)

class CollegeInfoAdmin(admin.ModelAdmin):
    list_display        = ['university_choices','faculty_choices','quota_name','no_of_student','is_shown']
    list_filter         = ['is_shown', 'university_choices','faculty_choices']
    search_fields       = ['quota_name']

    fieldsets = [
        (None, {'fields': ['university_choices','faculty_choices','quota_name','no_of_student','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]
    
admin.site.register(CollegeInfo, CollegeInfoAdmin)