from django.db import models

class HumidityTemp(models.Model):
    temprature=models.IntegerField()
    humidity=models.IntegerField()
    rectime=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'HumidityTemp'

    

class UserDetails(models.Model):
    phone_number=models.TextField(max_length=14)
    user_password=models.TextField(max_length=30)
    class Meta:
        db_table = 'UserDetail'

    def __str__(self):
        return self.phone_number
    
