
#imports
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import  *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

@login_required
def dashboard(request):
    context = {
        # 'sales': Sale.objects.all(),
        # 'purchases': Purchase.objects.all(),
        # 'stocks': Stock.objects.all(),
        'product' : Product.objects.all(),
        'employees': Employee.objects.all(),
        'financial_transactions': FinancialTransaction.objects.all(),
    }
    return render(request, 'main/dashboard.html', context)

# Add other views as needed

#Product Views
@login_required
def product_list(request):
    products = Product.objects.all()
    filter_form = ProductFilterForm(request.GET)
    if filter_form.is_valid():
        if filter_form.cleaned_data['name']:
            products = products.filter(name__icontains=filter_form.cleaned_data['name'])
        if filter_form.cleaned_data['category']:
            products = products.filter(category=filter_form.cleaned_data['category'])
        if filter_form.cleaned_data['supplier']:
            products = products.filter(supplier=filter_form.cleaned_data['supplier'])
    return render(request, 'main/product_list.html', {'products': products, 'filter_form': filter_form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'main/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'main/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'main/product_confirm_delete.html', {'product': product})


# Branch views

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'main/branch_list.html', {'branches': branches})

def branch_detail(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    return render(request, 'main/branch_detail.html', {'branch': branch})

def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm()
    return render(request, 'main/branch_form.html', {'form': form})

def branch_update(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'main/branch_form.html', {'form': form})

def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_list')
    return render(request, 'main/branch_confirm_delete.html', {'branch': branch})

# Employees views
def employee_list(request):
    employees = Employee.objects.all()
    filter_form = EmployeeFilterForm(request.GET)
    if filter_form.is_valid():
        if filter_form.cleaned_data['first_name']:
            employees = employees.filter(first_name__icontains=filter_form.cleaned_data['first_name'])
        if filter_form.cleaned_data['last_name']:
            employees = employees.filter(last_name__icontains=filter_form.cleaned_data['last_name'])
        if filter_form.cleaned_data['branch']:
            employees = employees.filter(branch=filter_form.cleaned_data['branch'])
        if filter_form.cleaned_data['status']:
            employees = employees.filter(status=filter_form.cleaned_data['status'])
    return render(request, 'main/employee_list.html', {'employees': employees, 'filter_form': filter_form})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'main/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'main/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'main/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'main/employee_confirm_delete.html', {'employee': employee})


# # Purchases

# def purchase_list(request):
#     form = PurchaseFilterForm(request.GET or None)
#     purchases = Purchase.objects.all()

#     if form.is_valid():
#         if form.cleaned_data['start_date']:
#             purchases = purchases.filter(date__gte=form.cleaned_data['start_date'])
#         if form.cleaned_data['end_date']:
#             purchases = purchases.filter(date__lte=form.cleaned_data['end_date'])
#         if form.cleaned_data['supplier']:
#             purchases = purchases.filter(supplier__icontains=form.cleaned_data['supplier'])

#     context = {
#         'purchases': purchases,
#         'form': form,
#     }
#     return render(request, 'main/purchase_list.html', context)

# def purchase_detail(request, pk):
#     purchase = get_object_or_404(Purchase, pk=pk)
#     return render(request, 'main/purchase_detail.html', {'purchase': purchase})

# def purchase_create(request):
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('purchase_list')
#     else:
#         form = PurchaseForm()
#     return render(request, 'main/purchase_form.html', {'form': form})

# def purchase_delete(request, pk):
#     purchase = get_object_or_404(Purchase, pk=pk)
#     if request.method == 'POST':
#         purchase.delete()
#         return redirect('purchase_list')
#     return render(request, 'main/purchase_confirm_delete.html', {'purchase': purchase})
