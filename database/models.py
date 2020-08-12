from django.db import models

# Create your models here.
class database_test(models.Model):
    date = models.CharField(max_length=50, primary_key=True)
    temper1 = models.CharField(max_length=50)
    temper2 = models.CharField(max_length=50)
    rain = models.CharField(max_length=50)
    wind = models.CharField(max_length=50)
    raintype = models.CharField(max_length=50)

    class Meta:
        db_table = "database_test"