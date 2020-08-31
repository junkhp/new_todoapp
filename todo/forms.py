from django import forms
from .models import ToDoModel

# 新しいタスクを作成するときのフォーム


class CreateForm(forms.ModelForm):

    class Meta:
        model = ToDoModel
        fields = ('title', 'memo', 'priority', 'duedate')
        # 締め切り日を設定する時に入力しやすくする．
        widgets = {
            'duedate': forms.SelectDateWidget
        }

# 既存のタスクに修正を加える時のフォーム


class UpdateForm(forms.ModelForm):
    class Meta:
        model = ToDoModel
        fields = '__all__'
        # 締め切り日を設定する時に入力しやすくする．
        widgets = {
            'duedate': forms.SelectDateWidget
        }
