# cat_project/urls.py
from django.contrib import admin
from django.urls import path
from cat_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cat/<int:cat_id>/', views.cat_info, name='cat_info'),
]
