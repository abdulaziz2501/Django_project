from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name=models.CharField(max_length=100, blank=False, null=False)
    user_name=models.CharField(max_length=100, blank=False, null=False)
    phone_number=models.CharField(max_length=11, blank=False, null=False)
    email=models.CharField(max_length=100, blank=False, null=False)
    password=models.CharField(max_length=100, blank=False, null=False)
    confirm_password=models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
