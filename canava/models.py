from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SoftTech_Student_id(models.Model):
    
    age_old = {
        ('Under 19','Under 19'),
        ('19 or Older','19 or Older')
    }
    job_r = {
        ('Office Management','Office Management'),
        ('Grapics Design','Grapics Design'),
        ('Web Development (Python,Django)','Web Development (Python,Django)'),
        ('Web Development (Django)','Web Development (Django)'),
        ('Python Programming','Python Programming'),
        ('Digital Marketing','Digital Marketing'),
        
    }
    interest_m = {
        ('Development','Development'),
        ('Design','Design'),
        ('Marketing','Marketing'),
    }
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=150)
    age = models.CharField(max_length=150)
    biography = models.TextField(max_length=150)
    course_name = models.CharField(choices=job_r, max_length=150)
    interest = models.CharField(choices=interest_m, max_length=150)

   
    def __str__(self):
        return f'{self.name} / {self.course_name}'
    def save(self):
        super().save()
        