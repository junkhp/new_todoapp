from django import forms
from .models import ToDoModel


class CreateForm(forms.ModelForm):

    class Meta:
        model = ToDoModel
        fields = ('title', 'memo', 'priority', 'duedate')
        widgets = {
            'duedate': forms.SelectDateWidget
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = '__all__'
        widgets = {
            'duedate': forms.SelectDateWidget
        }
