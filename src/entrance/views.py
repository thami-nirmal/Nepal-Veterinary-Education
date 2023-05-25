from django.shortcuts import render
from django.views import View

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
        return render(request, template_name)


class CollegeInfoView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'entrance_college_info.html'
        return render(request, template_name)