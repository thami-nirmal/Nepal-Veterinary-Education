from django.shortcuts import render, HttpResponse
from django.views import View
from .models import (SyllabusInfo,
                     CollegeInfo,
                     LoksewaModelQuestion,
                     LoksewaPastQuestion,
                     LoksewaNotes,
                     CouncilAct,
                     CouncilRegulation,
                     CouncilPastQuestion,
                     CouncilModelQuestion)

from personal.views import LevelAndMaterialDetails

# Create views here.

#region Syllaubus Info View
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
        template_name                   = 'post_graduate_syllabus_info.html'
        # Retrieve all syllabus information objects that are marked as shown
        syllabus_info_object_list       = SyllabusInfo.objects.filter(is_shown=True)

        # Create an empty dictionary to group the syllabus information
        group           = {}
        # Create an empty list to store the syllabus data
        syllabus_data   = []

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

        level_material_detail_list          = LevelAndMaterialDetails()

        # Prepare the context dictioanry to be passed to the template
        context = {
            'syllabus_data'                : syllabus_data,
            'syllabus_info_object_list'    : syllabus_info_object_list,
            'group'                        : group,
            'level_material_detail_list'   : level_material_detail_list,
        }

        # Render the template with the provided context
        return render(request, template_name, context)
    
#endregion

#region College Info View
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
        template_name                    = 'post_graduate_college_info.html'
        # Retrieve all college information objects that arer marked as shown
        college_info_object_list         = CollegeInfo.objects.filter(is_shown=True)

        # Create an empty dictionary to group the college information
        group          = {}
        # Create an empty list to store the college data
        college_data   = []

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

        level_material_detail_list          = LevelAndMaterialDetails()

        # Prepare the context dictionary to be passed to the template
        context = {
            'college_data'                : college_data,
            'college_info_object_list'    : college_info_object_list,
            'group'                       : group,
            'level_material_detail_list'  : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)
    
#endregion

#region Loksewa View
class LoksewaView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'loksewa.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name     = 'loksewa.html'

        loksewa_model_question_object_list          = LoksewaModelQuestion.objects.filter(is_shown=True)
        loksewa_past_question_object_list           = LoksewaPastQuestion.objects.filter(is_shown=True)
        loksewa_notes_object_list                   = LoksewaNotes.objects.filter(is_shown=True)


        level_material_detail_list                  = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'loksewa_model_question_object_list'    : loksewa_model_question_object_list,
            'loksewa_past_question_object_list'     : loksewa_past_question_object_list,
            'loksewa_notes_object_list'             : loksewa_notes_object_list,
            'level_material_detail_list'            : level_material_detail_list  
        }

        # Render the template with the provided context
        return render(request, template_name, context)
    
#endregion

#region Loksewa Past Question Content View
class LoksewaPastQuestionContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'loksewa_past_question_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name                         = 'loksewa_past_question_content_view.html'
        loksewa_past_question_object          = LoksewaPastQuestion.objects.get(id = id)

        level_material_detail_list          = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'loksewa_past_question_object'    : loksewa_past_question_object,
            'level_material_detail_list'      : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)
    
#endregion

#region Loksewa Model Question Content View
class LoksewaModelQuestionContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'loksewa_model_question_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name                          = 'loksewa_model_question_content_view.html'
        loksewa_model_question_object          = LoksewaModelQuestion.objects.get(id = id)

        level_material_detail_list             = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'loksewa_model_question_object'    : loksewa_model_question_object,
            'level_material_detail_list'       : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)
#endregion  

#region Loksewa Notes Content View
class LoksewaNotesContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'loksewa_notes_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name                 = 'loksewa_notes_content_view.html'
        loksewa_notes_object          = LoksewaNotes.objects.get(id = id)

        level_material_detail_list          = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'loksewa_notes_object'            : loksewa_notes_object,
            'level_material_detail_list'      : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)

#endregion

#region Council View
class CouncilView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'council.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name     = 'council.html'

        council_act_object_list                     = CouncilAct.objects.filter(is_shown=True)
        council_regulation_object_list              = CouncilRegulation.objects.filter(is_shown=True)
        council_past_question_object_list           = CouncilPastQuestion.objects.filter(is_shown=True)
        council_model_question_object_list          = CouncilModelQuestion.objects.filter(is_shown=True)

        level_material_detail_list                  = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'council_act_object_list'                : council_act_object_list,
            'council_regulation_object_list'         : council_regulation_object_list,
            'council_past_question_object_list'      : council_past_question_object_list,
            'council_model_question_object_list'     : council_model_question_object_list,
            'level_material_detail_list'             : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)

#endregion

#region Council Act Content View
class CouncilActContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'council_act_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name                 = 'council_act_content_view.html'
        council_act_object            = CouncilAct.objects.get(id = id)

        level_material_detail_list    = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'council_act_object'              : council_act_object,
            'level_material_detail_list'      : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)

#endregion 

#region Council Regulation Content View
class CouncilRegulationContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'council_regulation_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name                        = 'council_regulation_content_view.html'
        council_regulation_object            = CouncilRegulation.objects.get(id = id)

        level_material_detail_list           = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'council_regulation_object'       : council_regulation_object,
            'level_material_detail_list'      : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)

#endregion

#region Council Past Question Content VIew
class CouncilPastQuestionContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'council_past_question_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name                          = 'council_past_question_content_view.html'
        council_past_question_object           = CouncilPastQuestion.objects.get(id = id)

        level_material_detail_list             = LevelAndMaterialDetails()
        # Prepare the context data for rendering the template
        context = {
            'council_past_question_object'     : council_past_question_object,
            'level_material_detail_list'       : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)

#endregion

#region Council Model Question Content View
class CouncilModelQuestionContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'council_model_question_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name                          = 'council_model_question_content_view.html'
        council_model_question_object          = CouncilModelQuestion.objects.get(id = id)

        level_material_detail_list             = LevelAndMaterialDetails()
        # Prepare the context data for rendering the template
        context = {
            'council_model_question_object'    : council_model_question_object,
            'level_material_detail_list'       : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)

#endregion