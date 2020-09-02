from django.urls import path
from . import views

urlpatterns = [
    # path('todo/', views.todo, name='todo'),
    path('', views.TodoListView.as_view(), name='first'),
    path('list/', views.TodoListView.as_view(), name='list'),
    path('detail/<int:pk>', views.TodoDetailView.as_view(), name='detail'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name='update'),
    path('archive/', views.TodoArchiveView.as_view(), name='archive'),
    path('move/<int:pk>', views.task_status_move, name='move'),
    path('changeorder/<int:pk>', views.HowtoOrderUpdateView.as_view(), name='changeorder'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutfunc, name='logout'),
]
