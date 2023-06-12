from django.shortcuts import render
from django.views import View
from graduate.models import Level, MaterialType
from .models import KrishiDiarys

# Create your views here.

# region Level and Material Details Function
def LevelAndMaterialDetails():
    
    level_object_list                                  = Level.objects.filter(is_shown = True)

    material_object_list                               = MaterialType.objects.filter(is_shown = True)

    level_material = {
        'level_object_list'                            : level_object_list,

        'material_object_list'                         : material_object_list,
    }
    return level_material
# endregion


#region Home View
class HomeView(View):
    def get(self, request,*args,**kwargs):

        template_name                                   = 'index.html'

        krishi_diary_details                            = KrishiDiarys.objects.filter(is_shown=True).order_by('-id')[:5]

        level_material_detail_list                      = LevelAndMaterialDetails()

        context = {
            'level_material_detail_list'                : level_material_detail_list,

            'krishi_diary_details'                      : krishi_diary_details,
        }
        return render(request, template_name, context)
#endregion

#region Useful Links View
class UsefulLinksView(View):
    def get(self, request, *args, **kwargs):

        template_name                                  = 'useful_links.html'

        level_material_detail_list                     = LevelAndMaterialDetails()

        context = {
            'level_material_detail_list'               : level_material_detail_list, 
        }

        return render(request, template_name, context)
#endregion


#region News Notice View
class NewsNoticeView(View):
    def get(self, request, *args, **kwargs):

        template_name                                  = 'news_notice_syllabus.html'

        level_material_detail_list                     = LevelAndMaterialDetails()

        context = {
            'level_material_detail_list'               : level_material_detail_list, 
        }

        return render(request, template_name, context)
#endregion


class KrishiDiarysView(View):
    def get(self, request, *args, **kwargs):

        template_name                                     = 'krishi_diarys.html'

        krishi_diarys_details_list                        = KrishiDiarys.objects.filter(is_shown=True).order_by('-id')[:8]

        level_material_detail_list                        = LevelAndMaterialDetails()

        context   = {
            'level_material_detail_list'                  : level_material_detail_list,

            'krishi_diarys_details_list'                  : krishi_diarys_details_list,
        }

        return render(request, template_name, context)


class KrishiDiarysContentView(View):
    def get(self, request, id, *args, **kwargs):

        template_name                                     = 'krishi_diarys_content_view.html'

        krishi_diarys_object                              = KrishiDiarys.objects.get(id = id)

        level_material_detail_list                        = LevelAndMaterialDetails()
        
        context = {
            'level_material_detail_list'                  : level_material_detail_list,

            'krishi_diarys_object'                        : krishi_diarys_object,
        }
        
        return render(request, template_name, context)