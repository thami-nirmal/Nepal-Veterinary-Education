#write urls code here
from django.urls import path
from personal.views import (
    HomeView, 
    UsefulLinksView, 
    NewsNoticeView,
    KrishiDiarysView,
    KrishiDiarysContentView
    )

urlpatterns = [
    path('',HomeView.as_view(), name='index'),

    path('useful-links/',UsefulLinksView.as_view(), name='useful_links'),

    path('news-notice-syllabus/',NewsNoticeView.as_view(), name='news_notice'),

    path('krishi-diarys/', KrishiDiarysView.as_view(), name='krishi_diarys'),

    path('krishi-diarys-content-view/<int:id>', KrishiDiarysContentView.as_view(), name='krishi_diarys_content_view'),

]
