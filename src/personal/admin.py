from django.contrib import admin
from personal.models import (NewsAndNotice, 
                            Experts,
                            KrishiDiarys,
                            Ads,
                            NewsLetter,
                            CustomerFeedback,
                            UsefulLinks,
                            DrugIndex)

# Register your models here.
class NewsAndNoticeAdmin(admin.ModelAdmin):
    list_display        = ['name','title','author','date','short_description','image','url','is_shown','is_news']
    list_filter         = ['is_shown', 'is_news']
    search_fields       = ['name','title']

    fieldsets = [
        (None, {'fields': ['name','title','author','short_description','image','url','is_shown','is_news']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(NewsAndNotice, NewsAndNoticeAdmin)


class ExpertsAdmin(admin.ModelAdmin):
    list_display         = ['name','designation','image','facebook_url','linkedin_url','website','is_shown']
    list_filter          = ['is_shown']
    search_fields        = ['name','organization']

admin.site.register(Experts, ExpertsAdmin)


class KrishiDiarysAdmin(admin.ModelAdmin):
    list_display         = ['name','pdf_url','is_shown']
    list_filter          = ['is_shown']
    search_fields        = ['name']

    fieldsets = [
        (None, {'fields': ['name','pdf_url','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(KrishiDiarys, KrishiDiarysAdmin)


class AdsAdmin(admin.ModelAdmin):
    list_display            = ['position','image','link','is_shown']
    list_filter             = ['is_shown']
    search_fields           = ['position']

admin.site.register(Ads, AdsAdmin)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display            = ['email','subscribe']
    list_filter             = ['subscribe']
    search_fields           = ['email']

admin.site.register(NewsLetter, NewsLetterAdmin)


class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display          = ['first_name','last_name','email','message','is_read']
    list_filter           = ['is_read']
    search_fields         = ['first_name','last_name','email']

admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)


class UsefulLinksAdmin(admin.ModelAdmin):
    list_display          = ['name','url','is_shown']
    list_filter           = ['is_shown']
    search_fields         = ['name']

admin.site.register(UsefulLinks, UsefulLinksAdmin)


class DrugIndexAdmin(admin.ModelAdmin):
    list_display           = ['trade_name','composition','indication_contraindication','dosage','remarks','image','is_shown']
    list_filter            = ['is_shown']
    search_fields          = ['trade_name','composition','indication_contraindication','dosage']

    fieldsets = [
        (None, {'fields': ['trade_name','composition','indication_contraindication','dosage','remarks','image','is_shown']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(DrugIndex, DrugIndexAdmin)


