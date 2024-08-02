from django.db import models

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class UnitOfMeasure(models.Model):
    unit_name = models.CharField(max_length=100)
    
class ProductCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=50, unique=True, default='DEFAULT_CODE')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    manager_name = models.CharField(max_length=255)
    opening_date = models.DateField()
    operating_hours = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    number_of_employees = models.IntegerField()
    services_offered = models.TextField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('renovation', 'Under Renovation')])

    def __str__(self):
        return self.branch_name
    
from django.db import models


#employees

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    position = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    address = models.TextField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FinancialAccount(models.Model):
    account_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class FinancialTransaction(models.Model):
    account = models.ForeignKey(FinancialAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=6, choices=[('Credit', 'Credit'), ('Debit', 'Debit')])
    transaction_date = models.DateField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
