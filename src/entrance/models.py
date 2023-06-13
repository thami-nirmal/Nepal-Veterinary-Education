from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class PastQuestion(models.Model):
    """
    Represents a Past Question with specific attributes.
    """
    year                                      = models.PositiveIntegerField(null=True)
    is_shown                                  = models.BooleanField(default=True)
    pdf_url                                   = models.URLField(max_length=200)
    is_pdf                                    = models.BooleanField(default=True)
    content                                   = RichTextUploadingField(null=True, blank=True)
    types                                     = models.CharField(max_length=100, blank=True)
    seo_title                                 = models.CharField(max_length=50, blank=True)
    seo_keyword                               = models.CharField(max_length=200, blank=True)
    seo_image                                 = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description                           = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the Year representation of the Past Question.
        """
        return str(self.year)

    class Meta:
        verbose_name_plural = 'Past Question'


class GK(models.Model):
    """
    Represents a GK i.e. General Knowledge with specific attributes.
    """
    name                                      = models.CharField(max_length=50,blank=True)
    is_shown                                  = models.BooleanField(default=True)
    pdf_url                                   = models.URLField(max_length=200)
    is_pdf                                    = models.BooleanField(default=True)
    content                                   = RichTextUploadingField(null=True,blank=True)
    seo_title                                 = models.CharField(max_length=50, blank=True)
    seo_keyword                               = models.CharField(max_length=200, blank=True)
    seo_image                                 = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description                           = models.TextField(blank=True)


    def __str__(self):
        """
        :return: the name of General Knowledge representation of the GK.
        """
        return self.name
    
    class Meta:
        verbose_name_plural = 'GK'
        

class ModelQuestion(models.Model):
    """
    Represents a Model Question with specific attributes.
    """
    name                                      = models.CharField(max_length=50,blank=True)
    model_code                                = models.CharField(max_length=50, blank=True)
    is_shown                                  = models.BooleanField(default=True)
    pdf_url                                   = models.URLField(max_length=200)
    is_pdf                                    = models.BooleanField(default=True)
    content                                   = RichTextUploadingField(null=True,blank=True)
    seo_title                                 = models.CharField(max_length=50, blank=True)
    seo_keyword                               = models.CharField(max_length=200, blank=True)
    seo_image                                 = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description                           = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the name of Model Question representation of the Model.
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Model Question'


university_choices        = (
                                ('AFU', 'Agriculture and Forestry University'),
                                ('TU', 'Tribhuvan University'),
                                ('PU', 'Purwanchal University'),
                                )
faculty_choices           = (
                                ('B.V.Sc and A.H', 'B.V.Sc and A.H / B.Sc Fisheries'),
                                ('B.Sc Agriculture', 'B.Sc Agriculture'),
                                ('B.Sc Forestry', 'B.Sc Forestry'),
                                )


class SyllabusInfo(models.Model):
    """
    Represents a Syllabus Info  with specific attributes
    """
    university_choices                        = models.CharField(max_length=100, choices=university_choices, blank=True)
    faculty_choices                           = models.CharField(max_length=100, choices=faculty_choices, blank=True)
    subject                                   = models.CharField(max_length=50,blank=True)
    no_of_question                            = models.PositiveIntegerField(null=True)
    marks                                     = models.PositiveSmallIntegerField(null=True)
    is_shown                                  = models.BooleanField(default=True)
    seo_title                                 = models.CharField(max_length=50, blank=True)
    seo_keyword                               = models.CharField(max_length=200, blank=True)
    seo_image                                 = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description                           = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the University Choices  representation of SyllabusInfo.
        """
        return self.university_choices

    class Meta:
        verbose_name_plural = 'Syllabus Info'


class CollegeInfo(models.Model):
    """
    Represents a College Info with specific attributes.
    """
    university_choices                        = models.CharField(max_length=100, choices=university_choices,default='')
    faculty_choices                           = models.CharField(max_length=100, choices=faculty_choices,default='')
    quota_name                                = models.CharField(max_length=50,blank=True)
    no_of_student                             = models.PositiveSmallIntegerField(null=True)
    is_shown                                  = models.BooleanField(default=True)
    seo_title                                 = models.CharField(max_length=50, blank=True)
    seo_keyword                               = models.CharField(max_length=200, blank=True)
    seo_image                                 = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description                           = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the University Choices representation of CollegeInfo.
        """
        return self.university_choices

    class Meta:
        verbose_name_plural = 'College Info'

    
    
    



