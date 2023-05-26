from django.shortcuts import render
from django.views import View
from .models import SyllabusInfo

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
        template_name = 'gk.html'
        return render(request, template_name)

class SyllabusInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'entrance_prep_syllabus.html'
        syllabus_info_object = SyllabusInfo.objects.all()
        tu_syllabus_info_object = syllabus_info_object.filter(university_choices = 'TU').order_by('faculty_choices')
        
        print(syllabus_info_object)
        syllabus_data = SyllabusInfo.objects.order_by('university_choices', ).values('university_choices', 'faculty_choices', 'subject', 'marks')
        # print(syllabus_data.values())
        # print(syllabus_info_object)
        context = {
            'data' : tu_syllabus_info_object,
            'syllabus_data' : syllabus_data,
        }
        return render(request, template_name, context)
    

class CollegeInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'entrance_college_info.html'
        return render(request, template_name)