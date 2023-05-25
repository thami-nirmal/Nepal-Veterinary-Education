#urls code here
from django.urls import path
from .views import GkView, SyllabusInfoView, CollegeInfoView

urlpatterns = [
    path('gk/',GkView.as_view(), name='gk'),
    path('entrance_prep_syllabus/',SyllabusInfoView.as_view(), name='syllabusinfo'),
    path('entrance_college_info/',CollegeInfoView.as_view(), name='collegeinfo'),
]