#urls code here
from django.urls import path
from .views import (PostView,
                    PostContentView,
                    PostCommentView,
                    LoadMoreCommentView, 
                    CommentEditView, 
                    CommentUpdateView, 
                    CommentDeleteView, 
                    likeBtnView, 
                    dislikeBtnView)

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),

    path('post-content-view/<str:slug>',PostContentView.as_view(), name='post_content_view'),

    path('post-comment/', PostCommentView.as_view(), name='post_comment'),

    path('load-more-comment/',LoadMoreCommentView.as_view(), name='load_more_comment'),

    path('edit-comment/', CommentEditView.as_view(), name='edit_comment'),

    path('update-comment/', CommentUpdateView.as_view(), name='update_comment'),

    path('delete-comment/', CommentDeleteView.as_view(), name='delete_comment'),

    path('like-btn/', likeBtnView.as_view(), name='like_btn'),

    path('dislike-btn/', dislikeBtnView.as_view(), name='dislike_btn'),
]