# forms.py
from django import forms

from core.models import Projects
from django.contrib.auth import get_user_model

class ProjectCreateForm(forms.ModelForm):
    """Project Model"""
    title = forms.CharField(max_length=255)
    start_date = forms.DateField()
    end_date = forms.DateField()
    team_lead = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all())
    costing = forms.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        model = Projects
        fields = ('title', 'description', 'start_date', 'end_date', 'team_lead', 'costing')