from django.db import models

# Create your models here.
class Tips(models.Model):
    total_bill: float
    tip: float
    sex: str
    smoker: str
    day: str
    time: str
    size: int

class Greeting(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    greeting = models.CharField(max_length=20)

    def __repr__(self):
        return f'Greeting({self.name})'
