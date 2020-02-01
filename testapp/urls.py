from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_login, name="user_login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('user-profile/', views.user_profile, name="user_profile"),

    path('department/<slug:slug>/', views.department, name="department"),   
    path('department/<int:id>/<slug:slug>/', views.department, name="department"),   
]
