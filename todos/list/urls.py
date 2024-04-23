from django.urls import path
from . import views

urlpatterns = [
    path('todo/<uuid:project_id>/', views.todo, name='todo'),
    path('proj/', views.project, name='proj'),
    path('login/', views.loginpage, name='loginpage'),
    path('add_todo_ajax/<str:description>', views.add_todo_ajax, name='add_todo_ajax'),
    path('update_todo_status/<uuid:id>/', views.update_todo_status, name='update_todo_status'),
    path('edit/<str:description>/', views.eedit, name='edit'),
    path('delete/<str:description>',views.dtl,name='delete'),
    path('allproject',views.allproject),
     path('oneproject/<int:id>',views.oneproject),
]

