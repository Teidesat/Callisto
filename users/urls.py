from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    path('<str:username>/', views.user_detail, name='user-detail'),
]
