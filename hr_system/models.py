
from django.db import models

#===========  importing auth details ==============#
from distutils.command.upload import upload
from email.policy import default

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings




#========   Creating employer user table track Employers =========#
class Employer(models.Model):
    employer_id = models.AutoField(primary_key=True) 
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    role = models.CharField(max_length=40, null=False, help_text="Write the company name and your current position")
    company = models.CharField(max_length=40, null=False)
    email = models.EmailField(null=False)
    phone_number = models.CharField( max_length=12 ,null=False, blank=True )
    employee_number = models.IntegerField(null=False,blank=False)
     
    def __str__(self):
        return self.role
    
#========= creating employee user table  ======================#
class Employee(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    employer_name = models.ForeignKey(Employer , on_delete = models.CASCADE)
    role = models.CharField(max_length=40, null=False, help_text="Write Your role in the company")
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField( max_length=12 ,null=False, blank=True )
    id_number =models.CharField( max_length=9 ,null=False, blank=True )
    kra_pin = models.CharField( max_length=15 ,null=False, blank=True )
    

    def __str__(self):
        return self.role
    
#======= Leave and days off work ===================#
class TimeOff(models.Model):
    timeoff_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    comments = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username





#========= Company asset table =====================#
class CompanyAsset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    asset_name = models.CharField(max_length=40, null=False, help_text="E.g Samsung P3 laptop,")
    available = models.BooleanField(null=True)

    def __str__(self):
        return self.asset_name
    

#========== to store inventory  table ============#
class CompanyInventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey(Employer, on_delete=models.CASCADE)    
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)
    asset_id = models.OneToOneField(CompanyAsset, on_delete=models.CASCADE)
    taking = models.DateField(blank=True)
    returning = models.DateField(blank=True)
    returned = models.BooleanField(default=False, help_text='tick this if an item in the inventory has been returned successfully.')

    def __str__(self):
        return self.emp_id.user.username
    




    
GENDER_CHOICES = (('M','Male'),
                      ('F','Female'),)
  
class Employees(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default='M')
    designation = models.CharField(max_length=150)
  
  
    def __str__(self):
        return self.name
    

class EmployeeTask(models.Model):
    task_name = models.CharField(max_length=150)
    employee = models.ForeignKey(Employee,  related_name='tasks',  on_delete=models.CASCADE)
    task_desc = models.CharField(max_length=350)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
  
 
  
    def __str__(self):
        return self.task_name