from django import forms
from .models import *

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