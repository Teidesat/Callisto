from django.urls import path

from . import views

app_name = 'departments'


urlpatterns = [
    path('', views.department_list, name='department-list'),
    path('<department_code>/', views.department_detail, name='department-detail'),
    path('<department_code>/projects/add/', views.add_project, name='add-project'),
    path(
        '<department_code>/projects/<project_pk>/edit/',
        views.edit_project,
        name='edit-project',
    ),
    path(
        '<department_code>/projects/<project_pk>/delete/',
        views.delete_project,
        name='delete-project',
    ),
    path(
        '<department_code>/projects/<project_pk>/',
        views.project_detail,
        name='project-detail',
    ),
]
