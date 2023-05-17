from django.db import models

# Create your models here.
class Entrance(models.Model):
    """
    Represents a Entrance with specific attributes
    """
    year                  = models.PositiveIntegerField(null=True)
    is_shown              = models.BooleanField(default=True)
    pdf_url               = models.URLField(max_length=200)
    is_pdf                = models.BooleanField(default=False)
    content               = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the Entrance Year representation of the Entrance.
        """
        return str(self.year)

class GK(models.Model):
    """
    Represents a GK i.e. General Knowledge with specific attributes
    """
    is_shown               = models.BooleanField(default=True)
    pdf_url                = models.URLField(max_length=200)
    is_pdf                 = models.BooleanField(default=False)
    content                = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the PDF URL for GK with specific attributes
        """
        return self.pdf_url

class SyllabusInfo(models.Model):
    """
    Represents a Syllabus Info  with specific attributes
    """
    university_choices        = (
                                 ('un1', 'university 1'),
                                 ('un2', 'university 2'),
                                 ('un3', 'university 3'),
                                )
    faculty_choices           = (
                                 ('fc1', 'faculty 1'),
                                 ('fc2', 'faculty 2'),
                                 ('fc3', 'faculty 3'),
                                )
    university_choices        = models.CharField(max_length=10, choices=university_choices, blank=True)
    faculty_choices           = models.CharField(max_length=10, choices=faculty_choices, blank=True)
    subject                   = models.CharField(max_length=50,blank=True)
    marks                     = models.PositiveSmallIntegerField(null=True)
    is_shown                  = models.BooleanField(default=True)

    def __str__(self):
        """
        :return: the University Choices  with specific attributes
        """
        return self.university_choices

class CollegeInfo(models.Model):
    """
    Represents a College Info with specific attributes
    """
    university_choices              = (
                                       ('un1', 'university 1'),
                                       ('un2', 'university 2'),
                                       ('un3', 'university 3'),
                                      )
    faculty_choices                 = (
                                       ('fc1', 'faculty 1'),
                                       ('fc2', 'faculty 2'),
                                       ('fc3', 'faculty 3'),
                                      )
    university_choices              = models.CharField(max_length=10, choices=university_choices,default='')
    faculty_choices                 = models.CharField(max_length=10, choices=faculty_choices,default='')
    department                      = models.CharField(max_length=50,blank=True)
    no_of_student                   = models.PositiveSmallIntegerField(null=True)
    is_shown                        = models.BooleanField(default=True)

    def __str__(self):
        """
        :return: the University Choices with specific attributes
        """
        return self.university_choices
    
    
    



