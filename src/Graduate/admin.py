from django.contrib import admin
from Graduate.models import Subject, Chapter, MaterialType, SemYear, Level, CollegeInfo, SyllabusInfo
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display=['subject_name','has_chapter_content','content','pdf_URL','Is_pdf','Is_visible']
admin.site.register(Subject,SubjectAdmin)

class ChapterAdmin(admin.ModelAdmin):
    list_display=['chapter_no','content','pdf_URL','Is_pdf','Is_visible']
admin.site.register(Chapter,ChapterAdmin)

class MaterialTypeAdmin(admin.ModelAdmin):
    list_display=['material_name','slug','Is_visible']
admin.site.register(MaterialType,MaterialTypeAdmin)

class SemYearAdmin(admin.ModelAdmin):
    list_display=['sem_year_num','Is_visible']
admin.site.register(SemYear,SemYearAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display=['level_name','Is_visible']
admin.site.register(Level,LevelAdmin)

class SyllabusInfoAdmin(admin.ModelAdmin):
    list_display=['university_choices','faculty_choices','subject','marks','Is_shown']
admin.site.register(SyllabusInfo,SyllabusInfoAdmin)

class CollegeInfoAdmin(admin.ModelAdmin):
    list_display=['university_choices','faculty_choices','department','no_of_student','Is_shown']
admin.site.register(CollegeInfo,CollegeInfoAdmin)