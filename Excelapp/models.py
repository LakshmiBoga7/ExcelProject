from django.db import models



class Myexcel(models.Model):

    BANKNAME=models.CharField(max_length=30)
    IFSC = models.CharField(max_length=30)
    OFFICE = models.CharField(max_length=30)
    ADDRESS = models.CharField(max_length=30)
    class Meta:
        db_table='Myexcel'
