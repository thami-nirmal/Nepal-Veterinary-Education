from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import SemYear, Level, MaterialContent, MaterialType, Subject
from personal.views import LevelAndMaterialDetails
from django.db.models import Q
# Create your views here.
def get_sem_year_list(request,id):
    sem_year_list = SemYear.objects.filter(level_id=id)
    return JsonResponse({'data': [{'id': sem_year.id, 'sem_year_num': sem_year.sem_year_num} for sem_year in sem_year_list]})

def get_material_type_list(request,id):
    material_type_list = MaterialType.objects.filter(level_id=id)
    return JsonResponse({'data': [{'id': material_type.id, 'material_name': material_type.material_name} for material_type in material_type_list]})

def get_subject_list(request,id):
    subject_list = Subject.objects.filter(level_id=id)
    return JsonResponse({'data': [{'id': subject.id, 'subject_name': subject.subject_name} for subject in subject_list]})


class NotesView(View):
    """
    
    """
    def get(self, request ,*args, **kwargs):
        # print(args)
        # print(kwargs)
        
        selected_level_name = kwargs['level_name']
        # print(selected_level_name)
        selected_material_name = kwargs['slug']
        print(selected_material_name)
        """
        
        """
        template_name                       = 'notes.html'

        level_material_detail_list          = LevelAndMaterialDetails()


        selected_level_object               = Level.objects.get(slug = selected_level_name)

        print(selected_level_object)
        print(selected_material_name)
        selected_material_type              = MaterialType.objects.get(slug = selected_material_name)
        print(selected_material_type.id)
        print('------------')
        print(selected_material_type)
        selected_material_content           = MaterialContent.objects.filter(material_type__level = selected_level_object,material_type = selected_material_type)
        print(selected_material_content)




        # selected_material_type              = MaterialType.objects.get()


        # notes_object_list                   = MaterialContent.objects.filter(is_shown=True)


        # desired_level                       = Level.objects.get(slug=selected_level_name)
        # # print(desired_level)

        # desired_material_list               = MaterialType.objects.filter(level=desired_level)
        # print('++++++++++++++++')
        # print(desired_material_list)


        # # desired_material_object             = MaterialType.objects.get(material_name=selected_material_name)
        # # print('**************')
        # # print(desired_material_object)

        # # desired_material_name               = MaterialType.objects.get(slug=selected_material_name)
        # # print(desired_material_name)

        # material_content_object_all = MaterialContent.objects.filter(Q(subject__level = desired_level) & Q(material_type__in = desired_material_list))
        # print('--------------------------------')
        # print(material_content_object_all)

        

        # # material_content_object = material_content_object_all.filter()


        sem_year_object_list                = SemYear.objects.filter(is_shown=True, level=selected_level_object)


        context = {
            'level_material_detail_list'   : level_material_detail_list,

            'selected_material_content'  : selected_material_content,

            'sem_year_object_list' : sem_year_object_list,

            
            # 'notes_object_list': notes_object_list,
            
            # 'desired_level'  : desired_level,
            # 'material_content_object_all' : material_content_object_all,
        }

        return render(request, template_name, context)

class NotesContentView(View):
    pass


