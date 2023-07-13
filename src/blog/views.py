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
        :return: True if the request is not an AJAX request
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
    """
    A view class for handling the load more comments feature
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request for loading more comments
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: True if the request is not an AJAX request
        """

        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With')  == 'XMLHttpRequest':

            # Get the logged-in user from the request object
            logged_in_user = request.user

            # Get the post Id from the GET parameters or access the post_id from ajax
            post_id = request.GET['post_id']

            # Get the current count of comments from the GET parameters and convert it to an integer
            count = int(request.GET.get('count'))  

            # Calculate the desired range of comments
            start = count
            end = count + 4

            # Retrieve the desired range of comments based on the post id and order them by id in descending order
            desired_comment_list = PostComments.objects.filter(post__uuid=post_id).order_by('-id')[start:end]
            
            # Serialize the comments into a list of dictionaries
            serialized_comments = []

            for comment in desired_comment_list:
                serialized_comments.append({
                    'user':comment.user.username,
                    'date':comment.date,
                    'comment':comment.comment,
                    'logged_in_user': str(logged_in_user),
                })
            
            # Return a JSON response containing to seralized comments and the updated count
            return JsonResponse({'comments':serialized_comments, 'count':count + len(desired_comment_list)}) # Include the updated count in the response
        
        # Return True if the request is not an AJAX request
        return True


class CommentEditView(View):
    """
    A view class for handling the editing of comments
    """
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request for editing a comments
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: True if the request is not an AJAX request
        """

        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
            # Get the post Id from the GET parameters
            post_id = request.GET['post_id']

            # Get the comment Id from the GET parameters
            comment_id = request.GET['commentId']

            # Retrieve the desired comment based on the post id and comment id
            desired_comment = PostComments.objects.get(post__uuid=post_id, id=comment_id)

            # Create a dictionary with the desired comment
            edit_comment = {
                'desired_comment' : desired_comment.comment
            }
            
            # Return a JsonResponse with the desired comment to edit
            return JsonResponse({'comments':[edit_comment]})
        
        # Return True if the request is not an AJAX request
        return True
    

class CommentUpdateView(View):
    """
    A view class for handling the updating of comments
    """
    def post(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request for updating a comment.
        :param request: the HTTP request object
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: JsonResponse with a success message if the comment is updated, otherwise True
        """

        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With')  == 'XMLHttpRequest':
            
            # Get the updated comment from the POST parameters
            update_comment = request.POST['update_comment']

            # Get the comment ID from the POST parameters
            commentId = request.POST['commentId']

            # Retrieve the comment from the database using the comment_id
            comment_obj = PostComments.objects.get(id=commentId)

            # Update the comment data
            comment_obj.comment = update_comment

            # Save the updated comment
            comment_obj.save()

            # Return a JsonResponse with a success message
            return JsonResponse({'Successfully Updated'})
        
        # Return True if the request is not an AJAX request
        return True
    
class CommentDeleteView(View):
    """
    A view class for handling the deletion of comments.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request for deleting a comment.
        :param request: the HTTP request object
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: JsonResponse with a success message if the comment is deleted, otherwise True
        """

        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
            # Get the post ID from the POST parameters
            post_id = request.POST.get('post_id')

            # Get the comment ID from the POST parameters
            comment_id = request.POST.get('commentId')

            # Retrieve the comment from the database using the post ID and comment ID
            delete_comment = PostComments.objects.get(post__uuid=post_id, id=comment_id)
            
            # Delete the comment
            delete_comment.delete()

            # Return a JsonResponse with a success message
            return JsonResponse({'message': 'Comment deleted successfully'})
        
        # Return True if the request is not an AJAX request
        return True






