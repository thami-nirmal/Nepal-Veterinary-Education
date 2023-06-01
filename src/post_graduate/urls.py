#urls code here
from django.urls import path
from .views import (CollegeInfoView,
                    SyllabusInfoView)


urlpatterns = [
    path('post-graduate-syllabus-info/',SyllabusInfoView.as_view(), name='post_graduate_syllabus_info'),
    path('post-graduate-college-info/',CollegeInfoView.as_view(), name='post_graduate_college_info'),
]