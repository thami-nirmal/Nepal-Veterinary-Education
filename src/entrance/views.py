from django.shortcuts import render
from django.views import View
from .models import SyllabusInfo, CollegeInfo, GK

# Create your views here.
class GkView(View):
    def get(self, request, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'gk.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        template_name     = 'gk.html'
        gk_object         = GK.objects.filter(is_shown=True)

        if gk_object.exists():
            gk_object = gk_object
        else:
            gk_object = None 

        context = {
            'gk_data_list' : gk_object,
        }

        return render(request, template_name, context)
    
class GkContentView(View):
    def get(self, request, id, *args, **kwargs):
        """
        Handle HTTP GET request and render the 'gk.html'
        :param request: the HTTP request object
        :param args: additional positional argument
        :param kwargs: additional keyword arguments
        :return: the rendered http response
        """
        template_name      = 'gk_content_view.html'
        gk_details_object  = GK.objects.get(id = id)
        context = {
            'gk_details' : gk_details_object,
        }

        return render(request, template_name, context)
    
    
    
class SyllabusInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name                  = 'entrance_prep_syllabus.html'
        syllabus_info_object           = SyllabusInfo.objects.filter(is_shown=True)
        
        group = {}
        syllabus_data = []

        if syllabus_info_object.exists():
            for data in syllabus_info_object:
                if data.university_choices not in group:
                    group[data.university_choices] = {}
                if data.faculty_choices not in group[data.university_choices]:
                    group[data.university_choices][data.faculty_choices] = []
                syllabus_data = [data.subject, data.no_of_question, data.marks]
                group[data.university_choices][data.faculty_choices].append(syllabus_data)

        # print(group)
        context = {
            'syllabus_data' : syllabus_data,
            'group': group,
        }
        return render(request, template_name, context)
    

class CollegeInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name                   = 'entrance_college_info.html'
        college_info_object             = CollegeInfo.objects.filter(is_shown=True)

        group = {}
        college_data = []
        
        if college_info_object.exists():
            for data in college_info_object:
                if data.university_choices not in group:
                    group[data.university_choices] = {}
                if data.faculty_choices not in group[data.university_choices]:
                    group[data.university_choices][data.faculty_choices] = []
                college_data = [data.quota_name, data.no_of_student]
                group[data.university_choices][data.faculty_choices].append(college_data)

        context = {
            'college_data' : college_data,
            'group' : group,
        }
        return render(request, template_name, context)

