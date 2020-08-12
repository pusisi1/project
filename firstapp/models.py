from django.db import models

# Create your models here.
class Korea(models.Model):
#날짜/기온/강수량/습도/풍속/풍향
# day/temp/rain/hum/ws/wd
# char/integer/integer/integer/integer/integer/
    day=models.CharField(max_length=30)
    temp=models.CharField(max_length=30)
    rain=models.CharField(max_length=30)
    hum=models.CharField(max_length=30)
    ws=models.CharField(max_length=30)
    wd=models.CharField(max_length=30)
    

