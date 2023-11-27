from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__ (self):
        return self.username

    
