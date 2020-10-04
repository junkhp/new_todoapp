# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import ToDoModel, CustomUser
from django.urls import reverse_lazy
from django.views import View
from .forms import CreateForm, UpdateForm, ChangeOrderForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class TodoListView(ListView):
    # memo LoginRequiredMixinとListViewの順番を入れ替えるとうまくいかない
    '''タスクの一覧を表示'''

    def get(self, request):
        # ログイン中のユーザー名を取得
        user_name = request.user.username
        # ユーザーに対応したリストの表示順の方法を取得(作成した順，締め切り順，優先度順)
        # order = HowtoOrder.objects.get(user_name=user_name).order
        order = CustomUser.objects.get(username=user_name).order
        # 昇順か降順を取得
        # ascending_or_descending = HowtoOrder.objects.get(
        # user_name=user_name).ascending_or_descending
        ascending_or_descending = CustomUser.objects.get(
            username=user_name).ascending_or_descending

        # ログイン中のユーザーのタスクを取得
        user_tasks = ToDoModel.objects.filter(user_name=user_name)

        # 表示順と昇順・降順の情報を下にリストを並べ替え
        if order == 'creation_order':
            if ascending_or_descending == 'ascending':
                tasks = user_tasks.filter(status='doing')
            elif ascending_or_descending == 'descending':
                tasks = user_tasks.filter(status='doing').order_by('-pk')

        elif order == 'due_order':
            if ascending_or_descending == 'ascending':
                tasks = user_tasks.filter(status='doing').order_by('duedate')
            elif ascending_or_descending == 'descending':
                tasks = user_tasks.filter(status='doing').order_by('-duedate')

        elif order == 'priority_order':
            if ascending_or_descending == 'ascending':
                tasks = user_tasks.filter(status='doing').order_by('priority', 'duedate')
            elif ascending_or_descending == 'descending':
                tasks = user_tasks.filter(status='doing').order_by('-priority', 'duedate')
        context = {
            'user_name': user_name,
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
        # ログイン中のユーザー名を取得
        user_name = request.user.username
        # statusが"done"のタスクを取得
        archive = ToDoModel.objects.filter(user_name=user_name, status='done')
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
        return render(request, 'todo/create2.html', context)

    def post(self, request, *args, **kwargs):
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return redirect('create')


class TodoUpdateView(View):
    '''タスクを編集'''

    def get(self, request, pk, *args, **kwargs):
        task = ToDoModel.objects.get(pk=pk)
        context = {
            'form': UpdateForm(instance=task),
        }
        return render(request, 'todo/update.html', context)

    def post(self, request, pk, *args, **kwargs):
        task = ToDoModel.objects.get(pk=pk)
        form = UpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return redirect('create')


class HowtoOrderUpdateView(View):
    '''タスクの並び順を変更'''

    def get(self, request, *args, **kwargs):
        # ログイン中のユーザー名を取得
        user_name = request.user.username
        order = CustomUser.objects.get(username=user_name)
        context = {
            'form': ChangeOrderForm(instance=order),
        }
        return render(request, 'todo/update_order.html', context)

    def post(self, request, *args, **kwargs):
        # ログイン中のユーザー名を取得
        user_name = request.user.username
        order = CustomUser.objects.get(username=user_name)
        form = ChangeOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return redirect('create')


# class HowtoOrderUpdateView(UpdateView):
#     '''タスクの並び順を変更'''
#     model = HowtoOrder
#     template_name = "todo/update_order.html"
#     fields = '__all__'
#     success_url = reverse_lazy('list')


class SignupView(View):
    '''サインアップ'''

    def get(self, request, *args, **kwargs):
        return render(request, 'todo/signup.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        # ユーザーを追加
        try:
            CustomUser.objects.get(username=username)
            return render(request, 'todo/signup.html', {'error': 'このユーザー名は既に登録されています．'})
        except:
            user = CustomUser.objects.create_user(username, '', password)
            # 新しいユーザーが作成されたタイミングで並び順モデルに新しいデータを追加
            # HowtoOrder.objects.create(user_name=username)
            return redirect('login')


class LoginView(View):
    '''ログイン'''

    def get(self, request, *args, **kwargs):
        return render(request, 'todo/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')


def logoutfunc(request):
    logout(request)
    return redirect('login')
