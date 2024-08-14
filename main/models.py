from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_info = models.IntegerField()
    address = models.CharField(max_length=255)
    email_address = models.EmailField()
    
    def __str__(self):
        return self.name
    

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
    stock_quantity = models.IntegerField()
   

    def __str__(self):
        return self.name
    



class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        
        return f"Purchase {self.purchase_id} of {self.product.name}"


class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=50, unique=True, default='DEFAULT_CODE')
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=20)
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
    
    
    
class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('product', 'branch')

    def __str__(self):
        return f"{self.product.name} in {self.branch.branch_name}"
    
class StockTransfer(models.Model):
    transfer_id = models.AutoField(primary_key=True)
    from_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='outgoing_transfers')
    to_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='incoming_transfers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transfer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transfer {self.transfer_id} of {self.product.name} from {self.from_branch.branch_name} to {self.to_branch.branch_name}"

    
    
@receiver(post_save, sender=Purchase)
def update_product_stock(sender, instance, **kwargs):
    product = instance.product
    product.stock_quantity += instance.quantity
    product.save()


@receiver(post_save, sender=StockTransfer)
def update_stock_quantities(sender, instance, **kwargs):
    from_branch_stock = Stock.objects.get(branch=instance.from_branch, product=instance.product)
    to_branch_stock, created = Stock.objects.get_or_create(branch=instance.to_branch, product=instance.product)

    # Update quantities
    from_branch_stock.quantity -= instance.quantity
    from_branch_stock.save()
    
    to_branch_stock.quantity += instance.quantity
    to_branch_stock.save()    
    
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.quantity} {self.product.name} at {self.branch.branch_name} on {self.sale_date}"

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
