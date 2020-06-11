from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    social_media = models.CharField(max_length=300)
    hobbies = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = 'Registrado'
