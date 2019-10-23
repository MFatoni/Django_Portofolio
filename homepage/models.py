from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=27)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField()
    
    def __str__(self):
        return self.message
