from django.db import models

# Create your models here.

class Qcategory(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    image=models.ImageField(upload_to='Category_Images/')

    def __str__(self):
        return self.title
    
    class Meta:
         verbose_name_plural='Catergories'
    
class Question(models.Model):
    category=models.ForeignKey(Qcategory, on_delete=models.CASCADE)
    question=models.TextField()
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    time_limit=models.IntegerField()
    level=models.CharField(max_length=100)
    right_option=models.CharField(max_length=100)

def __str__(self):
        return self.question


