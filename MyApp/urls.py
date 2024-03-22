from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollegesView, DepartmentsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/colleges/', CollegesView.as_view(), name='get_colleges'),
    path('api/departments/', DepartmentsView.as_view(), name='get_departments'),
]
