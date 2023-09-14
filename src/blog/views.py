from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Post, PostComments, PostLikes, PostViews, UserViews
from personal.views import LevelAndMaterialDetails
from django.db.models import Q
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
        post_object_list     = Post.objects.filter(is_published=True).order_by('-created_at')

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
        template_name                            = 'post_detail.html'

        # Retrieve the post content object
        post_content_object                      = Post.objects.get(uuid = slug)

        # Retrieve comments for the post
        posted_comment_list                      = PostComments.objects.filter(post__uuid=slug)

        # Retrieve the latest 4 comments for the load more comments
        posted_comment_object_list               = PostComments.objects.filter(post__uuid=slug).order_by('-id')[:4]

        # Retrieve the current post time
        current_post_time = post_content_object.created_at
        
        # Retrieve the previous post of current post
        previous_suggested_blog = Post.objects.filter(created_at__lt=current_post_time).order_by('-created_at').first()

        # Logged in user
        user = request.user

        user_post_like = False
        user_post_like_obj = None

        if user.is_authenticated:
            # Try to retrieve the user's post like object with is_liked=True
            try:
                # Retrieve the user's post like object for the given post (identified by slug)
                # with is_liked=True, indicating that the user has liked the post
                user_post_like_obj = PostLikes.objects.get(post__uuid=slug, user=user, is_liked=True)

            except PostLikes.DoesNotExist:
                # If the user's post like object does not exist or the user has not liked the post,
                # set user_post_like_obj to None
                user_post_like_obj = None

            # Check if the user has any post like
            if PostLikes.objects.filter(post=slug,user=user).exists():
                user_post_like =True

        # Retrieve the post liked count of post
        post_like_count                         = PostLikes.objects.filter(post__uuid=slug, is_liked=True).count()
        
        # Retrieve the number of shared post
        share_post_count                        = post_content_object.share_count

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list              = LevelAndMaterialDetails()

        # Prepare the context data for rendering the template
        context = {
            'user_post_like'                           : user_post_like,

            'user_post_like_obj'                       : user_post_like_obj,

            'post_content_object'                      : post_content_object,

            'level_material_detail_list'               : level_material_detail_list,

            'posted_comment_object_list'               : posted_comment_object_list,

            'posted_comment_list'                      : posted_comment_list,

            'post_like_count'                          : post_like_count,

            'share_post_count'                         : share_post_count,

            'previous_suggested_blog'                  : previous_suggested_blog

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

            if not logged_in_user.is_authenticated:

                comment_data = {
                    'login' : False
                }

                return JsonResponse([comment_data],safe=False)

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
                    'id'   : posted_comment.id,
                    'user_first_name': posted_comment.user.first_name,
                    'user_last_name': posted_comment.user.last_name,
                    'date': formatted_date,
                    'comment': posted_comment.comment,
                    'logged_in_user': str(logged_in_user),
                }
                # Append the comment data dictionary to the posted_comment_list
                posted_comment_list.append(comments_data)

            user_profile_image = posted_comment.user.profile.profile_image.url
            print("USER PROFILE IMAGE", user_profile_image)

            # Prepare the comment data to be returned as JSON response
            comment_data = {
                'login': True,
                'id':post_comment.id,
                'user_first_name': post_comment.user.first_name,
                'user_last_name': post_comment.user.last_name,
                'username':post_comment.user.username,
                'date': formatted_date,
                'comment': post_comment.comment,
                'logged_in_user': str(logged_in_user),
                'posted_comment_list': posted_comment_list,
                'user_profile_image' : user_profile_image
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
                    'id':comment.id,
                    'user_first_name':comment.user.first_name,
                    'user_last_name':comment.user.last_name,
                    'username':comment.user.username,
                    'date':comment.date,
                    'comment':comment.comment,
                    'logged_in_user': str(logged_in_user),
                    'user_profile_image': comment.user.profile.profile_image.url
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

class likeBtnView(View):
    """
    A view class for handling the like button functionality
    """
    def post(self, request, *args, **kwargs):
        """
        Handle HTTP POST request for liking a post
        :param request: the HTTP request object
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: JSON response
        """
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            # Get the 'post_id' from the POST request data
            post_id = request.POST['post_id']

            # Get the currently logged-in user
            logged_in_user = request.user

            if not logged_in_user.is_authenticated:

                saved_post_like = {
                    'login':False
                }
                
                # Return a JSON response with the saved_post_like data
                return JsonResponse({'saved_post_like': [saved_post_like]})

            # Retrieve the Post object associated with the 'post_id'
            get_post_object = Post.objects.get(uuid = post_id)

            # Create a new PostLikes object representing the like action
            if not PostLikes.objects.filter(user=logged_in_user,post=get_post_object).exists():
                post_like = PostLikes(user=logged_in_user, post=get_post_object, is_liked=True)

                # Save the Postlikes object to the database
                post_like.save()
                

            # Retrieve the post liked count of post
            post_like_count        = PostLikes.objects.filter(post=get_post_object, is_liked=True).count()

            # Prepare the saved_post_like data for the JSON response
            saved_post_like = {
                'login':True,
                'post_like_id' : post_like.id,
                'post_like_user' : post_like.user.username,
                'post_like_count' : post_like_count
            }

            # Return a JSON response with the saved_post_like data
            return JsonResponse({'saved_post_like': [saved_post_like]})

        # Return True if the request is not an XMLHttpRequest
        return True

class dislikeBtnView(View):
    """
    A view class for handling the dislike button functionality
    """
    def post(self, request, *args, **kwargs):
        """
        Handle HTTP POST request for disliking a post
        :param request: the HTTP request object
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: JSON response
        """
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            # Get the 'post_id' and 'post_like_id' from the POST request data
            post_id = request.POST['post_id']
            post_like_id = request.POST['post_like_id']
            
            # Get the currently logged-in-user
            logged_in_user = request.user

            # Retrieve the specific PostLikes object to be deleted
            post_like = PostLikes.objects.get(post__uuid=post_id, id=post_like_id, user=logged_in_user)

            # Delete the PostLikes object from the database
            post_like.delete()

            # Retrieve the post liked count of post
            post_like_count                       = PostLikes.objects.filter(post=post_id, is_liked=True).count()

            # Prepare the delete_post_like data for the JSON response
            delete_post_like = {
                'post_like_count'              : post_like_count
            }

            # Return a JSON response indicating the successful deletion
            return JsonResponse({'data': [delete_post_like]})
            
        # Return True if the request is not an XMLHttpRequest
        return True

class PostViewsView(View):
    """
    A view class to handle post requests for tracking and incrementing post views.
    """
    def post(self,request,*args,**kwargs):
        """
        Handles the post request to track and increment post views.

        Parameters:
        - request: The HTTP request object
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - If the request is an AJAX request, returns a JSON response indicating the success message.
        - If the request is not an AJAX request, returns a boolean value of True
        """

        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
            # Retrieve the 'post_id' value from the AJAX request's POST data
            post_id = request.POST.get('post_id')

            # Get the Post object based on the 'post_id'
            get_post_object = Post.objects.get(uuid=post_id)

            # Retrieve the PostViews object related to the Post object, if it exists
            post_views = PostViews.objects.filter(post=get_post_object).first()

            # If no PostViews object exists
            if not post_views:
                # Create a new PostViews object with initial views set to 1
                post_views = PostViews.objects.create(post=get_post_object, views=1)
            else:
                # If a PostViews object exists increment the views count and save the changes
                post_views.views += 1
                post_views.save()
                
            # Return a JSON response indicating the success message
            return JsonResponse({'message': 'Post successfully received views'})
        
        # If the request is not an AJAX request, return a boolean value of True
        return True

class UserViewsView(View):
    """
    A view class to handle post requests for tracking and incrementing user views.
    """
    def post(self,request,*args,**kwargs):
        """
        Handles the post request to track and increment user views

        Parameters:
        - request: The HTTP request object
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - If the request is an AJAX request, returns a JSON response indicating the success message.
        - If the request is not an AJAX request, returns a boolean value of True
        """
        
        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            # Retrieve the 'post_id' value from the AJAX request's POST data
            post_id = request.POST.get('post_id')

            # Get the Post object based on the 'post_id'
            post_object = Post.objects.get(uuid=post_id)

            # Get the currently logged-in user
            logged_in_user = request.user
            
            # Query the UserViews model to see if a record exists for the post
            user_views = UserViews.objects.filter(post=post_object).first()

            # If there's a logged-in user
            if logged_in_user:
                # If no UserViews record exists for the post, create a new one
                if not user_views:
                    user_views = UserViews.objects.create(user=logged_in_user,post=post_object, count=1)
                else:
                    # If a UserViews record exists, increment the 'count' field and save
                    user_views.count += 1
                    user_views.save()
            else:
                # Return a JSON response indicating that the user must be logged in
                return JsonResponse({'message': 'You must be logged in to perform this action.'}, status=401)
            
            # Return a JSON response indicating success
            return JsonResponse({'message':'Post successfully received user views'})

        # If the request is not AJAX, return True
        return True

class SharePostView(View):
    """
    This view handles AJAX POST requests to increment the share count of a post object.
    """
    def post(self, request, *args, **kwargs):
        """
        Handle the POST request to increment the share count of a post
        :param request: the HTTP request object
        :param args: additional positional arguments
        :param kwargs: additional keyword arguments
        :return: JSON response
        """
        
        # Check if the request is an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            
            # Get the post_id from the POST data
            post_id = request.POST.get('post_id')
            
            # Retrieve the post object using the provided post_id
            share_post_object = Post.objects.get(uuid=post_id)  
            
            # Increment the share count of the post object
            if share_post_object.share_count is None:
                share_post_object.share_count = 1
            else:
                share_post_object.share_count += 1

            # Save the updated post object
            share_post_object.save()

            # Prepare data for the response
            share_post_object_data_list = []
            share_post_object_data = {
                'post_share_count': share_post_object.share_count,
            }

            share_post_object_data_list.append(share_post_object_data)
            
            # Return a JSON response with the updated share count
            return JsonResponse({'share_post_object_count': share_post_object_data_list})
        
        # If not an AJAX request, return True
        return True
