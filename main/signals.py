from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase, Stock, Branch, Product

@receiver(post_save, sender=Purchase)
def update_main_branch_stock(sender, instance, created, **kwargs):
    if created:  # Only run this if the purchase is newly created
        # Fetch the Main Branch (ensure you have a branch named 'Main_Branch')
        try:
            main_branch = Branch.objects.get(branch_name='Main_Branch')
        except Branch.DoesNotExist:
            main_branch = None
        
        if main_branch:
            # Update the stock for the purchased product at the Main Branch
            stock, created = Stock.objects.get_or_create(
                branch=main_branch,
                product=instance.product
            )
            # Add the purchased quantity to the main branch stock
            stock.quantity = stock.quantity + instance.quantity
            stock.save()
