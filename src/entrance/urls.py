#urls code here
from django.urls import path
from .views import GkView, SyllabusInfoView, CollegeInfoView,GkContentView

urlpatterns = [
    path('gk/',GkView.as_view(), name='gk'),
    path('gk-content-view/<int:id>',GkContentView.as_view(), name='gk_content'),
    path('entrance-prep-syllabus/',SyllabusInfoView.as_view(), name='entrance_syllabus_info'),
    path('entrance-college-info/',CollegeInfoView.as_view(), name='entrance_college_info'),
]