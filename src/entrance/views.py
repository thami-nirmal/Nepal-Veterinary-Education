from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import (SyllabusInfo, 
                     CollegeInfo, 
                     GK, 
                     PastQuestion, 
                     ModelQuestion)

# Create your views here.
class GkView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'gk.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        template_name     = 'gk.html'
        gk_object         = GK.objects.filter(is_shown=True)

        if gk_object.exists():
            gk_object = gk_object
        else:
            gk_object = None  

        context = {
            'gk_data_list' : gk_object,
        }

        return render(request, template_name, context)
    
class GkContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'gk_content_view.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        template_name      = 'gk_content_view.html'
        gk_details_object  = GK.objects.get(id = id)
        context = {
            'gk_details' : gk_details_object,
        }

        return render(request, template_name, context)

class PastQuestionView(View):
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
                'year' : past_question_object.year, 
                'url'  : past_question_object.pdf_url, 
                'types' : past_question_object.types
                }
            # Append the PastQuestion data dictionary to the collection list
            past_question_collection_list.append(past_question_data)
            # Return a JSON response containing the past_question_collection_list
            return JsonResponse({'data' : past_question_collection_list})
          
        # Set the template name for rendering
        template_name      = 'past_question.html'
        # Retrieve the first PastQuestion object where is_shown is True
        past_question_object  = PastQuestion.objects.filter(is_shown=True).first()
        # Retrieve all PastQuestion objects where is_shown is True
        past_question_object_list  = PastQuestion.objects.filter(is_shown=True)

        # Prepare the context data for rendering the template
        context = {
            'past_question' : past_question_object,
            'past_question_object_list' : past_question_object_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class ModelQuestionView(View):
    def get(self, request, *args, **kwargs):
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
                'name' : model_question_object.name, 
                'url'  : model_question_object.pdf_url, 
                'model_code' : model_question_object.model_code
                }
             # Append the ModelQuestion data dictionary to the collection list
            model_question_collection_list.append(model_question_data)
            # Return a JSON response containing the model_question_collection_list
            return JsonResponse({'data' : model_question_collection_list})

        # Set the template name for rendering
        template_name      = 'model_question.html'
        # Retrieve the first ModelQuestion object where is_shown is True
        model_question_object  = ModelQuestion.objects.filter(is_shown=True).first()
        # Retrieve all ModelQuestion objects where is_shown is True
        model_question_object_list  = ModelQuestion.objects.filter(is_shown=True)

        # Prepare the context data for rendering the template
        context = {
            'model_question' : model_question_object,
            'model_question_object_list' : model_question_object_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class SyllabusInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name                  = 'entrance_prep_syllabus.html'
        syllabus_info_object           = SyllabusInfo.objects.filter(is_shown=True)
        
        group = {}
        syllabus_data = []

        if syllabus_info_object.exists():
            for data in syllabus_info_object:
                if data.university_choices not in group:
                    group[data.university_choices] = {}
                if data.faculty_choices not in group[data.university_choices]:
                    group[data.university_choices][data.faculty_choices] = []
                syllabus_data = [data.subject, data.no_of_question, data.marks]
                group[data.university_choices][data.faculty_choices].append(syllabus_data)

        # print(group)
        context = {
            'syllabus_data' : syllabus_data,
            'group': group,
        }
        return render(request, template_name, context)
    

class CollegeInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name                   = 'entrance_college_info.html'
        college_info_object             = CollegeInfo.objects.filter(is_shown=True)

        group = {}
        college_data = []
        
        if college_info_object.exists():
            for data in college_info_object:
                if data.university_choices not in group:
                    group[data.university_choices] = {}
                if data.faculty_choices not in group[data.university_choices]:
                    group[data.university_choices][data.faculty_choices] = []
                college_data = [data.quota_name, data.no_of_student]
                group[data.university_choices][data.faculty_choices].append(college_data)

        context = {
            'college_data' : college_data,
            'group' : group,
        }
        return render(request, template_name, context)

