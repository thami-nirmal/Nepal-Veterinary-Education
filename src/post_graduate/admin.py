from django.contrib import admin
from post_graduate.models import CouncilAct, CouncilRegulation, CouncilModelQuestion, LoksewaModelQuestion, CouncilPastQuestion, LoksewaPastQuestion, LoksewaNotes, SyllabusInfo, CollegeInfo
from django.utils.safestring import mark_safe

# Register your models here.
class CouncilActAdmin(admin.ModelAdmin):
    list_display = ['name','pdf_url','is_shown']
    list_filter = ['is_shown']
    search_fields = ['name',]

    fieldsets = [
        (None, {'fields': ['name','pdf_url','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(CouncilAct, CouncilActAdmin)


class CouncilRegulationAdmin(admin.ModelAdmin):
    list_display = ['name','pdf_url','is_shown']
    list_filter = ['is_shown']
    search_fields = ['name']

    fieldsets = [
        (None, {'fields': ['name','pdf_url','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(CouncilRegulation, CouncilRegulationAdmin)


class CouncilModelQuestionAdmin(admin.ModelAdmin):
    list_display = ['name','is_shown','pdf_url','is_pdf','formatted_content']
    list_filter = ['is_shown', 'is_pdf']
    search_fields = ['name']

    fieldsets = [
        (None, {'fields': ['name','is_shown','pdf_url','is_pdf','content']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(CouncilModelQuestion, CouncilModelQuestionAdmin)


class LoksewaModelQuestionAdmin(admin.ModelAdmin):
    list_display = ['name','is_shown','pdf_url','is_pdf','formatted_content']
    list_filter = ['is_shown', 'is_pdf']
    search_fields = ['name']

    fieldsets = [
        (None, {'fields': ['name','is_shown','pdf_url','is_pdf','content']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(LoksewaModelQuestion, LoksewaModelQuestionAdmin)


class CouncilPastQuestionAdmin(admin.ModelAdmin):
    list_display = ['is_shown','year','pdf_url','is_pdf','formatted_content','types']
    list_filter = ['is_shown','is_pdf']
    search_fields = ['types']
    ordering = ['-year']

    fieldsets = [
        (None, {'fields': ['is_shown','year','pdf_url','is_pdf','content','types']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)
    
    formatted_content.short_description = 'content'

admin.site.register(CouncilPastQuestion, CouncilPastQuestionAdmin)


class LoksewaPastQuestionAdmin(admin.ModelAdmin):
    list_display = ['is_shown','year','pdf_url','is_pdf','formatted_content','types']
    list_filter = ['is_shown', 'is_pdf']
    search_fields = ['types']
    ordering = ['-year']

    fieldsets = [
        (None, {'fields': ['is_shown','year','pdf_url','is_pdf','content','types']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)
    
    formatted_content.short_description = 'content'

admin.site.register(LoksewaPastQuestion, LoksewaPastQuestionAdmin)


class LoksewaNotesAdmin(admin.ModelAdmin):
    list_display = ['name','is_shown','pdf_url','is_pdf','formatted_content']
    list_filter = ['is_shown', 'is_pdf']
    search_fields = ['name']

    fieldsets = [
        (None, {'fields': ['name','is_shown','pdf_url','is_pdf','content']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(LoksewaNotes, LoksewaNotesAdmin)


class SyllabusInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','subject','marks','is_shown']
    list_filter = ['university_choices','faculty_choices', 'is_shown']
    search_fields = ['subject']

    fieldsets = [
        (None, {'fields': ['university_choices','faculty_choices','subject','marks','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(SyllabusInfo, SyllabusInfoAdmin)


class CollegeInfoAdmin(admin.ModelAdmin):
    list_display = ['university_choices','faculty_choices','department','no_of_student','is_shown']
    list_filter = ['university_choices', 'faculty_choices','is_shown']
    search_fields = ['department']

    fieldsets = [
        (None, {'fields': ['university_choices','faculty_choices','department','no_of_student','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]
    
admin.site.register(CollegeInfo, CollegeInfoAdmin)
