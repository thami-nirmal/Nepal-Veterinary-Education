from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import (SyllabusInfo, 
                    CollegeInfo, 
                    GK, 
                    PastQuestion, 
                    ModelQuestion)
from personal.models import Ads
from blog.models import PostViews, Post

from personal.views import LevelAndMaterialDetails
from django.core.paginator import Paginator
# Create your views here.

#region GK View
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
        template_name             = 'gk.html'

        # Retrieve GK objects that are marked as shown
        gk_object_list            = GK.objects.filter(is_shown=True).order_by('-id')

        # Pagination settings
        items_per_page            = 4

        # Create Paginator object
        paginator                 = Paginator(gk_object_list, items_per_page)

        # Get the current page number from the request's GET paramerters
        page_number               = request.GET.get('page')

        # Get the page gk page object  for the requested page number
        gk_page_obj               = paginator.get_page(page_number)

        # Retrieve the ads list
        ads_object_list           = Ads.objects.filter(is_shown=True)

        # Retrieve the 'position' values from the ads_object_list and store them in ads_object_position_list
        ads_object_position_list              = ads_object_list.values_list('position')

        # Create an empty list called ads_position_list to store 'position' values
        ads_position_list =[]

        # Loop through each item in ads_object_position_list
        for item in ads_object_position_list:
            # Append the first element (position) of each item to the ads_position_list
            ads_position_list.append(item[0])

        # Check if '6' is in the ads_position_list
        if '6' in ads_position_list:
            # Retrieve the two popular post which has most of the views and have the ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:2]
        else:
            # Retrieve the two popular post which has most of the views and haven't ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:3]

        # Retrieve a list of other related post where is_published is True and order them by descending created_at, taking the latest 3 objects list
        other_related_post                  = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list          = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {

        'level_material_detail_list'      : level_material_detail_list,

        'gk_page_obj'                     : gk_page_obj,

        'items_per_page'                  : items_per_page,

        'gk_object_list'                  : gk_object_list,

        'ads_object_list'                 : ads_object_list,

        'popular_post'                    : popular_post,

        'other_related_post'              : other_related_post,

        'ads_position_list'               : ads_position_list
    }

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
        template_name                         = 'gk_content_view.html'

        # Retrieve the GK details object with the given 'id'
        gk_details_object                     = GK.objects.get(id = id)

        # Retrieve the ads list
        ads_object_list                       = Ads.objects.filter(is_shown=True)

        # Retrieve the 'position' values from the ads_object_list and store them in ads_object_position_list
        ads_object_position_list              = ads_object_list.values_list('position')

        # Create an empty list called ads_position_list to store 'position' values
        ads_position_list =[]

        # Loop through each item in ads_object_position_list
        for item in ads_object_position_list:
            # Append the first element (position) of each item to the ads_position_list
            ads_position_list.append(item[0])

        # Check if '6' is in the ads_position_list
        if '6' in ads_position_list:
            # Retrieve the two popular post which has most of the views and have the ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:2]
        else:
            # Retrieve the two popular post which has most of the views and haven't ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:3]

        # Retrieve a list of other related post where is_published is True and order them by descending created_at, taking the latest 3 objects list
        other_related_post                  = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list          = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'gk_details'                      : gk_details_object,

            'level_material_detail_list'      : level_material_detail_list,

            'ads_object_list'                 : ads_object_list,

            'popular_post'                    : popular_post,

            'other_related_post'              : other_related_post,

            'ads_position_list'               : ads_position_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)
