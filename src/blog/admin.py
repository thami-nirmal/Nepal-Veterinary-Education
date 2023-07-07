from django.contrib import admin
from .models import Post, PostComments, PostViews, PostLikes, UserViews, PostTags, PostCategory, FeaturePost
from django.utils.safestring import mark_safe

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display          = ['uuid','user','title','slug','feature_image','is_published','created_at','updated_at','short_description','post_category','formatted_content']
    list_filter           = ['is_published', 'post_category']
    search_fields         = ['title', 'short_description']
    ordering              = ['-created_at', '-updated_at']

    def formatted_content(self, obj):
        return mark_safe(obj.description)

    formatted_content.short_description = 'description'

    fieldsets = [
        (None, {'fields': ['user', 'title','feature_image','is_published','short_description','post_category','description']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(Post, PostAdmin)


class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ['user','post','comment','date']

admin.site.register(PostComments, PostCommentsAdmin)


class PostViewsAdmin(admin.ModelAdmin):
    list_display = ['post','views']

admin.site.register(PostViews, PostViewsAdmin)


class PostLikesAdmin(admin.ModelAdmin):
    list_display = ['user','post','is_liked']

admin.site.register(PostLikes, PostLikesAdmin)


class UserViewsAdmin(admin.ModelAdmin):
    list_display = ['user','post']

admin.site.register(UserViews, UserViewsAdmin)



class PostTagsAdmin(admin.ModelAdmin):
    list_display = ['post','tags']

admin.site.register(PostTags, PostTagsAdmin)


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','colour']

    fieldsets = [
        (None, {'fields': ['name', 'colour']}),
        ('SEO Options', 
        {"classes": ["collapse"],
        'fields': ['seo_title', 'seo_keyword', 'seo_image', 'seo_description']}),
    ]

admin.site.register(PostCategory, PostCategoryAdmin)


class FeaturePostAdmin(admin.ModelAdmin):
    list_display = ['position','post']

admin.site.register(FeaturePost, FeaturePostAdmin)







