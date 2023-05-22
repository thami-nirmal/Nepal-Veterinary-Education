from django.db import models

# Create your models here.
class NewsAndNotice(models.Model):
    """
    Represents News and Notice with specific attributes.
    """
    name                          = models.CharField(max_length=50,blank=True)
    title                         = models.CharField(max_length=50, blank=True)
    short_description             = models.CharField(max_length=300, blank=True)
    image                         = models.ImageField(upload_to='news_notice_images/', blank=True, null=True)
    url                           = models.URLField(max_length=200)
    is_shown                      = models.BooleanField(default=True)
    is_news                       = models.BooleanField(default=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the name of News and Notice
        """
        return self.name
    
    class Meta:
        verbose_name_plural = 'News and Notice'


class Experts(models.Model):
    """
    Represents Experts with specific attributes
    """
    name                    = models.CharField(max_length=50, blank=True)
    designation             = models.CharField(max_length=50, blank=True)
    organization            = models.CharField(max_length=50, blank=True)
    image                   = models.ImageField(upload_to='expert_images/', blank=True, null=True)
    facebook_url            = models.URLField(max_length=200, null=True)
    linkedin_url            = models.URLField(max_length=200, null=True)
    website                 = models.URLField(max_length=200, null=True)

    def __str__(self):
        """
        :return: the name of Experts representation of Experts
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Experts'


class KrishiDiarys(models.Model):
    """
    Represents KrishiDiarys with specific attributes
    """
    name                          = models.CharField(max_length=50, blank=True)
    pdf_url                       = models.URLField(max_length=200)
    is_shown                      = models.BooleanField(default=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

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
    position                = models.CharField(max_length=30,blank=True)
    image                   = models.ImageField(upload_to='ads/', blank=True, null=True)
    is_shown                = models.BooleanField(default=True)
    
    def __str__(self):
        """
        :return: the position of Ads representation of Ads
        """
        return self.position
    
    class Meta:
        verbose_name_plural = 'Ads'


class NewsLetter(models.Model):
    """
    Represents a news letter subscription entry
    """
    email                = models.EmailField(max_length=254)
    subscribe            = models.BooleanField(default=False)

    def __str__(self):
        """
        :return: the email address of subscriber
        """
        return self.email

    class Meta:
        verbose_name_plural = 'News Letter'

    
class CustomerFeedback(models.Model):
    """
    Represents a customer feedback entry
    """
    first_name                = models.CharField(max_length=50, blank=True)
    last_name                 = models.CharField(max_length=50, blank=True)
    email                     = models.EmailField(max_length=254, null=True)
    message                   = models.TextField()
    is_read                   = models.BooleanField(default=False)

    def __str__(self):
        """
        :return: the first name of customer
        """
        return self.first_name

    class Meta:
        verbose_name_plural  = 'Customer Feedback'

    
class UsefulLinks(models.Model):
    """
    Represents a useful links with specific attributes
    """
    name                          = models.CharField(max_length=50, blank=True)
    url                           = models.URLField(max_length=254)
    is_shown                      = models.BooleanField(default=True)

    def __str__(self):
        """
        :return: the name of useful links
        """
        return self.name

    class Meta:
        verbose_name_plural  = 'Useful Links'


class DrugIndex(models.Model):
    """
    Represents a drug index entry
    """
    trade_name                         = models.CharField(max_length=50, blank=True)
    composition                        = models.CharField(max_length=100, blank=True)
    indication_contraindication        = models.CharField(max_length=300, blank=True)
    dosage                             = models.CharField(max_length=50, blank=True)
    remarks                            = models.CharField(max_length=200, blank=True)
    image                              = models.ImageField(upload_to='drug_index_images/',blank=True)
    is_shown                           = models.BooleanField(default=True)
    seo_title                          = models.CharField(max_length=50, blank=True)
    seo_keyword                        = models.CharField(max_length=200, blank=True)
    seo_image                          = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description                    = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the composition of drug index
        """
        return self.composition

    class Meta: 
        verbose_name_plural  = 'Drug Index'

         


    


    