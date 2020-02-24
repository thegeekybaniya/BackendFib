from django.contrib.auth.models import User as DjangoUser
from django.db import models

# Create your models here.

class User(DjangoUser):
    name=models.CharField(max_length=20)

    def __str__(self):
        return "User %s" % self.name.title()



class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return "Admin %s" % self.user.__str__()




class Project(models.Model):
    name= models.CharField(max_length=30)
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return "Employee %s" % self.user.__str__()
