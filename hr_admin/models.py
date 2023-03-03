from django.db import models

# Create your models here.



GENDER_CHOICES = (('M','Male'),
                      ('F','Female'),)
  
class Employee(models.Model):
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
    employee = models.ForeignKey(Employee,
                                  related_name='tasks',
                                  on_delete=models.CASCADE)
    task_desc = models.CharField(max_length=350)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
  
 
  
    def __str__(self):
        return self.task_name