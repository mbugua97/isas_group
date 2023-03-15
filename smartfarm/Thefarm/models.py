from django.db import models

class HumidityTemp(models.Model):
    temprature=models.IntegerField()
    humidity=models.IntegerField()
    rectime=models.DateTimeField(auto_now=True)

class UserDetails(models.Model):
    phone_number=models.TextField(max_length=14)
    user_password=models.TextField(max_length=30)
