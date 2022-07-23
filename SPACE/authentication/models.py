from asyncio.base_subprocess import WriteSubprocessPipeProto
from email.headerregistry import Address
import imp
from platform import mac_ver
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class signup_organization(models.Model):
    Name_organization=models.CharField(max_length=150)
    address=models.TextField()
    Website=models.TextField()
    Email_ID=models.CharField(max_length=100)
    Contact_Number_Organization=models.CharField(max_length=13)
    Contact_Person=models.CharField(max_length=50)
    Confirm_Password=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    Organization=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name_organization

class signup_student(models.Model):
    Student_firstname=models.CharField(max_length=50)
    Student_lastname=models.CharField(max_length=50)
    Student_mailid=models.CharField(max_length=100)
    Student_contact_number=models.CharField(max_length=13)
    Student_address=models.TextField()
    Student_org_name=models.CharField(max_length=150)
    Student_dept_name=models.CharField(max_length=50)
    Student_program_id=models.CharField(max_length=50)
    Student_confirm_password=models.CharField(max_length=50)
    date_posted=models.DateTimeField(default=timezone.now)
    Student=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Student_firstname

class signup_freelancer(models.Model):
    Freelancer_name=models.CharField(max_length=150)
    address=models.TextField()
    Email_ID=models.CharField(max_length=100)
    Contact_Number_Freelancer=models.CharField(max_length=50)
    Confirm_Password=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    Freelancer=models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.Freelancer_name




