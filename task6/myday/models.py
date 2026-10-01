from django.db import models

class Product(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=100)
    pprice = models.FloatField()
    poffer = models.IntegerField()

    def __str__(self):
        return self.pname
