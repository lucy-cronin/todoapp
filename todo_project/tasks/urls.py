from django.urls import path
from .views import *

urlpatterns = [
    path("", task_list, name="home"),
    path("create/", create_task, name="create"),
    path('detail/<str:pk>/', detail_task, name='detail'),
    path('update/<str:pk>/', update_task, name='update'),
    path('delete/<str:pk>/', delete_task, name='delete'),
]