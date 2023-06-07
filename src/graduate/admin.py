from django.contrib import admin
from graduate.models import Subject, Chapter, MaterialType, SemYear, Level, MaterialContent
from django.utils.safestring import mark_safe

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display           = ['subject_name','slug','is_shown','level','sem_year']
    list_filter            = ['is_shown','sem_year']
    search_fields          = ['subject_name']

    fieldsets = [
        (None, {'fields': ['subject_name','is_shown','level','sem_year']}),
        # ('SEO Options', 
        # {"classes": ["collapse"],
        # 'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    # def formatted_content(self, obj):
    #     return mark_safe(obj.content)

    # formatted_content.short_description = 'content'

admin.site.register(Subject,SubjectAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display          = ['chapter_no','slug','pdf_URL','is_pdf','is_shown','material_content']
    list_filter           = ['is_shown', 'is_pdf','material_content']
    ordering              = ['-chapter_no']

    fieldsets = [
        (None, {'fields': ['chapter_no','pdf_URL','is_pdf','is_shown','material_content']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(Chapter,ChapterAdmin)


class MaterialTypeAdmin(admin.ModelAdmin):
    list_display           = ['material_name','slug','is_shown','level']
    list_filter            = ['is_shown', 'level']
    search_fields          = ['material_name']

    fieldsets = [
        (None, {'fields': ['material_name','is_shown','level']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(MaterialType,MaterialTypeAdmin)


class SemYearAdmin(admin.ModelAdmin):
    list_display          = ['sem_year_num','slug','is_shown','level','is_year']
    list_filter           = ['is_shown', 'level','is_year']
    search_fields         = ['sem_year_num']

    fieldsets = [
        (None, {'fields': ['sem_year_num','is_shown','level','is_year']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(SemYear,SemYearAdmin)


class LevelAdmin(admin.ModelAdmin):
    list_display          = ['level_name','slug','is_shown']
    list_filter           = ['is_shown']
    search_fields         = ['level_name']

    fieldsets = [
        (None, {'fields': ['level_name','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(Level,LevelAdmin)


class MaterialContentAdmin(admin.ModelAdmin):
    list_display     = ['has_chapter_content','formatted_content','pdf_URL','is_pdf','is_shown','material_type','subject']
    list_filter      = ['is_shown']

    fieldsets = [
        (None, {'fields':['has_chapter_content','content','pdf_URL','is_pdf','is_shown','material_type','subject']}),
        ('SEO Options',
         {"classes":["collapse"],
          'fields':['seo_title','seo_keyword','seo_image','seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)
    
    formatted_content.short_description = 'content'

admin.site.register(MaterialContent, MaterialContentAdmin)