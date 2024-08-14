from django import forms
from .models import *


#product Category

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
        
# class ProductCategoryFilterForm(forms.Form):
#     name = forms.CharField(required=False)
#     category = forms.CharField(required=False)
#     description = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)

# products form

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False)
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), required=False)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)
    
    
# Stock Management

class StockTransferForm(forms.ModelForm):
    class Meta:
        model = StockTransfer
        fields = ['product', 'from_branch', 'to_branch', 'quantity']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class PurchaseFilterForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    supplier = forms.CharField(max_length=100, required=False)


#Branches form

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        
        
        
        
# Sales

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'branch', 'quantity', 'sale_price']
        
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


#Employees form

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeFilterForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=False)
    status = forms.ChoiceField(choices=[('active', 'Active'), ('inactive', 'Inactive')], required=False)
    
    