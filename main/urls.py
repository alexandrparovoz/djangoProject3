
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('create/', views.create),
    path('addtask/', views.add_task),
    path('edittask/', views.edit_task, name='edittask'),
    path('<int: pk>/update', views.TaskUpdateView. as_view(), name='task_update'),
    path('<int: pk>/delete', views.TaskDeleteView. as_view(), name='task_delete'),
    path('<int: pk>', views.TaskDetailView. as_view(), name='task_detail'),

]