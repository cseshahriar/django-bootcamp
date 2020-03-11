from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    '''
    __str__
    A Python “magic method” that returns a string representation of any object. This is what Python and Django will use whenever a model instance needs to be coerced and displayed as a plain string. Most notably, this happens when you display an object in an interactive console or in the admin.
    You’ll always want to define th
    '''
    def __str__(self):
        return self.topic_name  
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) # relationship  
    name  = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    # string representation 
    def __str__(self):
        return self.name 
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date) # obj to str  