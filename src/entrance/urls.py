#urls code here
from django.urls import path
from .views import GkView, SyllabusInfoView, CollegeInfoView

urlpatterns = [
    path('gk/',GkView.as_view(), name='gk'),
    path('entrance-prep-syllabus/',SyllabusInfoView.as_view(), name='entrance_syllabus_info'),
    path('entrance-college-info/',CollegeInfoView.as_view(), name='entrance_college_info'),
]