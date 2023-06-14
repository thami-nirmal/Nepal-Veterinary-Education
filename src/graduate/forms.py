from django import forms
from .models import  Level, Subject, MaterialContent


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'is_shown','level', 'sem_year']
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)

        try:
            self.initial['level'] = kwargs['instance'].level.id
        except:
            pass

        level_list = [('', '----Select Level---')] + [(i.id, i.level_name) for i in Level.objects.all()]

        self.fields['level'].widget = forms.Select(
            attrs={
                'id': 'id',
                'onchange': 'getSemesterYear(this.value)',
                'style': 'width:200px'
            },
            choices=level_list,
        )

        # Set the initial value of sem_year field to None
        self.fields['sem_year'].widget.choices = [('', '----Select Semester/Year---')]

class MaterialContentForm(forms.ModelForm):
    level = forms.ModelChoiceField(queryset=Level.objects.all(), empty_label='----Select Level---')
    
    class Meta:
        model = MaterialContent
        fields = ['has_sub_content','content','pdf_URL','is_pdf','is_shown','level','material_type','subject']
    def __init__(self, *args, **kwargs):
        super(MaterialContentForm, self).__init__(*args, **kwargs)
        try:
            self.initial['level'] = kwargs['instance'].level.id
        except:
            pass
        level_list = [('', '----Select Level---')] + [(i.id, i.level_name) for i in Level.objects.all()]

        self.fields['level'].widget = forms.Select(
            attrs={
                'id': 'id',
                'onchange': 'getMaterialType(this.value);getSubject(this.value)',
                'style': 'width:200px'
            },
            choices=level_list,
        )

        # Set the initial value of sem_year field to None
        self.fields['material_type'].widget.choices = [('', '----Select Material Type---')]
        self.fields['subject'].widget.choices = [('', '----Select Subject---')]
