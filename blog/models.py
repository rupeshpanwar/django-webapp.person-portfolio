from django.db import models

# Create your models here.
class Blog(models.Model):
    blogtitle = models.CharField(max_length = 100)
    date = models.DateField(auto_now=True)
    blogdescription = models.CharField(max_length = 1000)


    def __str__(self):
        return self.blogtitle
