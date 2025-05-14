from django import forms

from .models import Projects


class AddProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EditProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
