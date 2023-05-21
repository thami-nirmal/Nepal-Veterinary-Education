from django.contrib import admin
from .models import Post, PostComments, PostViews, PostLikes, UserViews, PostDescription, PostTags
from django.utils.safestring import mark_safe

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['user','title','slug','feature_image','is_published','created_at','updated_at','short_description']

admin.site.register(Post, PostAdmin)


class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ['user','post','comment']

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


class PostDescriptionAdmin(admin.ModelAdmin):
    list_display = ['post','formatted_content']

    def formatted_content(self, obj):
        return mark_safe(obj.description)

    formatted_content.short_description = 'description'

admin.site.register(PostDescription, PostDescriptionAdmin)


class PostTagsAdmin(admin.ModelAdmin):
    list_display = ['post','tags']

admin.site.register(PostTags, PostTagsAdmin)





