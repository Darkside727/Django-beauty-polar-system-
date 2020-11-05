from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_status(models.Model):
    status = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.status

class registration(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    status = models.ForeignKey(User_status, on_delete=models.CASCADE, null= True)
    name = models.CharField(max_length=50, null=True)
    last = models.CharField(max_length=10, null=True)
    contact = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.email

class Service(models.Model):
    name = models.CharField(max_length=100, null = True)
    cost = models.IntegerField(null = True)
    image = models.FileField(upload_to='images')
    decs = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class BookStatus(models.Model):
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.status

class BookPaid(models.Model):
    paid = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.paid

class Apponitment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(registration, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(BookStatus, on_delete=models.CASCADE, null=True)
    paid = models.ForeignKey(BookPaid, on_delete=models.CASCADE, null=True)
    date1 = models.DateField(null=True)
    time1 = models.TimeField(null=True)

    def __str__(self):
        return self.customer.user.username+" "+self.service.name

