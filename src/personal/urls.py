#write urls code here
from django.urls import path
from personal.views import HomeView, UsefulLinksView, NewsNoticeView

urlpatterns = [
    path('',HomeView.as_view(), name='index'),
    path('useful_links/',UsefulLinksView.as_view(), name='usefullinks'),
    path('news_notice_syllabus/',NewsNoticeView.as_view(), name='newsnotice'),
]
