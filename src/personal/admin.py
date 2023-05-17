from django.contrib import admin
from personal.models import Notice, Experts, KrishiDiarys, Ads

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['name','url','is_shown','is_external']

admin.site.register(Notice, NoticeAdmin)

class ExpertsAdmin(admin.ModelAdmin):
    list_display = ['name','description']

admin.site.register(Experts, ExpertsAdmin)

class KrishiDiarysAdmin(admin.ModelAdmin):
    list_display = ['name','pdf_url','is_shown']

admin.site.register(KrishiDiarys, KrishiDiarysAdmin)

class AdsAdmin(admin.ModelAdmin):
    list_display = ['position','image','is_shown']

admin.site.register(Ads, AdsAdmin)

