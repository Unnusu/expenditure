from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thestart(models.Model):
    expense = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.expense
    
    class Meta:
        db_table = 'THESTART'
    
    
    