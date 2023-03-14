from django.db import models

class HumidityTemp(models.Model):
    temprature=models.IntegerField()
    humidity=models.IntegerField()
    rectime=models.DateTimeField(auto_now=True)