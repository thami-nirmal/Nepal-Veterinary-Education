from django.db import models

# Create your models here.
class CouncilAct(models.Model):
    """
    Represents council act with specific attributes.
    """
    name                = models.CharField(max_length=50,blank=True)
    pdf_url             = models.URLField(max_length=200)
    is_shown            = models.BooleanField(default=True)

    def __str__(self):
        """
        :return: the name of council act representation of CouncilAct
        """
        return self.name

class CouncilRegulation(models.Model):
    """
    Represents council regulation with specific attributes
    """
    name                = models.CharField(max_length=50, blank=True)
    pdf_url             = models.URLField(max_length=200)
    is_shown            = models.BooleanField(default=True)

    def __str__(self):
        """
        :return: the name of council regulation representation of CouncilRegulation
        """
        return self.name
    
class CouncilModelQuestion(models.Model):
    """
    Represents council model question with specific attributes
    """
    is_shown            = models.BooleanField(default=True)
    pdf_url             = models.URLField(max_length=200)
    is_pdf              = models.BooleanField(default=False)
    content             = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the pdf url of council model question representation of CouncilModelQuestion
        """
        return self.pdf_url

class LoksewaModelQuestion(models.Model):
    """
    Represents loksewa model question with specific attributes
    """
    is_shown            = models.BooleanField(default=True)
    pdf_url             = models.URLField(max_length=200)
    is_pdf              = models.BooleanField(default=False)
    content             = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the pdf url of loksewa model question representation of LoksewaModelQuestion
        """
        return self.pdf_url

class CouncilPastQuestion(models.Model):
    """
    Represents council past question with specific attributes
    """
    is_shown            = models.BooleanField(default=True)
    year                = models.PositiveIntegerField(null=True)
    pdf_url             = models.URLField(max_length=200)
    is_pdf              = models.BooleanField(default=False)
    content             = models.CharField(max_length=300,blank=True)
    
    def __str__(self):
        """
        :return: the year of council past question representation of CouncilPastQuestion
        """
        return str(self.year)

class LoksewaPastQuestion(models.Model):
    """
    Represents loksewa past question with specific attributes
    """
    is_shown           = models.BooleanField(default=True)
    year               = models.PositiveIntegerField(null=True)
    pdf_url            = models.URLField(max_length=200)
    is_pdf             = models.BooleanField(default=False)
    content            = models.CharField(max_length=300,blank=True)
    
    def __str__(self):
        """
        :return: the year of loksewa past question representation of LoksewaPastQuestion
        """
        return str(self.year)

class LoksewaNotes(models.Model):
    """
    Represents loksewa notes with specific attributes
    """
    is_shown           = models.BooleanField(default=True)
    pdf_url            = models.URLField(max_length=200)
    is_pdf             = models.BooleanField(default=False)
    content            = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """
        :return: the pdf url of loksewa notes representation of LoksewaNotes
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
        :return: the University Choices representation of SyllabusInfo.
        """
        return self.university_choices

class CollegeInfo(models.Model):
    """
    Represents a College Info with specific attributes.
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
        :return: the University Choices representation of CollegeInfo.
        """
        return self.university_choices



    