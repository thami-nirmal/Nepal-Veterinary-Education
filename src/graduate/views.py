from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import (SemYear,
                    Level,
                    MaterialContent,
                    MaterialType,
                    Subject,
                    SubContent)

from personal.models import Ads

from blog.models import PostViews, Post

from personal.views import LevelAndMaterialDetails

# Create your views here.

#region admin panel dropdown function
def get_sem_year_list(request,id):
    """
    : param request: The HTTP request object.
    : param id: The ID of the level.
    """
    # Create a list of dictionaries containing the semester year data
    sem_year_list = SemYear.objects.filter(level_id=id)

    # Return a JSON response with the semester year data
    return JsonResponse({'data': [{'id': sem_year.id, 'sem_year_num': sem_year.sem_year_num} for sem_year in sem_year_list]})


def get_material_type_list(request,id):
    """
    : param request: The HTTP request object.
    : param id: The ID of the level.
    """
    # Create a list of dictionaries containing the material type data
    material_type_list = MaterialType.objects.filter(level_id=id)

    # Return a JSON response with material type data
    return JsonResponse({'data': [{'id': material_type.id, 'material_name': material_type.material_name} for material_type in material_type_list]})


def get_subject_list(request,id):
    """
    : param request: The HTTP request object.
    : param id: The ID of the level.
    """
    # Create a list of dictionaries containing the subject data
    subject_list = Subject.objects.filter(level_id=id)

    # Return a JSON response with subject data
    return JsonResponse({'data': [{'id': subject.id, 'subject_name': subject.subject_name} for subject in subject_list]})
#endregion


class GraduateView(View):
    """
    View class for handling HTTP GET requests related to graduate level materials.
    It retrieves the necessary data for rendering the 'graduate.html' template,
    """
    def get(self, request ,*args, **kwargs):
        """
        Handle HTTP GET request and render the 'graduate.html' template
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered HTTP response
        """

        # Retrieves the value of the 'level_name' keyword argument from the URL parameters
        selected_level_name                            = kwargs['level_name']

        # Retrieves the value of the 'slug' keyword argument from the URL parameters
        selected_material_name                         = kwargs['slug']

        # Set the template name for rendering
        template_name                                  = 'graduate.html'

        # Create an instance of LevelAndMaterialDetails to hold level and material details
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Retrieve the selected level object based on the level name
        selected_level_object                          = Level.objects.get(slug = selected_level_name)

        # Retrieve the selected material type object based on the material name
        selected_material_type_object                  = MaterialType.objects.get(slug = selected_material_name)

        # Rretrieve the material content objects that match the selected level and materail type
        selected_material_content                      = MaterialContent.objects.filter(material_type__level = selected_level_object,material_type = selected_material_type_object)

        # Retrieve the semester
        sem_year_object_list                           = SemYear.objects.filter(is_shown=True, level=selected_level_object)

        # Retrieve the ads list
        ads_object_list                                = Ads.objects.filter(is_shown=True)

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
        other_related_post                             = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        #Prepare the context data for redering the template
        context = {
            'selected_level_object'                    : selected_level_object,

            'selected_material_type_object'            : selected_material_type_object,

            'level_material_detail_list'               : level_material_detail_list,

            'selected_material_content'                : selected_material_content,

            'sem_year_object_list'                     : sem_year_object_list,

            'ads_object_list'                          : ads_object_list,

            'popular_post'                             : popular_post,

            'other_related_post'                       : other_related_post,

            'ads_position_list'                        : ads_position_list
        }

        # Render the 'graduate.html' template with the provided context
        return render(request, template_name, context)


