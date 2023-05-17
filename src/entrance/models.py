from django.db import models

# Create your models here.
class PastQuestion(models.Model):
    """
    Represents a Past Question with specific attributes
    """
    year                  = models.PositiveIntegerField(null=True)
    is_shown              = models.BooleanField(default=True)
    pdf_url               = models.URLField(max_length=200)
    is_pdf                = models.BooleanField(default=False)
    content               = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the Year representation of the Past Question.
        """
        return str(self.year)

class GK(models.Model):
    """
    Represents a GK i.e. General Knowledge with specific attributes
    """
    name                   = models.CharField(max_length=50,blank=True)
    is_shown               = models.BooleanField(default=True)
    pdf_url                = models.URLField(max_length=200)
    is_pdf                 = models.BooleanField(default=False)
    content                = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the name of General Knowledge with specific attributes
        """
        return self.name

class ModelQuestion(models.Model):
    """
    Represents a Model Question with specific attributes
    """
    name                   = models.CharField(max_length=50,blank=True)
    is_shown               = models.BooleanField(default=True)
    pdf_url                = models.URLField(max_length=200)
    is_pdf                 = models.BooleanField(default=False)
    content                = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the name of Model Question with specific attributes
        """
        return self.name

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
    
    
    



