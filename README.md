This project is based out of Django3 about Personal Portfolio<br />
here are commands used to create the project in python3 <br />
django-admin startproject personal_portfolio <br />
#create webapp say blog <br />
python3 manage.py startapp blog <br />
#add another webapp say portfolio <br />
python3 manage.py startapp portfolio <br />
# section 2 add these app to settings.py <br />
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'portfolio',
]
'''

#check the lending page <br />
python3 manage.py runserver <br />

#now to save info into Db, there are models available to interact with Db
, these are mapped thorugh "class" that basically represents a "table" and <br />
properties of the class represents "column" in the table <br />

#now under portfolio app -> models.py file
from django.db import models
'''
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    image = models.URLField(blank=True)
'''

