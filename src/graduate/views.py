from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import MaterialContent, SemYear, Level
from personal.views import LevelAndMaterialDetails
# Create your views here.
def get_sem_year_list(request,id):
    sem_year_list = SemYear.objects.filter(level_id=id)
    return JsonResponse({'data': [{'id': sem_year.id, 'sem_year_name': sem_year.sem_year_num} for sem_year in sem_year_list]})

class NotesView(View):
    """
    
    """
    def get(self, request ,*args, **kwargs):
        selected_level_name = kwargs['level_name']
        selected_material_name = kwargs['material_name']
        """
        
        """
        template_name                       = 'notes.html'
        notes_object_list                   = MaterialContent.objects.filter(is_shown=True)
        desired_level                       = Level.objects.get(slug=selected_level_name)
        sem_year_object_list                = SemYear.objects.filter(is_shown=True, level=desired_level)
        # print(sem_year_object_list)

        level_material_detail_list          = LevelAndMaterialDetails()

        context = {
            'notes_object_list': notes_object_list,
            'sem_object_list' : sem_year_object_list,
            'desired_level'  : desired_level,

            'level_material_detail_list'   : level_material_detail_list,
        }

        return render(request, template_name, context)

class NotesContentView(View):
    pass


