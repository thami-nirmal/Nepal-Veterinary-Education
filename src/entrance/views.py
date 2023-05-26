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
        template_name                  = 'entrance_prep_syllabus.html'
        syllabus_info_object           = SyllabusInfo.objects.filter(is_shown=True)
        tu_syllabus_info_object        = syllabus_info_object.filter(university_choices = 'TU').order_by('faculty_choices')
        
        # print(syllabus_info_object)
        # syllabus_data = SyllabusInfo.objects.order_by('university_choices', ).values('university_choices', 'faculty_choices', 'subject', 'marks')
        # print(syllabus_data.values()
        # print(syllabus_info_object)
        group = {}
        for data in syllabus_info_object:
            if data.university_choices not in group:
                group[data.university_choices] = {}
            if data.faculty_choices not in group[data.university_choices]:
                group[data.university_choices][data.faculty_choices] = []
            syllabus_data = [data.subject, data.no_of_question, data.marks]
            group[data.university_choices][data.faculty_choices].append(syllabus_data)

        # print(group)
        context = {
            'data' : tu_syllabus_info_object,
            'syllabus_data' : syllabus_data,
            'group': group,
        }
        return render(request, template_name, context)
    

class CollegeInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'entrance_college_info.html'
        return render(request, template_name)