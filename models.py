from django.db import models
from django.db import models


# Create your models here.

class Admin(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_admin(self):
        self.save()

    def delete_admin(self):
        self.delete()

# Create your models here.
