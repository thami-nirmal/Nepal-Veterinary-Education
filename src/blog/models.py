import uuid
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    """
    Represents a Post with specific attributes
    """
    uuid                     = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    user                     = models.ForeignKey(User, related_name = 'post_user',on_delete = models.CASCADE)
    slug                     = models.SlugField(max_length = 50)
    title                    = models.CharField(max_length = 50,blank = True)
    feature_image            = models.ImageField(upload_to='profile_images/', blank = True, null = True)
    is_published             = models.BooleanField(default = False)
    created_at               = models.DateField(auto_now_add = True)
    updated_at               = models.DateField(auto_now = True)
    short_description        = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: user associated with post 
        """
        return str(self.user)

    class Meta:
        verbose_name_plural  = 'Post'


class PostComments(models.Model):
    """
    Represents comment on a Post with specific attributes
    """
    user                  = models.ForeignKey(User, related_name='postComment_user' ,on_delete=models.CASCADE)
    post                  = models.ForeignKey(Post, related_name='postComment_post',on_delete=models.CASCADE)
    comment               = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: user associated with post comment
        """
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Post Comments'


class PostViews(models.Model):
    """
    Represents views of a post with specific attributes
    """
    post                 = models.ForeignKey(Post, related_name='postViews_post',on_delete=models.CASCADE)
    views                = models.PositiveIntegerField(null=True)

    def __str__(self):
        """
        :return: the post associated with post views
        """
        return str(self.post)

    class Meta:
        verbose_name_plural = 'Post Views'


class PostLikes(models.Model):
    """
    Represents likes on a post with specific attributes
    """
    user                 = models.ForeignKey(User, related_name='postLikes_user',on_delete=models.CASCADE)
    post                 = models.ForeignKey(Post, related_name='postLikes_post',on_delete=models.CASCADE)
    is_liked             = models.BooleanField(default=False)

    def __str__(self):
        """
        :return: user associated post likes 
        """
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Post Likes'


class UserViews(models.Model):
    """
    Represents views of user on a post with specific attributes
    """
    user                = models.ForeignKey(User,related_name='userViews_user', on_delete=models.CASCADE)
    post                = models.ForeignKey(Post,related_name='userViews_post', on_delete=models.CASCADE)

    def __str__(self):
        """
        :return: user associated with User views
        """
        return str(self.user)

    class Meta:
        verbose_name_plural = 'User Views'


class PostDescription(models.Model):
    """
    Represents description of a post with specific attributes
    """
    post                 = models.ForeignKey(Post, related_name='postDescription_post',on_delete=models.CASCADE)
    description          = RichTextField()

    def __str__(self):
        """
        :return: post associated with post description
        """
        return str(self.post)

    class Meta:
        verbose_name_plural = 'Post Description'


class PostTags(models.Model):
    """
    Represents tags associated with post with specific attributes
    """
    post               = models.ForeignKey(Post,related_name='postTags_post', on_delete=models.CASCADE)
    tags               = models.CharField(max_length=200, blank=True)

    def __str__(self):
        """
        :return: post associated with post tags
        """
        return str(self.post)

    class Meta:
        verbose_name_plural = 'Post Tags'
