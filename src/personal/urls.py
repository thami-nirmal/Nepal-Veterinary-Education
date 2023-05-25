#write urls code here
from django.urls import path
from personal.views import (
    HomeView, 
    UsefulLinksView, 
    NewsNoticeView
    )

urlpatterns = [
    path('',HomeView.as_view(), name='index'),
    path('useful-links/',UsefulLinksView.as_view(), name='useful_links'),
    path('news-notice-syllabus/',NewsNoticeView.as_view(), name='news_notice'),
]
