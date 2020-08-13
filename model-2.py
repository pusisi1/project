from django.db import models

'''
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
'''
class Korea(models.Model):
#날짜/시각/날씨/강수확률/강수량/기온/습도
# day/time/weather/RP/rain/temp/hum
    day=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    weather=models.CharField(max_length=100)
    RP=models.CharField(max_length=100)
    rain=models.CharField(max_length=100)
    temp=models.CharField(max_length=100)
    hum=models.CharField(max_length=100)

class NORWAY(models.Model):
#시간/날씨/온도/강수량/풍속

#time/weather/temp/rain/wind
    time=models.CharField(max_length=100)
    weather=models.CharField(max_length=100)
    temp=models.CharField(max_length=100)
    rain=models.CharField(max_length=100)
    wind=models.CharField(max_length=100)

class BBC(models.Model):
#시간/온도/강수확률/날씨
#time/temp/RP/weather/
    time=models.CharField(max_length=100)
    temp=models.CharField(max_length=100)
    RP=models.CharField(max_length=100)
    weather=models.CharField(max_length=100)
    


    

