from django.urls import path
from .views import Tasklist, Taskdetail, Taskcreate, Taskupdate, DeleteView, Customloginview, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('login/', Customloginview.as_view(), name= 'customloginview'),
        path('logout/', LogoutView.as_view(next_page= 'customloginview'), name= 'logout'),
        path('register/', Register.as_view(), name= 'register'),
        path('', Tasklist.as_view(), name='tasks'),
        path('task/<int:pk>/', Taskdetail.as_view(), name='taskdetail'), 
        path('create-task/', Taskcreate.as_view(), name= 'createtask'),
        path('update-task/<int:pk>/', Taskupdate.as_view(), name= 'task-update'),
        path('delete-task/<int:pk>/', DeleteView.as_view(), name= 'task-delete'),
]