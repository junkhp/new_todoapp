from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ToDoModel, HowtoOrder
from django.urls import reverse_lazy
from django.views import View
from .forms import CreateForm, UpdateForm
from django import forms
# Create your views here.


class TodoListView(ListView):
    def get(self, request):
        order = HowtoOrder.objects.get(pk=1).order
        ascending_or_descending = HowtoOrder.objects.get(pk=1).ascending_or_descending
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


listview = TodoListView.as_view()


class TodoDetailView(DetailView):
    template_name = 'todo/detail.html'
    model = ToDoModel


class TodoDeleteView(DeleteView):
    template_name = 'todo/delete.html'
    model = ToDoModel
    success_url = reverse_lazy('list')


class TodoArchiveView(ListView):
    def get(self, request):
        archive = ToDoModel.objects.filter(status='done')
        context = {
            'archive': archive,
        }
        return render(request, 'todo/archive.html', context)


def task_status_move(request, pk):
    task = ToDoModel.objects.get(pk=pk)
    status = task.status
    if status == 'doing':
        task.status = 'done'
    if status == 'done':
        task.status = 'doing'
    task.save()
    return redirect(request.META['HTTP_REFERER'])


class TodoCreateView(View):
    def get(self, request, *args, **kwargs):
        """GETリクエスト用のメソッド"""

        context = {
            'form': CreateForm(),
        }
        # ログイン画面用のテンプレートに値が空のフォームをレンダリング
        return render(request, 'todo/create.html', context)

    def post(self, request, *args, **kwargs):
        """POSTリクエスト用のメソッド"""
        # リクエストからフォームを作成
        form = CreateForm(request.POST)
        form.save()
        return redirect('list')


class TodoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        task = ToDoModel.objects.get(pk=pk)
        context = {
            'form': UpdateForm(instance=task),
        }
        # ログイン画面用のテンプレートに値が空のフォームをレンダリング
        return render(request, 'todo/update.html', context)

    def post(self, request, pk, *args, **kwargs):
        task = ToDoModel.objects.get(pk=pk)
        form = UpdateForm(request.POST, instance=task)
        form.save()
        return redirect('list')


class HowtoOrderUpdateView(UpdateView):
    model = HowtoOrder
    template_name = "todo/update_order.html"
    fields = '__all__'
    success_url = reverse_lazy('list')