class GraduateContentView(View):
    """
    View class for handling HTTP GET requests related to graduate content details.
    It retrieves the necessary data for rendering the 'graduate_content_view.html' template.
    """

    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'graduate_content_view.html' template
        :param request: the HTTP request object
        :param id: the ID of the graduate content
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered HTTP response
        """

        # Set the template name for rendering
        template_name                                  = 'graduate_content_view.html'

        # Retrieve the graduate details object based on the provided 'id'
        graduate_details_object                        = MaterialContent.objects.get(id=id)

        # Retrieve the graduate level details object based on the provided id
        graduate_level_details_object                  = graduate_details_object.material_type.level.level_name

        # Create a instance of LeveAndMaterialDetails to hold level and material details
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Retrieve the ads list
        ads_object_list                                = Ads.objects.filter(is_shown=True)

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
            popular_post                               = PostViews.objects.all().order_by('-views')[:2] 
        else:
            # Retrieve the two popular post which has most of the views and haven't ads
            popular_post                               = PostViews.objects.all().order_by('-views')[:3]

        # Retrieve a list of other related post where is_published is True and order them by descending created_at, taking the latest 3 objects list
        other_related_post                             = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Prepare the context data for rendering the template
        context = {
            'graduate_details_object'                  : graduate_details_object,

            'level_material_detail_list'               : level_material_detail_list,

            'graduate_level_details_object'            : graduate_level_details_object,

            'ads_object_list'                          : ads_object_list,

            'popular_post'                             : popular_post,

            'other_related_post'                       : other_related_post,

            'ads_position_list'                        : ads_position_list
        }

        # Render the 'graduate_content_view.html' template with provided context
        return render(request, template_name, context)


class GraduateSubContentView(View):
    """
    View class for handling HTTP GET requests related to graduate sub-content.
    It retrieves the necessary data for rendering the 'graduate_sub_content_view.html' template.
    """
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'graduate_sub_content_view.html' template
        :param request: the HTTP request object
        :param id: the ID of the sub-content
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: the rendered HTTP response
        """

        # Check if the request was made via AJAX
        if request.headers.get('X-Requested-With')     == 'XMLHttpRequest':

            # Retrieve the 'id' parameter from the GET request
            id                                         = request.GET['id']    

            # Retrieve the SubContent object with the given 'id'
            sub_content_object                         = SubContent.objects.get(id = id)

            # Create a list to hold the Subcontent data
            sub_content_object_list                    = []

            # Create a dictionary with the relevant SubContent data
            sub_content_object_data                    = {

                'url'                                  : sub_content_object.pdf_URL,

                'is_pdf'                               : sub_content_object.is_pdf,

                'content'                              : sub_content_object.content

                }
            
            # Append the SubContent data dictionary to the collection list
            sub_content_object_list.append(sub_content_object_data)

            # Return a JSON response containing the sub_content_object_list
            return JsonResponse({'data' : sub_content_object_list})
        
        # Set the template name for rendering
        template_name                                  = 'graduate_sub_content_view.html'

        # Retrieve the sub-content object based on the provided ID
        sub_content_object                             = SubContent.objects.filter(material_content__id=id).first()

        # Retrieve all sub-content objects where is_shown is True and material_content matches the provided ID
        sub_content_object_list                        = SubContent.objects.filter(is_shown=True, material_content__id=id)

        # Retrieve the name of selected level, material, and subject
        selected_sub_content_level_name                = sub_content_object.material_content.material_type.level.level_name
        selected_sub_content_material_name             = sub_content_object.material_content.material_type.material_name
        selected_sub_content_subject_name              = sub_content_object.material_content.subject.subject_name

        # Create an instance of LevelAndMaterialDetails to hold level and material details
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Retrieve the ads list
        ads_object_list                                = Ads.objects.filter(is_shown=True)

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
        other_related_post                             = Post.objects.filter(is_published=True).order_by('-created_at')[:3]

        # Prepare the context data for rendering the template
        context = {
            'level_material_detail_list'               : level_material_detail_list,

            'sub_content_object_list'                  : sub_content_object_list,

            'sub_content_object'                       : sub_content_object,

            'selected_sub_content_level_name'          : selected_sub_content_level_name,

            'selected_sub_content_material_name'       : selected_sub_content_material_name,

            'selected_sub_content_subject_name'        : selected_sub_content_subject_name,

            'ads_object_list'                          : ads_object_list,

            'popular_post'                             : popular_post,

            'other_related_post'                       : other_related_post,

            'ads_position_list'                        : ads_position_list
        }

        # Render the 'graduate_chapter_content_view.html' template with provided context
        return render(request, template_name, context)

