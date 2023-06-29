from django.shortcuts import render, HttpResponse
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

        # Retrieve the GK details object with the given 'id'
        post_content_object                   = Post.objects.get(uuid = slug)
        # print(post_content_object.title)

        # Call the LevelAndMaterialDetails function to retrieve level and material data
        level_material_detail_list            = LevelAndMaterialDetails()
        
        # Prepare the context data for rendering the template
        context = {
            'post_content_object'                      : post_content_object,
            
            'level_material_detail_list'      : level_material_detail_list
        }

        # Render the template with the provided context
        return render(request, template_name, context)
    

class PostCommentView(View):
    def post(self, request, *args, **kwargs):
        print("Hello Worlds")
        if request.headers.get('X-Requested-With')  == 'XMLHttpRequest':
            print("Hello Universe")
            # Get the form input value from the request
            email = request.POST['email']
            name = request.POST['name']
            comment = request.POST['comment']
            id = request.POST['id']
            print(name, email, comment, id)

            post_comment = PostComments(comment=comment)
            post_comment.save()
            print(post_comment)
            
            return JsonResponse({'status': 'success'})
        return True



