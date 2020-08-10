from django.db import models

# Create your models here.

class profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class clgdet(models.Model):
    name = models.ForeignKey(profile, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    school = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)

class othdet(models.Model):
    name = models.ForeignKey(profile, on_delete=models.CASCADE)
    prefloc = models.CharField(max_length=100)
    curloc = models.CharField(max_length=15)
    pskills = models.CharField(max_length=100)
    sskills = models.CharField(max_length=100)
