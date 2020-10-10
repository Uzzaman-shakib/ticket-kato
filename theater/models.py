from django.db import models


class theater_list(models.Model):
        theater_name = models.CharField(max_length = 50)
        
class contacts(models.Model):
    name = models.CharField(max_length=250,default="")
    email = models.CharField(max_length=250,default="")
    subject = models.CharField(max_length=250,default="")
    message = models.CharField(max_length=1000,default="")
