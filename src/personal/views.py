from django.shortcuts import render
from django.views import View
from graduate.models import Level, MaterialType

# Create your views here.
#region Level and Material Details Function
def LevelAndMaterialDetails():
    level_object_list       = Level.objects.filter(is_shown = True)
    material_object_list    = MaterialType.objects.filter(is_shown = True)

    level_material = {
        'level_object_list'     : level_object_list,
        'material_object_list'  : material_object_list,
    }
    return level_material
#endregion

#region Home View
class HomeView(View):
    def get(self, request,*args,**kwargs):
        template_name                  = 'index.html'
        level_material_detail_list     = LevelAndMaterialDetails()

        context = {
            'level_material_detail_list'   : level_material_detail_list,
        }
        return render(request, template_name, context)
#endregion

#region Useful Links View
class UsefulLinksView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'useful_links.html'
        return render(request, template_name)
#endregion

#region News Notice View
class NewsNoticeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'news_notice_syllabus.html'
        return render(request, template_name)
#endregion
