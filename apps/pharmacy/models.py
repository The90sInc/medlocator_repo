from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Pharmacy(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=60, help_text='Required. Add a valid email')
    # account_manager = models.CharField(max_length=150)
    # account_manager_phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='pharmacy', on_delete=models.CASCADE)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

