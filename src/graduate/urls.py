from django.urls import path
from .views import GraduateView, GraduateContentView, GraduateSubContentView, SearchView
from graduate.views import get_sem_year_list, get_material_type_list,get_subject_list

urlpatterns = [
    path('sem-year/<int:id>',get_sem_year_list, name='get_sem_year_list'),

    path('material-type/<int:id>',get_material_type_list, name='get_material_type_list'),

    path('subject/<int:id>',get_subject_list, name='get_subject_list'),

    path('<str:level_name>/<str:slug>/', GraduateView.as_view(), name='graduate_detail'),

    path('graduate-content-view/<int:id>',GraduateContentView.as_view(), name='graduate_content_view'),

    path('graduate-sub-content-view/<int:id>',GraduateSubContentView.as_view(), name='graduate_sub_content_view'),

    path('search-view/',SearchView.as_view(), name='search_view'),
]
