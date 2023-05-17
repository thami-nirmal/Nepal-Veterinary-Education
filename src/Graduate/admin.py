from django.contrib import admin
from Graduate.models import Subject, Chapter, MaterialType, SemYear, Level

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display=['subject_name','has_chapter_content','content','pdf_URL','is_pdf','is_visible','material_type']

admin.site.register(Subject,SubjectAdmin)

class ChapterAdmin(admin.ModelAdmin):
    list_display=['chapter_no','content','pdf_URL','is_pdf','is_visible','subject']

admin.site.register(Chapter,ChapterAdmin)

class MaterialTypeAdmin(admin.ModelAdmin):
    list_display=['material_name','slug','is_visible','sem_year']

admin.site.register(MaterialType,MaterialTypeAdmin)

class SemYearAdmin(admin.ModelAdmin):
    list_display=['sem_year_num','is_visible','level']

admin.site.register(SemYear,SemYearAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display=['level_name','is_visible']

admin.site.register(Level,LevelAdmin)
