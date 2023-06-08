from django.urls import path
from .views import NotesView, NotesContentView
from graduate.views import get_sem_year_list

urlpatterns = [
    path('sem-year/<int:id>',get_sem_year_list, name='get_sem_year_list'),
    path('<str:level_name>/<str:material_name>/', NotesView.as_view(), name='graduate_detail'),
    path('notes-content-view/<int:id>',NotesContentView.as_view(), name='notes_content_view'),
]