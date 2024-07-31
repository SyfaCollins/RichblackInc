from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
  path('', views.dashboard, name='dashboard'),
    path('purchases/', views.purchase_list, name='purchase_list'),
    path('purchases/<int:pk>/', views.purchase_detail, name='purchase_detail'),
    path('purchases/new/', views.purchase_create, name='purchase_create'),
    path('purchases/<int:pk>/delete/', views.purchase_delete, name='purchase_delete'),
    path('branches/', views.branch_list, name='branch_list'),
    path('branches/<int:pk>/', views.branch_detail, name='branch_detail'),
    path('branches/new/', views.branch_create, name='branch_create'),
    path('branches/<int:pk>/edit/', views.branch_update, name='branch_update'),
    path('branches/<int:pk>/delete/', views.branch_delete, name='branch_delete'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/new/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),

]
