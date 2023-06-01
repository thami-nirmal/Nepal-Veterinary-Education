from django.shortcuts import render, HttpResponse
from django.views import View
from .models import (SyllabusInfo,
                     CollegeInfo)

# Create your views here.
class SyllabusInfoView(View):
    """
    A Django view that retrieves syllabus information from the database and renders it to a template.
    This view fetches syllabus information objects that are marked as shown and groups them based on 
    university and faculty choices.
    
    The grouped data is then passed to the 'post_graduate_syllabus_info.html' template, which will
    display the syllabus information in a structured format.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'post_graduate_syllabus_info.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name
        template_name              = 'post_graduate_syllabus_info.html'
        # Retrieve all syllabus information objects that are marked as shown
        syllabus_info_object       = SyllabusInfo.objects.filter(is_shown=True)

        # Create an empty dictionary to group the syllabus information
        group = {}
        # Create an empty list to store the syllabus data
        syllabus_data = []

        # Check if any syllaus information exists
        if syllabus_info_object.exists():
            # iterate through each syllabus information object
            for data in syllabus_info_object:
                # Check if the university choice exists as a key in the group dictionary
                if data.university_choices not in group:
                    # Create an empty dictionary for the university choice
                    group[data.university_choices] = {}
                # Check if the faculty choice exists as a key in the group dictionary under the university choice
                if data.faculty_choices not in group[data.university_choices]:
                    # Create an empty list for the faculty choice
                    group[data.university_choices][data.faculty_choices] = []
                # Create a list with the syllabus data
                syllabus_data = [data.subject, data.no_of_question, data.marks]
                # append the syllabus data to the appropriate group in the dictionary
                group[data.university_choices][data.faculty_choices].append(syllabus_data)

        # Prepare the context dictioanry to be passed to the template
        context = {
            'syllabus_data' : syllabus_data,
            'group' : group,
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class CollegeInfoView(View):
    """
    A Django view that retrieves college information from the database and renders it to a template.
    This view fetches syllabus information objects that are marked as shown and groups them based on 
    university and faculty choices.

    The grouped data is then passed to the 'post_graduate_college_info.html' template, which will
    display the syllabus information in a structured format.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'post_graduate_syllabus_info.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name
        template_name               = 'post_graduate_college_info.html'
        # Retrieve all college information objects that arer marked as shown
        college_info_object         = CollegeInfo.objects.filter(is_shown=True)

        # Create an empty dictionary to group the college information
        group = {}
        # Create an empty list to store the college data
        college_data = []

        # Check if any college information exists
        if college_info_object.exists():
            # Iterate through each college information object
            for data in college_info_object:
                # Check if the university choice exists as a key in the group dictionary
                if data.university_choices not in group:
                    # Create an empty dictionary for the university choice
                    group[data.university_choices] = {}
                # Check if the faculty choice exists as a key in the group dictionary under the university choice
                if data.faculty_choices not in group[data.university_choices]:
                    # Create an empty list for the faculty choice
                    group[data.university_choices][data.faculty_choices] = []
                 # Create a list with the college data
                college_data = [data.quota_name, data.no_of_student]
                # append the college data to the appropriate group in the dictionary
                group[data.university_choices][data.faculty_choices].append(college_data)

        # Prepare the context dictionary to be passed to the template
        context = {
            'college_data' : college_data,
            'group' : group,
        }

        # Render the template with the provided context
        return render(request, template_name, context)




