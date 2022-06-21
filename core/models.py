from django.db import models

# Create your models here.
class Send_message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=360 )
    message = models.TextField(max_length=1500)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Message'

class Denote_informations(models.Model):

    fname = models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email = models.EmailField(max_length=360)
    phone = models.CharField(max_length=25)
    age=models.IntegerField()
    class_room=models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    booktype=models.CharField(max_length=100)
    img=models.ImageField(upload_to='img/%y/%m/%d')
    message=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.fname +' '+ self.lname
    class Meta:
        verbose_name = 'Denote Informations'