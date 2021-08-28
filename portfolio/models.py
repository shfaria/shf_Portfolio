from django.db import models

class Project(models.Model):   #every model class is subclass of models.Model
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image= models.ImageField(upload_to= 'portfolio/images/')
    url= models.URLField(blank= True) #blank can be added to anywhere

    def __str__(self):
        return self.title

