from django.shortcuts import render, redirect
from django.views import View
from graduate.models import Level, MaterialType
from .models import (KrishiDiarys,
                    UsefulLinks,
                    Experts,
                    DrugIndex,
                    NewsAndNotice,
                    NewsLetter,
                    CustomerFeedback)
from blog.models import Post

from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import resolve
from django.http import JsonResponse

from graduate.models import MaterialContent
from post_graduate.models import (LoksewaNotes, 
                                LoksewaPastQuestion,
                                LoksewaModelQuestion,
                                CouncilAct,
                                CouncilRegulation,
                                CouncilPastQuestion,
                                CouncilModelQuestion)
from entrance.models import GK
from blog.models import Post

from django.db.models import Q
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

        # Retrieve a list of News and Notice objects where is_shown is True and order them by descending Id, taking the latest 4 objects list
        news_notice_object_list                         = NewsAndNotice.objects.filter(is_shown=True).order_by('-id')[:4]

        # retrieve a list of blog post objects where is_published is True and order them by descending created_at, taking the latest 2 objects list
        blog_post_object_list1                          = Post.objects.filter(is_published=True).order_by('-created_at')[:2]

        # retrieve a list of blog post objects where is_published is True and order them by descending created_at, taking the second latest 2 objects list
        blog_post_object_list2                          = Post.objects.filter(is_published=True).order_by('-created_at')[2:4]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                      = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'                : level_material_detail_list,

            'krishi_diary_details'                      : krishi_diary_details,

            'news_notice_object_list'                   : news_notice_object_list,

            'blog_post_object_list1'                    : blog_post_object_list1,

            'blog_post_object_list2'                    : blog_post_object_list2
        }

        # Render the template with specified context and return the rendered response
        return render(request, template_name, context)


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
        items_per_page                                = 8

        # Create Paginator object
        paginator                                      = Paginator(useful_links_data_list, items_per_page)

        # Get the current page number from the request's GET parameters
        page_number                                    = request.GET.get('page')

        # Get the page object for the request page number
        useful_links_page_obj                          = paginator.get_page(page_number)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'               : level_material_detail_list,

            'useful_links_page_obj'                    : useful_links_page_obj,

            'items_per_page'                           : items_per_page,

            'useful_links_data_list'                   : useful_links_data_list,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)


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

            'news_notice_object_list'                  : news_notice_object_list,

            'news_notice_items_per_page'               : news_notice_items_per_page,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)


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

            'krishi_diarys_details_list'                  : krishi_diarys_details_list,

            'items_per_page'                              : items_per_page,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)


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

            'items_per_page'                           : items_per_page,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)


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

            'drug_index_obj_list'                           : drug_index_obj_list,

            'items_per_page'                                : items_per_page,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)


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


class NewsLetterView(View):
    """
    View class for handling newsletter subscription.
    """
    def post(self, request, *args, **kwargs):
        """
        Process the newsletter subscription request when the form is submitted.
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: default response.
        """
        # Check if the request was made via AJAX
        if request.headers.get('X-Requested-With')  == 'XMLHttpRequest':
            # Get the email from the request
            email        = request.POST['email']

            if email:
                # If the email does not exist in the NewsLetter model
                if not NewsLetter.objects.filter(email=email).exists():
                    # Create a new NewsLetter object with the email and subscribe status
                    newsletter = NewsLetter(email=email, subscribe=True)
                    # Save the newsletter object to the database
                    newsletter.save()
                # Display a success message to the user
                messages.success(request,'Successfully subscribed')
                # Return a success response
                return JsonResponse({'status': 'success'})
        # Return a default response
        return True


        # # Retrieve the value of the 'email' field from the form's POST data
        # email = request.POST.get('email')
        # # Get the current page URL dynamically
        # url_name  = request.POST.get('url_name')
        # print(url_name)
        # # Check if the 'email' value is not empty
        # if email:
        #     # If the email does not exist in the NewsLetter model
        #     if not NewsLetter.objects.filter(email=email).exists():
        #         # Create a new NewsLetter object with the email and subscribe status
        #         newsletter = NewsLetter(email=email, subscribe=True)
        #         # Save the newsletter object to the database
        #         newsletter.save()
        #     # Display a success message to the user
        #     messages.success(request,'Successfully subscribed')

        # # Get the current page URL name dynamically
        # return redirect(url_name)


