from django.contrib import admin
from personal.models import NewsAndNotice, Experts, KrishiDiarys, Ads, NewsLetter, CustomerFeedback, UsefulLinks, DrugIndex

# Register your models here.
class NewsAndNoticeAdmin(admin.ModelAdmin):
    list_display = ['name','title','short_description','image','url','is_shown','is_news']

admin.site.register(NewsAndNotice, NewsAndNoticeAdmin)


class ExpertsAdmin(admin.ModelAdmin):
    list_display = ['name','designation','image','facebook_url','linkedin_url','website']

admin.site.register(Experts, ExpertsAdmin)


class KrishiDiarysAdmin(admin.ModelAdmin):
    list_display = ['name','pdf_url','is_shown']

admin.site.register(KrishiDiarys, KrishiDiarysAdmin)


class AdsAdmin(admin.ModelAdmin):
    list_display = ['position','image','is_shown']

admin.site.register(Ads, AdsAdmin)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email','subscribe']

admin.site.register(NewsLetter, NewsLetterAdmin)


class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','message','is_read']

admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)


class UsefulLinksAdmin(admin.ModelAdmin):
    list_display = ['name','url','is_shown']

admin.site.register(UsefulLinks, UsefulLinksAdmin)


class DrugIndexAdmin(admin.ModelAdmin):
    list_display = ['trade_name','composition','dosage','remarks','image','is_shown']

admin.site.register(DrugIndex, DrugIndexAdmin)


