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


class NeighbourHood(models.Model):
    name=models.CharField(max_length=50,null=False)
    location=models.CharField(max_length=50,null=False)
    occupants_count=models.IntegerField(default=0,null=False)
    admin=models.ForeignKey(Admin, on_delete=CASCADE,null=True)

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
       pass

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        pass
