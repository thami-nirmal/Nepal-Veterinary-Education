from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import (SyllabusInfo, 
                     CollegeInfo, 
                     GK, 
                     PastQuestion, 
                     ModelQuestion)



# Create your views here.
def LevelDetails():
    level_object_list       = Level.objects.filter(is_shown = True)
    return level_object_list


def MaterialDetails():
    material_object_list    = MaterialType.objects.filter(is_shown = True)
    return material_object_list


class GkView(View):
    """
    View class for handling HTTP GET requests related to GK.
    It renders the 'gk.html' template and passes the list of GK objects to the template context.
    """

    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'gk.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name     = 'gk.html'
        # Retrieve GK objects that are marked as shown
        gk_object         = GK.objects.filter(is_shown=True)
        # Check if GK objects exist
        if gk_object.exists():
            gk_object = gk_object
        else:
            gk_object = None  

        level_detail_list          = LevelDetails()
        material_detail_list       = MaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'gk_data_list'                : gk_object,
            'level_detail_list'           : level_detail_list,
            'material_detail_list'        : material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)
    

class GkContentView(View):
    """
    View class for handling HTTP GET requests related to GK content.
    It renders the 'gk_content_view.html' template and passes the GK details object to the template context.
    """

    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'gk_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name              = 'gk_content_view.html'
        # Retrieve the GK details object with the given 'id'
        gk_details_object          = GK.objects.get(id = id)

        level_detail_list          = LevelDetails()
        material_detail_list       = MaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'gk_details'                  : gk_details_object,
            'level_detail_list'           : level_detail_list,
            'material_detail_list'        : material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class PastQuestionView(View):
    """
    View class for handling HTTP GET requests related to past questions.
    If the request is made via AJAX, it retrieves the PastQuestion data for a specific 'id'
    and returns a JSON response containing the relevant information.
    If it is not an AJAX request, it retrieves the necessary data for rendering the 'past_question.html' template,
    including the first PastQuestion object where 'is_shown' is True and a list of all PastQuestion objects
    where 'is_shown' is True. It then renders the template with the provided context data.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'past_question.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        
        # Check if the request was made via AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
             # Retrieve the 'id' parameter from the GET request
            id = request.GET['id']    
            # Retrieve the PastQuestion object with the given 'id'
            past_question_object  = PastQuestion.objects.get(id = id)
             # Create a list to hold the PastQuestion data
            past_question_collection_list = []
            # Create a dictionary with the relevant PastQuestion data
            past_question_data = {
                'year'    : past_question_object.year, 
                'url'     : past_question_object.pdf_url, 
                'types'   : past_question_object.types
                }
            # Append the PastQuestion data dictionary to the collection list
            past_question_collection_list.append(past_question_data)
            # Return a JSON response containing the past_question_collection_list
            return JsonResponse({'data' : past_question_collection_list})
          
        # Set the template name for rendering
        template_name                = 'past_question.html'
        # Retrieve the first PastQuestion object where is_shown is True
        past_question_object         = PastQuestion.objects.filter(is_shown=True).first()
        # Retrieve all PastQuestion objects where is_shown is True
        past_question_object_list    = PastQuestion.objects.filter(is_shown=True)


        level_detail_list        = LevelDetails()
        material_detail_list     = MaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'past_question'               : past_question_object,
            'past_question_object_list'   : past_question_object_list,
            'level_detail_list'           : level_detail_list,
            'material_detail_list'        : material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class ModelQuestionView(View):
    """
    View class for handling HTTP GET requests related to model questions.
    If the request is made via AJAX, it retrieves the ModelQuestion data for a specific 'id'
    and returns a JSON response containing the relevant information.
    If it is not an AJAX request, it retrieves the necessary data for rendering the 'model_question.html' template,
    including the first ModelQuestion object where 'is_shown' is True and a list of all ModelQuestion objects
    where 'is_shown' is True. It then renders the template with the provided context data.
    """

    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'model_question.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        # Check if the request was made via AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
             # Retrieve the 'id' parameter from the GET request
            id = request.GET['id']
             # Retrieve the ModelQuestion object with the given 'id'
            model_question_object  = ModelQuestion.objects.get(id = id)
            # Create a list to hold the ModelQuestion data
            model_question_collection_list = []
            # Create a dictionary with the relevant ModelQuestion data
            model_question_data = {
                'name'         : model_question_object.name, 
                'url'          : model_question_object.pdf_url, 
                'model_code'   : model_question_object.model_code
                }
             # Append the ModelQuestion data dictionary to the collection list
            model_question_collection_list.append(model_question_data)
            # Return a JSON response containing the model_question_collection_list
            return JsonResponse({'data' : model_question_collection_list})

        # Set the template name for rendering
        template_name                 = 'model_question.html'
        # Retrieve the first ModelQuestion object where is_shown is True
        model_question_object         = ModelQuestion.objects.filter(is_shown=True).first()
        # Retrieve all ModelQuestion objects where is_shown is True
        model_question_object_list    = ModelQuestion.objects.filter(is_shown=True)

        level_detail_list        = LevelDetails()
        material_detail_list     = MaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'model_question'              : model_question_object,
            'model_question_object_list'  : model_question_object_list,
            'level_detail_list'           : level_detail_list,
            'material_detail_list'        : material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class SyllabusInfoView(View):
    """
    A Django view that retrieves syllabus information from the database and renders it to a template.
    This view fetches syllabus information objects that are marked as shown and groups them based on 
    university and faculty choices.
    The grouped data is then passed to the 'entrance_prep_syllabus.html' template, which will
    display the syllabus information in a structured format.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'entrance_prep_syllabus.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name
        template_name                  = 'entrance_prep_syllabus.html'
        # Retrieve all syllabus information objects that are marked as shown
        syllabus_info_object_list      = SyllabusInfo.objects.filter(is_shown=True)
        
        # Create an empty dictionary to group the syllabus information
        group          = {}
        # Create an empty list to store the syllabus data
        syllabus_data  = []

        # Check if any syllaus information exists
        if syllabus_info_object_list.exists():
            # iterate through each syllabus information object
            for data in syllabus_info_object_list:
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


        level_detail_list        = LevelDetails()
        material_detail_list     = MaterialDetails()

        context = {
            'syllabus_data'               : syllabus_data,
            'syllabus_info_object_list'   : syllabus_info_object_list,
            'group'                       : group,
            'level_detail_list'           : level_detail_list,
            'material_detail_list'        : material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class CollegeInfoView(View):
    """
    A Django view that retrieves college information from the database and renders it to a template.
    This view fetches syllabus information objects that are marked as shown and groups them based on 
    university and faculty choices.
    The grouped data is then passed to the 'entrance_college_info.html' template, which will
    display the syllabus information in a structured format.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'entrance_college_info.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name
        template_name                   = 'entrance_college_info.html'
        # Retrieve all college information objects that arer marked as shown
        college_info_object_list        = CollegeInfo.objects.filter(is_shown=True)

        # Create an empty dictionary to group the college information
        group           = {}
        # Create an empty list to store the college data
        college_data    = []
        
        # Check if any college information exists
        if college_info_object_list.exists():
            # Iterate through each college information object
            for data in college_info_object_list:
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

        level_detail_list        = LevelDetails()
        material_detail_list     = MaterialDetails()

        # Prepare the context dictionary to be passed to the template
        context = {
            'college_data'                : college_data,
            'college_info_object_list'    : college_info_object_list,
            'group'                       : group,
            'level_detail_list'           : level_detail_list,
            'material_detail_list'        : material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)

