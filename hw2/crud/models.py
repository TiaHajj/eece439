from django.db import models

class Datbase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    profession = models.CharField(max_length=200, default='')
    date= models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    database = models.ForeignKey(Datbase, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    


# Create your models here.
