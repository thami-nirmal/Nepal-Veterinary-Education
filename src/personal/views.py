from django.shortcuts import render
from django.views import View
from graduate.models import Level, MaterialType
from .models import KrishiDiarys
from django.core.paginator import Paginator

# Create your views here.

# region Level and Material Details Function
# This function retrieves the level and material details for displaying in a navigation bar.
def LevelAndMaterialDetails():
    # Retrieve a list of Level objects where is_shown is True
    level_object_list                                  = Level.objects.filter(is_shown = True)

    # Retrieve a list of MaterialType objects where is_shown is True
    material_object_list                               = MaterialType.objects.filter(is_shown = True)

    # Create dictionary to store the level and material data
    level_material = {
        'level_object_list'                            : level_object_list,

        'material_object_list'                         : material_object_list,
    }

    # Return the level and material data as a dictionary
    return level_material
# endregion


#region Home View
class HomeView(View):
    """
    View class for handling HTTP GET requests related to the home page.
    It retrieves the necessary data for rendering the 'index.html' template.
    """
    def get(self, request,*args,**kwargs):
        """
        Handle HTTP GET request and render the 'index.html' template.
        
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        # Specify the template to be rendered
        template_name                                   = 'index.html'

        # Retrieve a list of KrishiDiarys objects where is_shown is True and order them by descending ID, taking the latest 5 objects
        krishi_diary_details                            = KrishiDiarys.objects.filter(is_shown=True).order_by('-id')[:5]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                      = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'                : level_material_detail_list,

            'krishi_diary_details'                      : krishi_diary_details,
        }

        # Render the template with specified context and return the rendered response
        return render(request, template_name, context)
#endregion


#region Useful Links View
class UsefulLinksView(View):
    """
    View class for handling HTTP GET requests related to the useful links page.
    It retrieves the necessary data for rendering the 'useful_links.html' template.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'useful_links.html' template.
        
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        # Specify the template to be rendered
        template_name                                  = 'useful_links.html'

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'               : level_material_detail_list, 
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)
#endregion


#region News Notice View
class NewsNoticeView(View):
    """
    View class for handling HTTP GET requests related to the news notice page.
    It retrieves the necessary data for rendering the 'news_notice_syllabus.html' template.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'news_notice_syllabus.html' template.
        
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        # Specify the template to be rendered
        template_name                                  = 'news_notice_syllabus.html'

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'               : level_material_detail_list, 
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)
#endregion


#region Krishi Diarys View
class KrishiDiarysView(View):
    """
    View class for handling HTTP GET requests related to the krishi diarys page.
    It retrieves the necessary data for rendering the 'krishi_diarys.html' template.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'krishi_diarys.html' template.
        
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        # Specify the template to be rendered
        template_name                                     = 'krishi_diarys.html'

        # Retrieve a list of KrishiDiarys objects where is_shown is True and order them by descending ID
        krishi_diarys_details_list                        = KrishiDiarys.objects.filter(is_shown=True).order_by('-id')

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                        = LevelAndMaterialDetails()

        # Pagination setttings
        items_per_page                                    = 8

        # Creae Paginator object
        paginator = Paginator(krishi_diarys_details_list, items_per_page)

        # Get the currrent page number from the request's GET parameters
        page_number                                       = request.GET.get('page')

        # Get the Page object for the requested page number
        page_obj                                          = paginator.get_page(page_number)

        # Create a context dictionary to store the data to be passed to the template
        context   = {
            'level_material_detail_list'                  : level_material_detail_list,

            'page_obj'                                    : page_obj,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)
#endregion


#region Krishi Diarys Content View
class KrishiDiarysContentView(View):
    """
    View class for handling HTTP GET requests related to the krishi diarys content page.
    It retrieves the necessary data for rendering the 'krishi_diarys_content_view.html' template.
    """
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'krishi_diarys_content_view.html' template.
        
        :param request: The HTTP request object.
        :param id: The ID of the krishi diary object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        #Specify the template to be rendered
        template_name                                     = 'krishi_diarys_content_view.html'

        # Retrieve the KrishiDiarys object with the specified ID
        krishi_diarys_object                              = KrishiDiarys.objects.get(id = id)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                        = LevelAndMaterialDetails()
        
        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'                  : level_material_detail_list,

            'krishi_diarys_object'                        : krishi_diarys_object,
        }
        
        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)
#endregion