from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Customer(models.Model):
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    phone = models.IntegerField()
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone} {self.email}"

    def get_absolute_url(self):
        return f"/customers/{self.id}/"


class Invest(models.Model):
    invest_name = models.CharField(max_length=40)
    adress = models.CharField(max_length=50)
    no_of_apartments = models.IntegerField()
    www = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.invest_name} {self.no_of_apartments} {self.www}"


class Apartment(models.Model):
    nr = models.IntegerField()
    m2 = models.IntegerField()
    invest = models.ForeignKey(Invest, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nr} {self.m2} {self.invest.invest_name}"


class Offer(models.Model):
    client = models.ForeignKey("Customer", on_delete=models.PROTECT)
    invest = models.ForeignKey("Invest", on_delete=models.PROTECT)
    apartment = models.ForeignKey("Apartment", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} {self.invest.invest_name} {self.apartment.nr}"


class Contract(models.Model):
    offer = models.ForeignKey("Offer", on_delete=models.SET_NULL, null=True)