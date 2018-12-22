# Create your models here.
from django.db import models


# admin can register merchant
class CreateMerchant(models.Model):
    # Owner Info
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    address = models.TextField(blank=True)

    # Business Info
    business_name = models.CharField(max_length=100)
    model_CHOICES = (('1', 'New York'), ('2', 'Jackson Heights '))
    business_model = models.CharField(choices=model_CHOICES, max_length=50, default='1')
    website = models.CharField(max_length=100)
    fb_page = models.CharField(max_length=100)

    # Payment Info
    bank_CHOICES = (('1', 'Bank'), ('2', 'Cash '), ('3', 'Wallet '))
    bank_detail = models.CharField(choices=bank_CHOICES, max_length=50, default='2')
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    routing = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    # Mobile Wallet
    wallet_CHOICES = (('1', 'Bank'), ('2', 'Cash '), ('3', 'Wallet '))
    wallet_type = models.CharField(choices=wallet_CHOICES, max_length=50, default='2')
    wallet_number = models.CharField(max_length=100)

    # contact Info
    cFirstName = models.CharField(max_length=100)
    cLastName = models.CharField(max_length=100)
    cPhnNo = models.CharField(max_length=100)
    cEmail = models.CharField(max_length=100)
    agree = models.BooleanField(default=True)

    def __str__(self):
        return self.firstName

