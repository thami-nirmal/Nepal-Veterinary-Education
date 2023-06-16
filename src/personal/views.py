from django.shortcuts import render
from django.views import View
from graduate.models import Level, MaterialType
from .models import KrishiDiarys, UsefulLinks, Experts, DrugIndex, NewsAndNotice
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

        # Retrieve a list of useful links objects where is_shown is True
        useful_links_data_list                         = UsefulLinks.objects.filter(is_shown=True).order_by('-id')

        # Pagination settings
        iterms_per_page                                = 8

        # Create Paginator object
        paginator                                      = Paginator(useful_links_data_list, iterms_per_page)

        # Get the current page number from the request's GET parameters
        page_number                                    = request.GET.get('page')

        # Get the page object for the request page number
        useful_links_page_obj                          = paginator.get_page(page_number)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'               : level_material_detail_list,

            'useful_links_page_obj'                    : useful_links_page_obj 
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)
#endregion


#region News and Notice View
class NewsNoticeView(View):
    """
    View class for handling HTTP GET requests related to the news notice page.
    It retrieves the necessary data for rendering the 'news_notice.html' template.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'news_notice.html' template.
        
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        # Specify the template to be rendered
        template_name                                  = 'news_notice.html'

        news_notice_object_list                        = NewsAndNotice.objects.filter(is_shown=True).order_by('-id')

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Pagination settings
        news_notice_items_per_page                     = 3

        # Create Paginator object
        news_notice_paginator                          = Paginator(news_notice_object_list, news_notice_items_per_page)

        # Get the current page number of news and notice from the request's GET parameters
        news_notice_current_page_number                = request.GET.get('page')

        # Get teh page object for the requested page number
        news_notice_page_obj                           = news_notice_paginator.get_page(news_notice_current_page_number)

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'               : level_material_detail_list,

            'news_notice_page_obj'                     : news_notice_page_obj,
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

        # Pagination settings
        items_per_page                                    = 4

        # Create Paginator object
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


#region Experts View
class ExpertsView(View):
    """
    View class for handling HTTP GET requests related to the experts page.
    It retrieves the necessary data for rendering the 'experts.html' template.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'experts.html' template.
        
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """
        # Set the template
        template_name                                  = 'experts.html'

        # Retrieve a list of Experts objects where is_shown is True and order them by descending ID
        experts_object_list                            = Experts.objects.filter(is_shown=True).order_by('-id')

        # Pagination settings
        items_per_page                                 = 6

        # Create Paginator object
        paginator                                      = Paginator(experts_object_list, items_per_page)

        # Get the current page number fom the request's GET parameters
        page_number                                    = request.GET.get('page')

        # Get the page object for the requested page number
        experts_page_obj                               = paginator.get_page(page_number)
        # print(experts_page_obj)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'               : level_material_detail_list,

            'experts_page_obj'                         : experts_page_obj,

            'experts_object_list'                      : experts_object_list,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)
#endregion


#region Drug Index View
class DrugIndexView(View):
    """
    View class for handling HTTP GET requests related to the drug index page.
    It retrieves the necessary data for rendering the 'drug_index.html' template.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'drug_index.html' template.
        
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        # Set the template name
        template_name                                       = 'drug_index.html'

        # Reterieve the list of drug index objects where is_shown is True
        drug_index_obj_list                                 = DrugIndex.objects.filter(is_shown=True).order_by('-id')

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                          = LevelAndMaterialDetails()

        # Pagination settings
        items_per_page                                      = 4

        # Create Paginator object
        paginator  = Paginator(drug_index_obj_list, items_per_page)

        # Get the current page number from the request's GET parameters
        page_number                                         = request.GET.get('page')

        # Get the Page object for the requested page number
        drug_index_page_obj                                 = paginator.get_page(page_number)

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'                    : level_material_detail_list,

            'drug_index_page_obj'                           : drug_index_page_obj,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)
#endregion


# region Drug Index Content View
class DrugIndexContentView(View):
    """
    View class for handling HTTP GET requests related to the drug index content page.
    It retrieves the necessary data for rendering the 'drug_index_content.html' template.
    """
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'drug_index_content.html' template.
        
        :param request: The HTTP request object.
        :param id: The ID of the drug index object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: The rendered HTTP response.
        """

        # Set the template name
        template_name                                           = 'drug_index_content.html'

        # Retrieve the Drug Index object with the given Id
        drug_index_object                                       = DrugIndex.objects.get(id=id)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                              = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'drug_index_object'                                 : drug_index_object,

            'level_material_detail_list'                        : level_material_detail_list,

        }

        # Render the template with the provided context
        return render(request, template_name, context)
#endregion    


