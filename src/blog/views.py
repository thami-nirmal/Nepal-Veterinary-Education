from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Post, PostComments

from personal.views import LevelAndMaterialDetails
# Create your views here.

class PostView(View):

    def get(self, request, *args, **kwargs):

        template_name        = 'post.html'

        post_object_list     = Post.objects.filter(is_published=True)
        # print(post_object_list)

        # post_comment_object_list  = PostComments.objects.all();
        # print(post_comment_object_list)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list   = LevelAndMaterialDetails()

        # Create a context dictionary to store the data to be passed to the template
        context = {

        'level_material_detail_list'      : level_material_detail_list,

        'post_object_list'                : post_object_list,

        }

        return render(request, template_name, context)

class PostContentView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs['slug']
        # Set the template name for rendering
        template_name                         = 'post_detail.html'

        post_content_object                   = Post.objects.get(uuid = slug)
        print("-----------------")
        print(post_content_object.title)

        posted_comment_list                   = PostComments.objects.filter(post__uuid=slug)

        posted_comment_object_list              = PostComments.objects.filter(post__uuid=slug).order_by('-id')[:4]
        print("000000000000000")
        print(posted_comment_object_list)


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
    def post(self, request, *args, **kwargs):

        if request.headers.get('X-Requested-With')  == 'XMLHttpRequest':

            logged_in_user = request.user   # we get the instance of user, because when we post data into fk field

            # print("Logged_in_user:::::::::::::::::::::",logged_in_user)

            comment = request.POST['comment']

            id = request.POST['id']

            get_post_object = Post.objects.get(uuid = id)

            post_comment = PostComments(user=logged_in_user, post=get_post_object, comment=comment)

            post_comment.save()

            formatted_date = post_comment.date.strftime("%B") + ' ' + str(post_comment.date.day) + ', ' + post_comment.date.strftime("%Y")

            posted_comment_list = []
            posted_comment_object_list = PostComments.objects.filter(post__uuid=id)
            for posted_comment in posted_comment_object_list:
                formatted_date = posted_comment.date.strftime("%B") + ' ' + str(posted_comment.date.day) + ', ' + posted_comment.date.strftime("%Y")
                comments_data = {
                    'user': posted_comment.user.username,
                    'date': formatted_date,
                    'comment': posted_comment.comment,
                    'logged_in_user': str(logged_in_user),
                }
                posted_comment_list.append(comments_data)

            comment_data = {
                'user': post_comment.user.username,
                'date': formatted_date,
                'comment': post_comment.comment,
                'logged_in_user': str(logged_in_user),
                'posted_comment_list': posted_comment_list
            }
            print(comment_data)
            
            return JsonResponse([comment_data],safe=False)
        
        return True
    





