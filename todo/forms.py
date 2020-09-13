from django import forms
from .models import ToDoModel, CustomUser


class CreateForm(forms.ModelForm):
    '''タスクを新規作成するときのフォーム'''
    class Meta:
        model = ToDoModel
        fields = ('title', 'memo', 'priority', 'duedate', 'user_name')
        # 締め切り日を設定する時に入力しやすくする．
        widgets = {
            'duedate': forms.SelectDateWidget
        }


class UpdateForm(forms.ModelForm):
    '''タスクを修正するときのフォーム'''
    class Meta:
        model = ToDoModel
        fields = ('title', 'memo', 'priority', 'duedate', 'status')
        # 締め切り日を設定する時に入力しやすくする．
        widgets = {
            'duedate': forms.SelectDateWidget
        }


class ChangeOrderForm(forms.ModelForm):
    '''並び順を変更するときのフォーム'''
    class Meta:
        model = CustomUser
        fields = ('order', 'ascending_or_descending')
