
from django.db import models
from users.models import User




class Tag(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Categories (models.Model):
    categ=  models.CharField(max_length=1000)    
    def __str__ (self):
        return self.categ



# Create your models here.
class Project (models.Model):
    title=  models.CharField(max_length=25)
    details=models.CharField(max_length=250)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)    
    total_target=models.FloatField(default=0)
    image = models.FileField(blank=True,upload_to = 'images/',null=True)
    Tags=models.ManyToManyField( 'Tag' ,related_name="projects", blank=True)
    sdate=models.DateField(null=True)
    edate=models.DateField(null=True)
    reported= models.BooleanField(default=False)
    Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
    )   
    donate=models.FloatField(default=0)
    rate = models.IntegerField(choices=Rating_CHOICES, default=1)
    avg_rate=models.FloatField(default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    

    def __str__ (self):
        return self.title


class Comment (models.Model):
    comment=  models.CharField(max_length=1000)
    project= models.ForeignKey(Project,on_delete=models.CASCADE,null=True)
    reported= models.BooleanField(default=False)
    
    def __str__ (self):
        return self.comment



class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    name=models.CharField(max_length=1000,default="")
    def __str__(self):
        return self.name


