from django.contrib import admin
from .models import Post, PostComments, PostViews, PostLikes, UserViews, PostDescription, PostTags
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['user_id','title','slug','feature_image','is_published','created_at','updated_at','short_description']

admin.site.register(Post, PostAdmin)

class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ['user_id','post_id','comment']

admin.site.register(PostComments, PostCommentsAdmin)

class PostViewsAdmin(admin.ModelAdmin):
    list_display = ['post_id','views']

admin.site.register(PostViews, PostViewsAdmin)

class PostLikesAdmin(admin.ModelAdmin):
    list_display = ['user_id','post_id','is_liked']

admin.site.register(PostLikes, PostLikesAdmin)

class UserViewsAdmin(admin.ModelAdmin):
    list_display = ['user_id','post_id']

admin.site.register(UserViews, UserViewsAdmin)

class PostDescriptionAdmin(admin.ModelAdmin):
    list_display = ['post_id','description']

admin.site.register(PostDescription, PostDescriptionAdmin)

class PostTagsAdmin(admin.ModelAdmin):
    list_display = ['post_id','tags']

admin.site.register(PostTags, PostTagsAdmin)