class CustomerFeedbackView(View):
    """
    View class for handling HTTP GET requests related to the customer feedback page.
    It rendering the 'customer_feedback.html' template.
    """
    def get(self, request, *args, **kwargs):

        # Set the template
        template_name  = 'customer_feedback.html'

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list                     = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {
            'level_material_detail_list'               : level_material_detail_list,
        }

        # Render the template with the specified context and return the rendered response
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Handle the POST request to submit customer feedback.
        :param request: The HTTP request object.
        :param args: Additional positional arguments.
        :param kwargs: Additional keyword arguments.
        :return: Default response.
        """
        
        # Retrieve the value of the customer feedback form's POST data
        if request.method         == 'POST':
            first_name             = request.POST.get('firstname')
            last_name              = request.POST.get('lastname')
            email                  = request.POST.get('Email')
            message                = request.POST.get('message')

            # Create a new CustomerFeedback object with the retrieved values and assign it to the variable customer_feedback
            # customer_feedback  = CustomerFeedback(first_name=first_name, last_name=last_name, email=email, message=message)

            # # Save the customer feedback object to the database
            # customer_feedback.save()

            # Create a new CustomerFeedback object and save it to the database
            CustomerFeedback.objects.create(
                first_name           = first_name,
                last_name            = last_name,
                email                = email,
                message              = message
            )

            # Redirect the user to the 'customer_feedback' page after successfully submitting the feedback.
            return redirect('customer_feedback')


def MaterialContentSearch(material_content_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in material_content_search_data:
        query |= (
            Q(subject__subject_name__icontains=search_term) |
            Q(material_type__material_name__icontains=search_term) |
            Q(subject__level__level_name__icontains=search_term) |
            Q(subject__sem_year__sem_year_num__icontains=search_term)
        )

    # Query MaterialContent objects that match the search terms
    search_results = MaterialContent.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []
    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_item = {
            'id'                            : result.id,
            'has_sub_content'               : result.has_sub_content,
            'subject'                       : result.subject.subject_name,
            'material_type'                 : result.material_type.material_name,
            'level'                         : result.subject.level.level_name,
            'sem_year'                      : result.subject.sem_year.sem_year_num,
        }
        results_list.append(search_item)

    # Return the list of search results
    return results_list


def LoksewaNotesSearch(loksewa_notes_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in loksewa_notes_search_data:
        query |= (
        Q(name__icontains=search_term)
        )

    # Query MaterialContent objects that match the search terms
    search_results = LoksewaNotes.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []
    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_item = {
            'id'                            : result.id,
            'name'                          : result.name,
            'loksewa_notes'                  : 'loksewa_notes',    # Flag indicating it's a Loksewa notes result
        }
        results_list.append(search_item)

    # Return the list of search results
    return results_list


def LoksewaPastQuestionSearch(loksewa_past_question_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in loksewa_past_question_search_data:
        query |= (
            Q(year__icontains=search_term)
        )
    
    # Query LoksewaPastQuestion objects that match the search terms
    search_results = LoksewaPastQuestion.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_item = {
            'id' : result.id,
            'year' : result.year,
            'loksewa_past_question': 'loksewa_past_question' # Flag indicating it's a Loksewa past question result
        }
        results_list.append(search_item)

    # Return the list of search results
    return results_list


def LoksewaModelQuestionSearch(loksewa_model_question_search_data):
    # Build a dynamic query using Q objects 
    query = Q()
    for search_term in loksewa_model_question_search_data:
        query |= (
            Q(name__icontains=search_term)
        )

    # Query LoksewaModelQuestion objects that match the search terms
    search_results = LoksewaModelQuestion.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_term = {
            'id':result.id,
            'name': result.name,
            'loksewa_model_question' : 'loksewa_model_question'    # Flag indicating it's a Loksewa model question result
        }
        results_list.append(search_term)

    # Return the list of search results
    return results_list


def CouncilActSearch(council_act_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in council_act_search_data:
        query |= (
            Q(name__icontains=search_term)
        )

    # Query CouncilAct objects that match the search terms
    search_results = CouncilAct.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_term = {
            'id' : result.id,
            'name':result.name,
            'council_act':'council_act'   # Flag indicating it's a council act result
        }
        results_list.append(search_term)
    
    # Return the list of search results
    return results_list


def CouncilRegulationSearch(council_regulation_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in council_regulation_search_data:
        query |= (
            Q(name__icontains=search_term)
        )

    # Query CouncilAct objects that match the search terms
    search_results = CouncilRegulation.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_term = {
            'id' : result.id,
            'name':result.name,
            'council_regulation':'council_regulation'   # Flag indicating it's a council regulation result
        }
        results_list.append(search_term)
    
    # Return the list of search results
    return results_list


def CouncilPastQuestionSearch(council_past_question_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in council_past_question_search_data:
        query |= (
            Q(year__icontains=search_term)
        )

    # Query CouncilAct objects that match the search terms
    search_results = CouncilPastQuestion.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_term = {
            'id' : result.id,
            'year':result.year,
            'council_past_question':'council_past_question'   # Flag indicating it's a council past question result
        }
        results_list.append(search_term)
    
    # Return the list of search results
    return results_list


def CouncilModelQuestionSearch(council_model_question_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in council_model_question_search_data:
        query |= (
            Q(name__icontains=search_term)
        )

    # Query CouncilAct objects that match the search terms
    search_results = CouncilModelQuestion.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_term = {
            'id' : result.id,
            'name':result.name,
            'council_model_question':'council_model_question'   # Flag indicating it's a council model question result
        }
        results_list.append(search_term)
    
    # Return the list of search results
    return results_list


def GKSearch(gk_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in gk_search_data:
        query |= (
            Q(name__icontains=search_term)
        )

    # Query CouncilAct objects that match the search terms
    search_results = GK.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_term = {
            'id' : result.id,
            'name':result.name,
            'general_knowledge':'general_knowledge'   # Flag indicating it's a general knowledge result
        }
        results_list.append(search_term)
    
    # Return the list of search results
    return results_list


def BlogPostSearch(blog_search_data):
    # Build a dynamic query using Q objects
    query = Q()
    for search_term in blog_search_data:
        query |= (
            Q(title__icontains=search_term)
        )

    # Query CouncilAct objects that match the search terms
    search_results = Post.objects.filter(query)

    # Generate a list of dictionaries with relevant information from search_results
    results_list = []

    for result in search_results:
        # Extract relevant information from the search result and create a dictionary
        search_term = {
            'id' : result.uuid,
            'title':result.title,
            'blog_post':'blog_post'   # Flag indicating it's a blog post result
        }
        results_list.append(search_term)
    
    # Return the list of search results
    return results_list

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

            # Call the search functions and capture the returned results
            material_content_results             = MaterialContentSearch(search_terms_list)

            loksewa_notes_results                = LoksewaNotesSearch(search_terms_list)
            loksewa_past_question_results        = LoksewaPastQuestionSearch(search_terms_list)
            loksewa_model_question_results       = LoksewaModelQuestionSearch(search_terms_list)
            
            council_act_results                  = CouncilActSearch(search_terms_list)
            council_regulation_results           = CouncilRegulationSearch(search_terms_list)
            council_past_question_results        = CouncilPastQuestionSearch(search_terms_list)
            council_model_question_results       = CouncilModelQuestionSearch(search_terms_list)

            general_knowledge_results            = GKSearch(search_terms_list)

            blog_post_results                    = BlogPostSearch(search_terms_list)

            # Combine the results from both functions
            results_list = material_content_results + loksewa_notes_results + loksewa_past_question_results + loksewa_model_question_results + council_act_results + council_regulation_results + council_past_question_results + council_model_question_results + general_knowledge_results + blog_post_results
            
            # Sort the results_list based on the number of matched search terms with each object's value
            results_list = sorted(results_list, key=lambda x: sum(any(term.lower() in str(value).lower() for term in search_terms_list) for value in x.values()), reverse=True)

            # Return the sorted results as a JSON response
            return JsonResponse({'results': results_list})

        # Return an error message for invalid requests
        return JsonResponse({'message': 'Invalid request'})


