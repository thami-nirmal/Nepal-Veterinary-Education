from django.db import models

# Create your models here.
class Notice(models.Model):
    """
    Represents Notice with specific attributes.
    """
    name            = models.CharField(max_length=50,blank=True)
    url             = models.URLField(max_length=200)
    is_shown        = models.BooleanField(default=True)
    is_external     = models.BooleanField(default=False)

    def __str__(self):
        """
        :return: the name of Notice representation of Notice
        """
        return self.name
    
    class Meta:
        verbose_name_plural = 'Notice'

class Experts(models.Model):
    """
    Represents Experts with specific attributes
    """
    name            = models.CharField(max_length=50, blank=True)
    description     = models.TextField()

    def __str__(self):
        """
        :return: the name of Experts representation of Experts
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Expert'

class KrishiDiarys(models.Model):
    """
    Represents KrishiDiarys with specific attributes
    """
    name             = models.CharField(max_length=50, blank=True)
    pdf_url          = models.URLField(max_length=200)
    is_shown         = models.BooleanField(default=True)

    def __str__(self):
        """
        :return: the name of Krishi Diarys representation of KrishiDiarys
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Krishi Diary'
        
class Ads(models.Model):
    """
    Represents Ads with specific attributes
    """
    position          = models.CharField(max_length=50,blank=True)
    image             = models.ImageField(upload_to='ads/')
    is_shown          = models.BooleanField(default=True)
    
    def __str__(self):
        """
        :return: the position of Ads representation of Ads
        """
        return self.position
    
    class Meta:
        verbose_name_plural = 'Ads'


    

    
    