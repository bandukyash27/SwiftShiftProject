from django.db import models

# Create your models here.


class ContactDetails(models.Model):
    name=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField(max_length=70)

    def __str__(self):
        return self.name