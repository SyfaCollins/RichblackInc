from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('', views.dashboard, name='dashboard'),
  path('products/', views.product_list, name='product_list'),
  path('products/<int:pk>/', views.product_detail, name='product_detail'),
  path('products/new/', views.product_create, name='product_create'),
  path('products/<int:pk>/edit/', views.product_update, name='product_update'),
  path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
  
  path('product_category/', views.product_category_list, name='product_category_list'),
  path('product_category/new/', views.product_category_create, name='product_category_create'),
  
# 
  path('stock/', views.product_list, name='stock_list'),
  path('stock/<int:pk>/', views.product_detail, name='stock_detail'),
  path('stock/new/', views.product_create, name='stock_create'),
  path('stock/<int:pk>/edit/', views.product_update, name='product_update'),
  path('stock/<int:pk>/delete/', views.product_delete, name='product_delete'),
  
  path('transfers/', views.transfer_list, name='transfer_list'),
  path('transfers/<int:pk>/', views.transfer_detail, name='transfer_detail'),
  path('transfers/new/', views.transfer_create, name='transfer_create'),
  
  path('sales/', views.sale_list, name='sale_list'),
  path('sales/<int:pk>/', views.sale_detail, name='sale_detail'),
  path('sales/new/', views.sale_create, name='sale_create'),
  
  # Supplier
  
  path('supplier/', views.supplier_list, name='supplier_list'),
  path('supplier/<int:pk>/', views.supplier_detail, name='supplier_detail'),
  path('supplier/new/', views.supplier_create, name='supplier_create'),
  path('supplier/<int:pk>/edit/', views.supplier_update, name='supplier_update'),
  path('supplier/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
  
  
  path('purchases/', views.purchase_list, name='purchase_list'),
  path('purchases/<int:pk>/', views.purchase_detail, name='purchase_detail'),
   path('purchases/<int:pk>/edit/', views.purchase_update, name='purchase_update'),
  path('purchases/new/', views.purchase_create, name='purchase_create'),
  path('purchases/<int:pk>/delete/', views.purchase_delete, name='purchase_delete'),
  
  path('purchases/multiple/', views.create_multiple_purchases, name='create_multiple_purchases'),
  path('purchases/upload/', views.upload_purchases, name='upload_purchases'),


  
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
