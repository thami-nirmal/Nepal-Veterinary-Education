from django.db import models

# Create your models here.
class Subject(models.Model):
    # uuId = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    subject_name = models.CharField(max_length=50,null=True)
    has_chapter_content = models.BooleanField(default=False)
    content = models.CharField(max_length=300, null=True) 
    pdf_URL = models.URLField(max_length=200)
    Is_pdf = models.BooleanField(default=False)
    Is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.subject_name

class Chapter(models.Model):
    chapter_no = models.PositiveSmallIntegerField(null=True)
    content = models.CharField(max_length=300, null=True)
    pdf_URL = models.URLField(max_length=220,default='')
    Is_pdf = models.BooleanField(default=False)
    Is_visible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.chapter_no)
    
class MaterialType(models.Model):
    material_name = models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50)
    Is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.material_name

class SemYear(models.Model):
    sem_year_num = models.PositiveSmallIntegerField(null=True)
    Is_visible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.sem_year_num)

class Level(models.Model):
    level_name = models.CharField(max_length=50,null=True)
    Is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.level_name
    
class SyllabusInfo(models.Model):
    university_choices = (
        ('un1', 'university 1'),
        ('un2', 'university 2'),
        ('un3', 'university 3'),
        )
    faculty_choices = (
        ('fc1', 'faculty 1'),
        ('fc2', 'faculty 2'),
        ('fc3', 'faculty 3'),
        )

    university_choices = models.CharField(max_length=10, choices=university_choices)
    faculty_choices = models.CharField(max_length=10, choices=faculty_choices)
    subject = models.CharField(max_length=50,null=True)
    marks = models.PositiveSmallIntegerField(null=True)
    Is_shown = models.BooleanField(default=False)

    def __str__(self):
        return self.university_choices

class CollegeInfo(models.Model):
    university_choices = (
        ('un1', 'university 1'),
        ('un2', 'university 2'),
        ('un3', 'university 3'),
        )
    faculty_choices = (
        ('fc1', 'faculty 1'),
        ('fc2', 'faculty 2'),
        ('fc3', 'faculty 3'),
        )

    university_choices = models.CharField(max_length=10, choices=university_choices,default='')
    faculty_choices = models.CharField(max_length=10, choices=faculty_choices,default='')
    department = models.CharField(max_length=50,null=True)
    no_of_student = models.PositiveSmallIntegerField(null=True)
    Is_shown = models.BooleanField(default=False)
    


    
    



    