from django.contrib import admin
from graduate.models import Subject, SubContent, MaterialType, SemYear, Level, MaterialContent
from django.utils.safestring import mark_safe
from graduate.forms import SubjectForm, MaterialContentForm
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    form                   = SubjectForm

    list_display           = ['subject_name','slug','is_shown','level','sem_year']
    list_filter            = ['is_shown','sem_year']
    search_fields          = ['subject_name']

    fieldsets = [
        (None, {'fields': ['subject_name','is_shown','level','sem_year']}),
        # ('SEO Options', 
        # {"classes": ["collapse"],
        # 'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    class Media:
        js = (
            'js/chained_dropdown.js',
        )

    # def formatted_content(self, obj):
    #     return mark_safe(obj.content)

    # formatted_content.short_description = 'content'

admin.site.register(Subject,SubjectAdmin)


class SubContentAdmin(admin.ModelAdmin):
    list_display          = ['sub_content_name','slug','pdf_URL','is_pdf','is_shown','material_content']
    list_filter           = ['is_shown', 'is_pdf','material_content']
    ordering              = ['-sub_content_name']

    fieldsets = [
        (None, {'fields': ['sub_content_name','pdf_URL','is_pdf','is_shown','material_content']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

    def formatted_content(self, obj):
        return mark_safe(obj.content)

    formatted_content.short_description = 'content'

admin.site.register(SubContent,SubContentAdmin)


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
    form             = MaterialContentForm

    list_display     = ['has_sub_content','formatted_content','pdf_URL','is_pdf','is_shown','get_level','material_type','subject']
    list_filter      = ['is_shown','has_sub_content']

    fieldsets = [
        (None, {'fields':['has_sub_content','content','pdf_URL','is_pdf','is_shown','level','material_type','subject']}),
        # ('SEO Options',
        #  {"classes":["collapse"],
        #   'fields':['seo_title','seo_keyword','seo_image','seo_description']}),
    ]

    def get_level(self, obj):
        return obj.subject.level

    def formatted_content(self, obj):
        return mark_safe(obj.content)
    
    formatted_content.short_description = 'content'
    get_level.short_description = 'level'

    class Media:
        js = (
            'js/chained_dropdown.js',
        )

admin.site.register(MaterialContent, MaterialContentAdmin)