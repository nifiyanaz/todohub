from django.db import models

# Create your models here.
# class Tasks(models.Model):
#     task=models.CharField(max_length=100)
#     priority=models.IntegerField()
#     dedline=models.DateField()
 
class Tasks(models.Model):
    title=models.CharField(max_length=100)
    
    
   
    def __str__(self):
        return self.title