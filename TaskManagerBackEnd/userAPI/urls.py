from django.urls import path
from . import views

app_name = 'userAPI'

urlpatterns = [
    path('users/get_users/', views.getData),
    path('users/post_users/', views.addData),
    path('users/put_users/<int:pk>/', views.getDataSingleObject),
    path('users/tasks/get_tasks/', views.getTasksData),
    path('users/tasks/add_tasks/', views.addTasksData),
    path('users/tasks/manage_tasks/<int:pk>/', views.putTasksData),
    path('users/tasks/delete_tasks/<int:pk>/', views.deleteTasksData)
]