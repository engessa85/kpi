from django import forms
from .models import ProjectForm

class ProjectFormModel(forms.ModelForm):
    class Meta:
        model = ProjectForm
        fields = '__all__'  # Include all fields
        exclude = ['user', 'progress']  # User will be assigned automatically