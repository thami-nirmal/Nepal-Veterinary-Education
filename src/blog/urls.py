#urls code here
from django.urls import path
from .views import PostView, PostContentView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),

    path('post-content-view/<str:slug>',PostContentView.as_view(), name='post_content_view'),

    # path('post-comment/', PostCommentView.as_view(), name='post_comment'),

]