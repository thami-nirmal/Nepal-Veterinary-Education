from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class CouncilAct(models.Model):
    """
    Represents council act with specific attributes
    """
    name                          = models.CharField(max_length=50,blank=True)
    pdf_url                       = models.URLField(max_length=200)
    is_shown                      = models.BooleanField(default=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the name of council act representation of CouncilAct
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Council Act'

class CouncilRegulation(models.Model):
    """
    Represents council regulation with specific attributes
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
        :return: the name of council regulation representation of CouncilRegulation
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Council Regulation'
    
class CouncilModelQuestion(models.Model):
    """
    Represents council model question with specific attributes
    """
    name                          = models.CharField(max_length=50, blank=True)
    is_shown                      = models.BooleanField(default=True)
    pdf_url                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=True)
    content                       = RichTextUploadingField(null=True, blank=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the pdf url of council model question representation of CouncilModelQuestion
        """
        return self.pdf_url

    class Meta:
        verbose_name_plural = 'Council Model Question'

class CouncilPastQuestion(models.Model):
    """
    Represents council past question with specific attributes
    """
    is_shown                      = models.BooleanField(default=True)
    year                          = models.PositiveIntegerField(null=True)
    pdf_url                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=True)
    content                       = RichTextUploadingField(null=True, blank=True)
    types                         = models.CharField(max_length=60, blank=True) 
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)
    
    def __str__(self):
        """
        :return: the year of council past question representation of CouncilPastQuestion
        """
        return str(self.year)

    class Meta:
        verbose_name_plural = 'Council Past Question'


class LoksewaModelQuestion(models.Model):
    """
    Represents loksewa model question with specific attributes
    """
    name                          = models.CharField(max_length=50, blank=True)
    is_shown                      = models.BooleanField(default=True)
    pdf_url                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=True)
    content                       = RichTextUploadingField(null=True, blank=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the pdf url of loksewa model question representation of LoksewaModelQuestion
        """
        return self.pdf_url

    class Meta:
        verbose_name_plural = 'Loksewa Model Question'


class LoksewaPastQuestion(models.Model):
    """
    Represents loksewa past question with specific attributes
    """
    is_shown                      = models.BooleanField(default=True)
    year                          = models.PositiveIntegerField(null=True)
    pdf_url                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=True)
    content                       = RichTextUploadingField(null=True,blank=True)
    types                         = models.CharField(max_length=60, blank=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)
    
    def __str__(self):
        """
        :return: the year of loksewa past question representation of LoksewaPastQuestion
        """
        return str(self.year)

    class Meta:
        verbose_name_plural = 'Loksewa Past Question'


class LoksewaNotes(models.Model):
    """
    Represents loksewa notes with specific attributes
    """
    name                          = models.CharField(max_length=50, blank=True)
    is_shown                      = models.BooleanField(default=True)
    pdf_url                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=True)
    content                       = RichTextUploadingField(null=True,blank=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the pdf url of loksewa notes representation of LoksewaNotes
        """
        return self.pdf_url

    class Meta:
        verbose_name_plural = 'Loksewa Note'


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
    university_choices            = models.CharField(max_length=100, choices=university_choices, blank=True)
    faculty_choices               = models.CharField(max_length=100, choices=faculty_choices, blank=True)
    subject                       = models.CharField(max_length=50,blank=True)
    no_of_question                = models.PositiveIntegerField(null=True)
    marks                         = models.PositiveSmallIntegerField(null=True)
    is_shown                      = models.BooleanField(default=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the University Choices representation of SyllabusInfo.
        """
        return self.university_choices

    class Meta:
        verbose_name_plural = 'Syllabus Info'


class CollegeInfo(models.Model):
    """
    Represents a College Info with specific attributes.
    """
    university_choices              = models.CharField(max_length=100, choices=university_choices,default='')
    faculty_choices                 = models.CharField(max_length=100, choices=faculty_choices,default='')
    quota_name                      = models.CharField(max_length=50,blank=True)
    no_of_student                   = models.PositiveSmallIntegerField(null=True)
    is_shown                        = models.BooleanField(default=True)
    seo_title                       = models.CharField(max_length=50, blank=True)
    seo_keyword                     = models.CharField(max_length=200, blank=True)
    seo_image                       = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description                 = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the University Choices representation of CollegeInfo.
        """
        return self.university_choices

    class Meta:
        verbose_name_plural = 'College Info'



