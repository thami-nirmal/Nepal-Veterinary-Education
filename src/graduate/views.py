from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from .models import (SemYear,
                    Level,
                    MaterialContent,
                    MaterialType,
                    Subject,
                    SubContent)

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

        #Prepare the context data for redering the template
        context = {
            'selected_level_object'                    : selected_level_object,

            'selected_material_type_object'            : selected_material_type_object,

            'level_material_detail_list'               : level_material_detail_list,

            'selected_material_content'                : selected_material_content,

            'sem_year_object_list'                     : sem_year_object_list,
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

        # Prepare the context data for rendering the template
        context = {
            'graduate_details_object'                  : graduate_details_object,

            'level_material_detail_list'               : level_material_detail_list,

            'graduate_level_details_object'            : graduate_level_details_object,
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

        # Prepare the context data for rendering the template
        context = {
            'level_material_detail_list'               : level_material_detail_list,

            'sub_content_object_list'                  : sub_content_object_list,

            'sub_content_object'                       : sub_content_object,

            'selected_sub_content_level_name'          : selected_sub_content_level_name,

            'selected_sub_content_material_name'       : selected_sub_content_material_name,

            'selected_sub_content_subject_name'        : selected_sub_content_subject_name
        }

        # Render the 'graduate_chapter_content_view.html' template with provided context
        return render(request, template_name, context)


class SearchView(View):
    """
    View class for handling search requests
    """
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for searching.
        """
        
        # Check if the request was made via AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            # Get the search term from the request parameters
            search_term = request.GET.get('searchTerm')

            # Split the search term into a list of individual search terms
            search_terms_list = search_term.split(' ') if search_term else []

            # Build a dynamic query using Q objects
            query = Q()
            for search_term in search_terms_list:
                query |= (
                    Q(subject__subject_name__istartswith=search_term) |
                    Q(material_type__material_name__istartswith=search_term) |
                    Q(subject__level__level_name__istartswith=search_term) |
                    Q(subject__sem_year__sem_year_num__istartswith=search_term)
                )
                
            # Query MaterialContent objects that match the search terms
            search_results = MaterialContent.objects.filter(query)

            # Generate a list of dictionaries with relevant information from search_results
            results_list = []
            for result in search_results:
                search_item = {
                    'id'                            : result.id,
                    'has_sub_content'               : result.has_sub_content,
                    'subject'                       : result.subject.subject_name,
                    'material_type'                 : result.material_type.material_name,
                    'level'                         : result.subject.level.level_name,
                    'sem_year'                      : result.subject.sem_year.sem_year_num,
                }
                results_list.append(search_item)

            # Sort the results_list based on the number of matched search terms with each object's value
            results_list = sorted(results_list, key=lambda x: sum(any(term.lower() in str(value).lower() for term in search_terms_list) for value in x.values()), reverse=True)

            # Return the sorted results as a JSON response
            return JsonResponse({'results': results_list})

        # Return an error message for invalid requests
        return JsonResponse({'message': 'Invalid request'})