import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    Represents profile i.e. user profile with specific attributes.
    """
    uuid                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user                 = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name           = models.CharField(max_length=50, blank=True)
    last_name            = models.CharField(max_length=50, blank=True)
    username             = models.EmailField(max_length=254, null=True)
    email                = models.EmailField(max_length=254, null=True)
    profile_image        = models.ImageField(upload_to = 'profile_images/', blank=True, null=True)
    created_at           = models.DateField(auto_now_add=True)
    updated_at           = models.DateField(auto_now=True)

    def __str__(self):
        """
        :return: the user-name of User representation of Profile.
        """
        return self.user.username

    class Meta:
        verbose_name_plural = 'User Profile'
