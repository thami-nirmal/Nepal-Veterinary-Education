#urls code here
from django.urls import path
from post_graduate.views import (CollegeInfoView,
                    SyllabusInfoView,
                    LoksewaView,
                    LoksewaPastQuestionContentView,
                    LoksewaModelQuestionContentView,
                    LoksewaNotesContentView,
                    CouncilView,
                    CouncilActContentView,
                    CouncilRegulationContentView,
                    CouncilPastQuestionContentView,
                    CouncilModelQuestionContentView,
                    )


urlpatterns = [

    path('post-graduate-syllabus-info/',SyllabusInfoView.as_view(), name='post_graduate_syllabus_info'),

    path('post-graduate-college-info/',CollegeInfoView.as_view(), name='post_graduate_college_info'),

    path('post-graduate-loksewa/',LoksewaView.as_view(), name='post_graduate_loksewa'),

    path('loksewa-past-question-content-view/<int:id>',LoksewaPastQuestionContentView.as_view(), name='loksewa_past_question_content_view'),
    path('loksewa-model-question-content-view/<int:id>',LoksewaModelQuestionContentView.as_view(), name='loksewa_model_question_content_view'),
    path('loksewa-notes-content-view/<int:id>',LoksewaNotesContentView.as_view(), name='loksewa_notes_content_view'),

    path('post-graduate-council/',CouncilView.as_view(), name='post_graduate_council'),

    path('council-act-content-view/<int:id>',CouncilActContentView.as_view(), name='council_act_content_view'),
    path('council-regulation-content-view/<int:id>',CouncilRegulationContentView.as_view(), name='council_regulation_content_view'),
    path('council-past-question-content-view/<int:id>',CouncilPastQuestionContentView.as_view(), name='council_past_question_content_view'),
    path('council-model-question-content-view/<int:id>',CouncilModelQuestionContentView.as_view(), name='council_model_question_content_view'),
]