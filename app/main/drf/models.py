from django.db import models

# Create your models here.

class Account(models.Model):
    account_options = (
        ("savings","SAVINGS"),
        ("checking","CHECKING"),
        ("credit","CREDIT"),
    )
    
    product = models.CharField(
        max_length=30,
        choices = account_options,
        default = account_options[0])
    
    customer_email = models.EmailField(max_length=100)

    def __str__ (self): 
        return f" Name: {self.user_name} | Email: {self.email} | Account Type: {self.product}"



    
