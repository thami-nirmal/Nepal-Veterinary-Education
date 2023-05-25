#urls code here
from django.urls import path
from .views import GkView

urlpatterns = [
    path('gk/',GkView.as_view(), name='gk'),
]