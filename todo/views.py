from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ToDoModel, HowtoOrder
from django.urls import reverse_lazy
from django.views import View
from .forms import CreateForm, UpdateForm
from django import forms
# Create your views here.


class TodoListView(ListView):
    '''タスクの一覧を表示'''

    def get(self, request):
        # リストの表示順の方法を取得(作成した順，締め切り順，優先度順)
        order = HowtoOrder.objects.get(pk=1).order
        # 昇順か降順を取得
        ascending_or_descending = HowtoOrder.objects.get(pk=1).ascending_or_descending

        # 表示順と昇順・降順の情報を下にリストを並べ替え
        if order == 'creation_order':
            if ascending_or_descending == 'ascending':
                tasks = ToDoModel.objects.filter(status='doing')
            elif ascending_or_descending == 'descending':
                tasks = ToDoModel.objects.filter(status='doing').order_by('-pk')

        elif order == 'due_order':
            if ascending_or_descending == 'ascending':
                tasks = ToDoModel.objects.filter(status='doing').order_by('duedate')
            elif ascending_or_descending == 'descending':
                tasks = ToDoModel.objects.filter(status='doing').order_by('-duedate')

        elif order == 'priority_order':
            if ascending_or_descending == 'ascending':
                tasks = ToDoModel.objects.filter(status='doing').order_by('priority', 'duedate')
            elif ascending_or_descending == 'descending':
                tasks = ToDoModel.objects.filter(status='doing').order_by('-priority', 'duedate')
        context = {
            'tasks': tasks,
        }
        return render(request, 'todo/list.html', context)


class TodoDetailView(DetailView):
    '''タスクの詳細を表示'''
    template_name = 'todo/detail.html'
    model = ToDoModel


class TodoDeleteView(DeleteView):
    '''タスクを削除'''
    template_name = 'todo/delete.html'
    model = ToDoModel
    success_url = reverse_lazy('list')


class TodoArchiveView(ListView):
    '''完了済みのタスクを一覧表示'''

    def get(self, request):
        # statusが"done"のタスクを取得
        archive = ToDoModel.objects.filter(status='done')
        context = {
            'archive': archive,
        }
        return render(request, 'todo/archive.html', context)


def task_status_move(request, pk):
    '''タスクのstatusが完了か未完了かを切替'''
    task = ToDoModel.objects.get(pk=pk)
    status = task.status
    if status == 'doing':
        task.status = 'done'
    if status == 'done':
        task.status = 'doing'
    task.save()
    return redirect(request.META['HTTP_REFERER'])


class TodoCreateView(View):
    '''新しいタスクを追加'''

    def get(self, request, *args, **kwargs):
        context = {
            'form': CreateForm(),
        }
        return render(request, 'todo/create.html', context)

    def post(self, request, *args, **kwargs):
        form = CreateForm(request.POST)
        form.save()
        return redirect('list')


class TodoUpdateView(View):
    '''タスクを追加'''

    def get(self, request, pk, *args, **kwargs):
        task = ToDoModel.objects.get(pk=pk)
        context = {
            'form': UpdateForm(instance=task),
        }
        return render(request, 'todo/update.html', context)

    def post(self, request, pk, *args, **kwargs):
        task = ToDoModel.objects.get(pk=pk)
        form = UpdateForm(request.POST, instance=task)
        form.save()
        return redirect('list')


class HowtoOrderUpdateView(UpdateView):
    '''タスクの並び順を変更'''
    model = HowtoOrder
    template_name = "todo/update_order.html"
    fields = '__all__'
    success_url = reverse_lazy('list')
