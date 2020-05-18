from django.db import models
from django.utils import timezone
# Create your models here.


class Patient(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=400, default='')
    phone_mobile = models.CharField(max_length=20)
    phone_landline = models.CharField(max_length=20)
    created_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.last_name, self.first_name
