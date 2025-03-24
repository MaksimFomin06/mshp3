from django.db import models

# Create your models here.

class CalculatorDB(models.Model):
    number_one: models.IntegerField = models.IntegerField()
    number_two: models.IntegerField = models.IntegerField()
    number_ans: models.IntegerField = models.IntegerField()
