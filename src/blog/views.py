from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Post, PostComments
from personal.views import LevelAndMaterialDetails
# Create your views here.

class PostView(View):
    """
    A view class for handling post-related requests.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'post.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Set the template name for rendering
        template_name        = 'post.html'

        # Retrieve published posts
        post_object_list     = Post.objects.filter(is_published=True)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list   = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {

        'level_material_detail_list'      : level_material_detail_list,

        'post_object_list'                : post_object_list,

        }

        # Render the template with the provided context
        return render(request, template_name, context)


class PostContentView(View):
    """
    A view class for displaying the content of post
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'post_detail.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """

        # Get the slug from the URL parameters
        slug = kwargs['slug']

        # Set the template name for rendering
        template_name                         = 'post_detail.html'

        # Retrieve the post content object
        post_content_object                   = Post.objects.get(uuid = slug)

        # Retrieve comments for the post
        posted_comment_list                   = PostComments.objects.filter(post__uuid=slug)

        # Retrieve the latest 4 comments for the post
        posted_comment_object_list              = PostComments.objects.filter(post__uuid=slug).order_by('-id')[:4]

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list            = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'post_content_object'                      : post_content_object,
            
            'level_material_detail_list'               : level_material_detail_list,

            'posted_comment_object_list'               : posted_comment_object_list,

            'posted_comment_list'                      : posted_comment_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)


class PostCommentView(View):
    """
    A view class for handling post comment submissions
    """
    def post(self, request, *args, **kwargs):
        """
        Handle HTTP POST request for submitting a post comment
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: True
        """

        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With')  == 'XMLHttpRequest':
            
            # Get the logged-in user
            logged_in_user = request.user 

            # Get the comment from the request's POST data
            comment = request.POST['comment']

            # Get the post Id from the request's POST data
            post_id = request.POST['post_id']

            # Retrieve the post object based on the ID
            get_post_object = Post.objects.get(uuid = post_id)

            # Create a new post comment object
            post_comment = PostComments(user=logged_in_user, post=get_post_object, comment=comment)

            # Save the post comment object to the database
            post_comment.save()

            # Format the comment's date
            formatted_date = post_comment.date.strftime("%B") + ' ' + str(post_comment.date.day) + ', ' + post_comment.date.strftime("%Y")

            # Initialize an empty list to store posted comments
            posted_comment_list = []

            # Retrieve comments for the post
            posted_comment_object_list = PostComments.objects.filter(post__uuid=post_id)

            # Iterate over the retrieved comments
            for posted_comment in posted_comment_object_list:
                # Format the data of each comment in the loop
                formatted_date = posted_comment.date.strftime("%B") + ' ' + str(posted_comment.date.day) + ', ' + posted_comment.date.strftime("%Y")
                
                # Create a dictionary to store the formatted comment data
                comments_data = {

                    'user': posted_comment.user.username,
                    'date': formatted_date,
                    'comment': posted_comment.comment,
                    'logged_in_user': str(logged_in_user),
                }
                # Append the comment data dictionary to the posted_comment_list
                posted_comment_list.append(comments_data)

            # Prepare the comment data to be returned as JSON response
            comment_data = {

                'user': post_comment.user.username,
                'date': formatted_date,
                'comment': post_comment.comment,
                'logged_in_user': str(logged_in_user),
                'posted_comment_list': posted_comment_list
            }
            
            # Return the comment data as JSON response
            return JsonResponse([comment_data],safe=False)
        
        # Return True if the request is not an AJAX request
        return True
    

class LoadMoreCommentView(View):
    def get(self, request, *args, **kwargs):
        print("Entered_+_+_+_+")
        if request.headers.get('X-Requested-With')  == 'XMLHttpRequest':

            logged_in_user = request.user

            post_id = request.GET['post_id']

            count = int(request.GET.get('count'))  # Get the current count of comments

            # Calculate the desired range of comments
            start = count
            end = count + 4

            desired_comment_list = PostComments.objects.filter(post__uuid=post_id).order_by('-id')[start:end]
            
            serialized_comments = []

            for comment in desired_comment_list:
                serialized_comments.append({
                    'user':comment.user.username,
                    'date':comment.date,
                    'comment':comment.comment,
                    'logged_in_user': str(logged_in_user),
                })
            
            return JsonResponse({'comments':serialized_comments, 'count':count + len(desired_comment_list)}) # Include the updated count in the response
        
        return True
    





