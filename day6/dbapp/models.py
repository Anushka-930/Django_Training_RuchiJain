from django.db import models

# Create your models here.

class Client(models.Model):
    clientid = models.CharField(max_length=100)
    clientname = models.CharField(max_length=100)
    clientcompany = models.CharField(max_length=20)

    def __str__(self):
        return self.clientname


class Customer(models.Model):
    customertid = models.CharField(max_length=100)
    customername = models.CharField(max_length=100)
    customercompany = models.CharField(max_length=20)

    def __str__(self):
        return self.customername


class Order(models.Model):
    orderid = models.CharField(max_length=100)
    ordername = models.CharField(max_length=100)
    ordernumber = models.FloatField()

    def __str__(self):
        return self.ordername
