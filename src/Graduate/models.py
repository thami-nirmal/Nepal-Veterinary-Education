from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
class Level(models.Model):
    """
    Represents a Level i.e Bachelor,Diploma with specific attributes
    """
    level_name                    = models.CharField(max_length=50,blank=True)
    is_shown                      = models.BooleanField(default=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the level name representation of the Level.
        """
        return self.level_name
    
    class Meta:
        verbose_name_plural = 'Level'


class SemYear(models.Model):
    """
    Represents a Semester Or Year with specific attributes
    """
    sem_year_num                  = models.PositiveSmallIntegerField(null=True)
    is_shown                      = models.BooleanField(default=True)
    level                         = models.ForeignKey(Level, related_name='SemYear_Level', on_delete=models.CASCADE,null=True)
    is_year                       = models.BooleanField(default=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)


    def __str__(self):
        """
        :return: the semester number or year number representation of the SemYear.
        """
        return str(self.sem_year_num)

    class Meta:
        verbose_name_plural = 'Semester Year'


class MaterialType(models.Model):
    """
    Represents a MaterialType i.e. Notes,Syllabus,Question paper,Assignments,Books etc. with specific attributes
    """
    material_name                 = models.CharField(max_length=50,blank=True)
    slug                          = models.SlugField(max_length=50, unique=True, editable=False)
    is_shown                      = models.BooleanField(default=True)
    sem_year                      = models.ForeignKey(SemYear, related_name='MaterialType_SemYear', on_delete=models.CASCADE,null=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the material name representation of the MaterialType.
        """
        return self.material_name

    class Meta:
        db_table = 'Material Type'
        verbose_name_plural = 'Material Type'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.material_name)
        super(MaterialType, self).save(*args, **kwargs)


class Subject(models.Model):
    """
    Represents a subject with specific attributes 
    """
    subject_name                  = models.CharField(max_length=50,blank=True)
    has_chapter_content           = models.BooleanField(default=False)
    content                       = RichTextUploadingField(null=True)
    pdf_URL                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=False)
    is_shown                      = models.BooleanField(default=True)
    material_type                 = models.ForeignKey(MaterialType, related_name='Subject_MaterialType', on_delete=models.CASCADE,null=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the Subject Name representation of the subject.
        """
        return self.subject_name

    class Meta:
        verbose_name_plural = 'Subject'


class Chapter(models.Model):
    """
    Represents a chapter (if Subject has_chapter_content is true) with specific attributes
    """
    chapter_no                    = models.PositiveSmallIntegerField(null=True)
    content                       = RichTextUploadingField(null=True)
    pdf_URL                       = models.URLField(max_length=220,default='')
    is_pdf                        = models.BooleanField(default=False)
    is_shown                      = models.BooleanField(default=True)
    subject                       = models.ForeignKey(Subject, related_name='Chapter_Subject', on_delete=models.CASCADE,null=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the chapter number representation of the chapter.
        """
        return str(self.chapter_no)

    class Meta:
        verbose_name_plural = 'Chapter'
        





    
    



    