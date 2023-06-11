from django.urls import path
from .views import NotesView, NotesContentView
from graduate.views import get_sem_year_list, get_material_type_list,get_subject_list

urlpatterns = [
    path('sem-year/<int:id>',get_sem_year_list, name='get_sem_year_list'),
    
    path('material-type/<int:id>',get_material_type_list, name='get_material_type_list'),

    path('subject/<int:id>',get_subject_list, name='get_subject_list'),
    
    path('<str:level_name>/<str:slug>/', NotesView.as_view(), name='graduate_detail'),

    path('notes-content-view/<int:id>',NotesContentView.as_view(), name='notes_content_view'),
]