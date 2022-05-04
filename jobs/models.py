
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class usereegistration(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   contact = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   pin = models.CharField(max_length=100,null=True)
   cv_doc = models.ImageField(upload_to='images/', null=True)
#
class companyegistration(models.Model):
   user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   contact = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   pin = models.CharField(max_length=100,null=True)


class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class Complaint(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)

class PostJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    users = models.ForeignKey(usereegistration,on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    language =  models.CharField(max_length=100,null=True)
    date =  models.CharField(max_length=100,null=True)
    time =  models.CharField(max_length=100,null=True)
    money =  models.CharField(max_length=100,null=True)
    jobdesc = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images/',null=True)
    companyname = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100,null=True)


class ViewAppont(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(PostJob,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100)

class AddVacancy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    jobtype = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    jobdesc = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100,null=True)
    qualification = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class AddWorkStatus(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    jobs = models.ForeignKey(PostJob,on_delete=models.CASCADE,null=True)
    statusdesc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    images = models.ImageField(upload_to='images/',null=True)
    status = models.ImageField(max_length=100,null=True)

class ApplyVacancy(models.Model):
    user = models.ForeignKey(usereegistration,on_delete=models.CASCADE)
    vacancy = models.ForeignKey(AddVacancy,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100)
    link = models.URLField(max_length=400,null=True,default='test')
    time = models.TimeField(max_length=400,null=True)
    date = models.CharField(max_length=400,null=True)








