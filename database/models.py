from django.db import models

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=100)
    name = models.CharField(max_length=10)

class Article(models.Model):
   
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class database_test(models.Model):
    date = models.CharField(max_length=50, primary_key=True)
    temper1 = models.CharField(max_length=50)
    temper2 = models.CharField(max_length=50)
    rain = models.CharField(max_length=50)
    wind = models.CharField(max_length=50)
    raintype = models.CharField(max_length=50)

    class Meta:
        db_table = "database_test"   

class database_raintest(models.Model):
    date = models.CharField(max_length=50, primary_key=True)
    temper1 = models.CharField(max_length=50)
    temper2 = models.CharField(max_length=50)
    rain = models.CharField(max_length=50)
   
    class Meta:
        db_table = "database_raintest"  

class database_content(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=50)

    class Meta:
        db_table = "database_content" 
    
class KOREA(models.Model):
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

        


