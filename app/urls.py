from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view, name='index'),
    path('rolls/', views.index_rolls, name='rolls'),
    path('set/', views.index_set, name='set'),
    path('napitki/', views.index_napitki, name='napitki'),
    path('user_register/', views.user_register, name='register'),
    path('user_login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]