#endregion


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
            past_question_object  = PastQuestion.objects.get(id = id, is_shown=True)
            
            # Create a list to hold the PastQuestion data
            past_question_collection_list = []

            # Create a dictionary with the relevant PastQuestion data
            past_question_data = {
                'year'          : past_question_object.year, 

                'url'           : past_question_object.pdf_url, 

                'content'       : past_question_object.content,

                'types'         : past_question_object.types,

                'is_pdf'        : past_question_object.is_pdf,

                }   
            
            # Append the PastQuestion data dictionary to the collection list
            past_question_collection_list.append(past_question_data) 

            # Return a JSON response containing the past_question_collection_list
            return JsonResponse({'data' : past_question_collection_list})
        
        # Set the template name for rendering
        template_name                            = 'past_question.html'

        # Retrieve the first PastQuestion object where is_shown is True
        past_question_object                     = PastQuestion.objects.filter(is_shown=True).first()

        # Retrieve all PastQuestion objects where is_shown is True
        past_question_object_list                = PastQuestion.objects.filter(is_shown=True)

        # Retrieve the ads list
        ads_object_list                          = Ads.objects.filter(is_shown=True)

        # Retrieve the 'position' values from the ads_object_list and store them in ads_object_position_list
        ads_object_position_list              = ads_object_list.values_list('position')

        # Create an empty list called ads_position_list to store 'position' values
        ads_position_list =[]

        # Loop through each item in ads_object_position_list
        for item in ads_object_position_list:
            # Append the first element (position) of each item to the ads_position_list
            ads_position_list.append(item[0])

        # Check if '6' is in the ads_position_list
        if '6' in ads_position_list:
            # Retrieve the two popular post which has most of the views and have the ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:2]
        else:
            # Retrieve the two popular post which has most of the views and haven't ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:3]

        # Retrieve a list of other related post where is_published is True and order them by descending created_at, taking the latest 3 objects list
        other_related_post                       = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list               = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'past_question'                      : past_question_object,

            'past_question_object_list'          : past_question_object_list,

            'level_material_detail_list'         : level_material_detail_list,

            'ads_object_list'                    : ads_object_list,

            'popular_post'                       : popular_post,

            'other_related_post'                 : other_related_post,

            'ads_position_list'                  : ads_position_list
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

                'model_code'   : model_question_object.model_code,

                'content'      : model_question_object.content,

                'is_pdf'       : model_question_object.is_pdf
                }
            
            # Append the ModelQuestion data dictionary to the collection list
            model_question_collection_list.append(model_question_data)

            # Return a JSON response containing the model_question_collection_list
            return JsonResponse({'data' : model_question_collection_list})

        # Set the template name for rendering
        template_name                         = 'model_question.html'

        selected_id = request.GET.get('id')
        if selected_id :
            model_question_object               =ModelQuestion.objects.filter(is_shown=True,id=selected_id)
            print(model_question_object, "FROM SEARCHING")
        else:
            # Retrieve the first ModelQuestion object where is_shown is True
            model_question_object               = ModelQuestion.objects.filter(is_shown=True).first()
            print(model_question_object)

        # Retrieve all ModelQuestion objects where is_shown is True
        model_question_object_list              = ModelQuestion.objects.filter(is_shown=True)

        # Retrieve the ads list
        ads_object_list                         = Ads.objects.filter(is_shown=True)

        # Retrieve the 'position' values from the ads_object_list and store them in ads_object_position_list
        ads_object_position_list                = ads_object_list.values_list('position')

        # Create an empty list called ads_position_list to store 'position' values
        ads_position_list =[]

        # Loop through each item in ads_object_position_list
        for item in ads_object_position_list:
            # Append the first element (position) of each item to the ads_position_list
            ads_position_list.append(item[0])

        # Check if '6' is in the ads_position_list
        if '6' in ads_position_list:
            # Retrieve the two popular post which has most of the views and have the ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:2]
        else:
            # Retrieve the two popular post which has most of the views and haven't ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:3]

        # Retrieve a list of other related post where is_published is True and order them by descending created_at, taking the latest 3 objects list
        other_related_post                        = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'model_question'                  : model_question_object,

            'model_question_object_list'      : model_question_object_list,

            'level_material_detail_list'      : level_material_detail_list,

            'ads_object_list'                 : ads_object_list,

            'popular_post'                    : popular_post,

            'other_related_post'              : other_related_post,

            'ads_position_list'               : ads_position_list,

            'selected_id'                     : selected_id
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

        # Retrieve the ads list
        ads_object_list                     = Ads.objects.filter(is_shown=True)

        # Retrieve the 'position' values from the ads_object_list and store them in ads_object_position_list
        ads_object_position_list              = ads_object_list.values_list('position')

        # Create an empty list called ads_position_list to store 'position' values
        ads_position_list =[]

        # Loop through each item in ads_object_position_list
        for item in ads_object_position_list:
            # Append the first element (position) of each item to the ads_position_list
            ads_position_list.append(item[0])

        # Check if '6' is in the ads_position_list
        if '6' in ads_position_list:
            # Retrieve the two popular post which has most of the views and have the ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:2]
        else:
            # Retrieve the two popular post which has most of the views and haven't ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:3]

        # Retrieve a list of other related post where is_published is True and order them by descending created_at, taking the latest 3 objects list
        other_related_post                  = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list          = LevelAndMaterialDetails()

        context = {
            'syllabus_data'                 : syllabus_data,

            'syllabus_info_object_list'     : syllabus_info_object_list,
            
            'group'                         : group,

            'level_material_detail_list'    : level_material_detail_list,

            'ads_object_list'               : ads_object_list,

            'popular_post'                  : popular_post,

            'other_related_post'            : other_related_post,
            
            'ads_position_list'             : ads_position_list
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

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list          = LevelAndMaterialDetails()

        # Retrieve the ads list
        ads_object_list                     = Ads.objects.filter(is_shown=True)

        # Retrieve the 'position' values from the ads_object_list and store them in ads_object_position_list
        ads_object_position_list              = ads_object_list.values_list('position')

        # Create an empty list called ads_position_list to store 'position' values
        ads_position_list =[]

        # Loop through each item in ads_object_position_list
        for item in ads_object_position_list:
            # Append the first element (position) of each item to the ads_position_list
            ads_position_list.append(item[0])

        # Check if '6' is in the ads_position_list
        if '6' in ads_position_list:
            # Retrieve the two popular post which has most of the views and have the ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:2]
        else:
            # Retrieve the two popular post which has most of the views and haven't ads
            popular_post                          = PostViews.objects.all().order_by('-views')[:3]

        # Retrieve a list of other related post where is_published is True and order them by descending created_at, taking the latest 3 objects list
        other_related_post                  = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Prepare the context dictionary to be passed to the template
        context = {
            'college_data'                    : college_data,

            'college_info_object_list'        : college_info_object_list,
            
            'group'                           : group,

            'level_material_detail_list'      : level_material_detail_list,

            'ads_object_list'                 : ads_object_list,

            'popular_post'                    : popular_post,

            'other_related_post'              : other_related_post,

            'ads_position_list'               : ads_position_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)

