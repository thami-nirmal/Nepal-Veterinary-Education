from django import forms
from .models import  Level, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'is_shown', 'level', 'sem_year']
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        try:
            self.initial['level'] = kwargs['instance'].level.id
        except:
            pass
        level_list = [('', '---Select Level---')] + [(i.id, i.level_name) for i in Level.objects.all()]

        self.fields['level'].widget = forms.Select(
            attrs={
                'id': 'id',
                'onchange': 'getSemYear(this.value)',
                'style': 'width:200px'
            },
            choices=level_list,
        )