import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    """
    Represents profile i.e. user profile with specific attributes.
    """
    uuid                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user                 = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name           = models.CharField(max_length=50, blank=True)
    last_name            = models.CharField(max_length=50, blank=True)
    email                = models.EmailField(max_length=254, null=True)
    profile_image        = models.ImageField(upload_to = 'profile_images/', blank=True, null=True)
    verified_email_otp   = models.CharField(max_length=5, blank=True, null=True)
    created_at           = models.DateField(auto_now_add=True)
    updated_at           = models.DateField(auto_now=True)

    def __str__(self):
        """
        :return: the user-name of User representation of Profile.
        """
        return self.user.username

    class Meta:
        verbose_name_plural       = 'User Profile' 


# This code snippet defines a signal receiver function that gets triggered
# After a User model instance is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    """
    Signal receiver function that creates or updates a Profile instance
    when a User instance is saved.

    Args:
        sender (class): The class that sent the signal (User model in this case).
        instance (User): The specific User instance that was saved.
        **kwargs: Additional keyword arguments passed to the receiver.

    Returns:
        None
    """

    # Check if a profile instance already exists for the User
    if Profile.objects.filter(user = instance).exists():
        # If a Profile instance exists, update its fields with values from the User instance.
        Profile.objects.filter(user = instance).update(first_name=instance.first_name,last_name = instance.last_name,email = instance.email)
    else:
        # If no Profile instance exists, create a new one using default values.
        # The email field is set using the username of the User instance.
        Profile.objects.create(user=instance,email=instance.username+'@nepalvetedu.com',first_name='admin',last_name='admin')


    

