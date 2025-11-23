from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=15, unique=True)
    addhar=models.CharField(max_length=20, unique=True)
    state=models.CharField(max_length=50)
    pin=models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    # accountID=models.AutoField(primary_key=True)

    class Meta:
        db_table = 'user_account'

    
class customeradd(models.Model):
    accnumber=models.CharField(primary_key=True,unique=True,max_length=100)
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=150, unique=True)
    pan=models.CharField(max_length=150, unique=True)
    aadhaar=models.CharField(max_length=20, unique=True)
    amount=models.IntegerField()

    class Meta:
        db_table = 'customer_add'

    # def __str__(self):
    #     return self.username