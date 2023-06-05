from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.
class Level(models.Model):
    """
    Represents a Level i.e Bachelor,Diploma with specific attributes
    """
    level_name                    = models.CharField(max_length=50,blank=True)
    slug                          = models.SlugField(max_length=50, unique=True, editable=False, null=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.level_name)
        super(Level, self).save(*args, **kwargs)


class SemYear(models.Model):
    """
    Represents a Semester Or Year with specific attributes
    """
    sem_year_num                  = models.PositiveSmallIntegerField(null=True)
    slug                          = models.SlugField(max_length=50, unique=True, editable=False, null=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sem_year_num)
        super(SemYear, self).save(*args, **kwargs)


class MaterialType(models.Model):
    """
    Represents a MaterialType i.e. Notes,Syllabus,Question paper,Assignments,Books etc. with specific attributes
    """
    material_name                 = models.CharField(max_length=50,blank=True)
    slug                          = models.SlugField(max_length=50, unique=True, editable=False, null=True)
    is_shown                      = models.BooleanField(default=True)
    # sem_year                      = models.ForeignKey(SemYear, related_name='MaterialType_SemYear', on_delete=models.CASCADE,null=True)
    level                         = models.ForeignKey(Level,related_name = 'MaterialType_Level',on_delete=models.CASCADE,null=True)
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
            base_slug     = slugify(self.material_name)
            level_name    = slugify(self.level.level_name)
            self.slug     = f"{base_slug}-{level_name}"
        super(MaterialType, self).save(*args, **kwargs)


class Subject(models.Model):
    """
    Represents a subject with specific attributes 
    """
    subject_name                  = models.CharField(max_length=50,blank=True)
    slug                          = models.SlugField(max_length=50, unique=True, editable=False, null=True)
    is_shown                      = models.BooleanField(default=True)
    # material_type                 = models.ForeignKey(MaterialType, related_name='Subject_MaterialType', on_delete=models.CASCADE,null=True)
    sem_year                      = models.ForeignKey(SemYear, related_name='subject_semyear', on_delete=models.CASCADE, null=True)
    level                         = models.ForeignKey(Level, related_name='subject_level', on_delete=models.CASCADE, null=True)


    def __str__(self):
        """
        :return: the Subject Name representation of the subject.
        """
        return self.subject_name

    class Meta:
        verbose_name_plural = 'Subject'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject_name)
        super(Subject, self).save(*args, **kwargs)

class MaterialContent(models.Model):
    """
    Represents a material content with a specific attributes
    """
    has_chapter_content           = models.BooleanField(default=True)
    content                       = RichTextUploadingField(null=True)
    pdf_URL                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=True)
    is_shown                      = models.BooleanField(default=True)
    material_type                 = models.ForeignKey(MaterialType, related_name='materialcontent_materialtype', on_delete=models.CASCADE, null=True)
    subject                       = models.ForeignKey(Subject, related_name='materialcontent_subject', on_delete=models.CASCADE, null=True)
    seo_title                     = models.CharField(max_length=50, blank=True)
    seo_keyword                   = models.CharField(max_length=200, blank=True)
    seo_image                     = models.ImageField(upload_to='seo_images/',blank=True, null=True)
    seo_description               = models.TextField(blank=True)

    def __str__(self):
        """
        :return: the material content representation of the material
        """
        return str(self.has_chapter_content)
    
    class Meta:
        verbose_name_plural = 'Material Content'


class Chapter(models.Model):
    """
    Represents a chapter (if Subject has_chapter_content is true) with specific attributes
    """
    chapter_no                    = models.PositiveSmallIntegerField(null=True)
    slug                          = models.SlugField(max_length=50, unique=True, editable=False, null=True)
    content                       = RichTextUploadingField(null=True)
    pdf_URL                       = models.URLField(max_length=220,default='')
    is_pdf                        = models.BooleanField(default=True)
    is_shown                      = models.BooleanField(default=True)
    # subject                       = models.ForeignKey(Subject, related_name='Chapter_Subject', on_delete=models.CASCADE,null=True)
    material_content              = models.ForeignKey(MaterialContent, related_name='chapter_materialcontent', on_delete=models.CASCADE, null=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.chapter_no)
        super(Chapter, self).save(*args, **kwargs)