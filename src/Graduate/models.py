from django.db import models

# Create your models here.
class Subject(models.Model):
    """Represents a subject with specific attributes"""
    subject_name                  = models.CharField(max_length=50,blank=True)
    has_chapter_content           = models.BooleanField(default=False)
    content                       = models.CharField(max_length=300, blank=True) 
    pdf_URL                       = models.URLField(max_length=200)
    is_pdf                        = models.BooleanField(default=False)
    is_visible                    = models.BooleanField(default=True)

    def __str__(self):
        """Returns the subject_name representation of the subject."""
        return self.subject_name

class Chapter(models.Model):
    """Represents a chapter with specific attributes"""
    chapter_no                    = models.PositiveSmallIntegerField(null=True)
    content                       = models.CharField(max_length=300, blank=True)
    pdf_URL                       = models.URLField(max_length=220,default='')
    is_pdf                        = models.BooleanField(default=False)
    is_visible                    = models.BooleanField(default=True)
    subject                       = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
 
    def __str__(self):
        """Returns the chapter number representation of the chapter."""
        return str(self.chapter_no)
    
class MaterialType(models.Model):
    """Represents a MaterialType with specific attributes"""
    material_name                 = models.CharField(max_length=50,blank=True)
    slug                          = models.SlugField(max_length=50)
    is_visible                    = models.BooleanField(default=True)

    def __str__(self):
        """Returns the material name representation of the MaterialType."""
        return self.material_name

class SemYear(models.Model):
    """Represents a SemYear with specific attributes"""
    sem_year_num                  = models.PositiveSmallIntegerField(null=True)
    is_visible                    = models.BooleanField(default=True)

    def __str__(self):
        """Returns the semester year number representation of the SemYear."""
        return str(self.sem_year_num)

class Level(models.Model):
    """Represents a Level with specific attributes"""
    level_name                    = models.CharField(max_length=50,blank=True)
    is_visible                    = models.BooleanField(default=True)

    def __str__(self):
        """Returns the level name representation of the Level."""
        return self.level_name
    
#  class SyllabusInfo(models.Model):
    # university_choices = (
    #     ('un1', 'university 1'),
    #     ('un2', 'university 2'),
    #     ('un3', 'university 3'),
    #     )
    # faculty_choices = (
    #     ('fc1', 'faculty 1'),
    #     ('fc2', 'faculty 2'),
    #     ('fc3', 'faculty 3'),
    #     )

    # university_choices = models.CharField(max_length=10, choices=university_choices, blank=True)
    # faculty_choices = models.CharField(max_length=10, choices=faculty_choices, blank=True)
    # subject = models.CharField(max_length=50,blank=True)
    # marks = models.PositiveSmallIntegerField(null=True)
    # Is_shown = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.university_choices

# class CollegeInfo(models.Model):
#     university_choices = (
#         ('un1', 'university 1'),
#         ('un2', 'university 2'),
#         ('un3', 'university 3'),
#         )
#     faculty_choices = (
#         ('fc1', 'faculty 1'),
#         ('fc2', 'faculty 2'),
#         ('fc3', 'faculty 3'),
#         )

#     university_choices = models.CharField(max_length=10, choices=university_choices,default='')
#     faculty_choices = models.CharField(max_length=10, choices=faculty_choices,default='')
#     department = models.CharField(max_length=50,blank=True)
#     no_of_student = models.PositiveSmallIntegerField(null=True)
#     Is_shown = models.BooleanField(default=False)
    




    
    



    