from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Ticket(models.Model):
    movie_name = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    hall_type = models.CharField(max_length=250)
    total_seat= models.CharField(max_length=250)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        image =Image.open(self.image.path)
        
        if image.height > 300 or image.width > 300:
            output_size = (300,300)
            image.thumbnail(output_size)
            image.save(self.image.path)
        
class Payment(models.Model):
    banking_name = models.CharField(max_length=250, default="")
    account_no= models.CharField(max_length=250,default="")
    password=models.CharField(max_length=250,default="")
   
    
    