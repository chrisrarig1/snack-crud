from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    title = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return_string = f'{self.title} {self.purchaser} {self.description}'
        # return self.name,self.purchaser,self.description
        return return_string
    
    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])

# Create your models here.
