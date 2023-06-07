from django.urls import path
from .views import NotesView, NotesContentView

urlpatterns = [
    path('<str:level_name>/<str:material_name>/', NotesView.as_view(), name='graduate_detail'),
    path('notes-content-view/<int:id>',NotesContentView.as_view(), name='notes_content_view'),
]