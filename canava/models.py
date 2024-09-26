from django.db import models

# Create your models here.
class alert_message_m(models.Model):
    
    age_old = {
        ('Under 19','Under 19'),
        ('19 or Older','19 or Older')
    }
    job_r = {
        ('Front-End Developer','Front-End Developer'),
        ('PHP Developer','PHP Developer'),
        ('Python Developer','Python Developer'),
        ('Django Developer','Django Developer'),
        ('Web Designer','Web Designer'),
        ('WordPress Developer','WordPress Developer'),
        ('Android Developer','Android Developer'),
        ('iOS Developer','iOS Developer'),
        ('Mobile Designer','Mobile Designer'),
        ('Business Owner','Business Owner'),
        ('Freelancer','Freelancer'),
    }
    interest_m = {
        ('Development','Development'),
        ('Design','Design'),
        ('Business','Business'),
    }
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=150)
    age = models.CharField(choices=age_old, max_length=150)
    biography = models.CharField(max_length=200)
    job_role = models.CharField(choices=job_r, max_length=150)
    interest = models.CharField(choices=interest_m, max_length=150)

    def __str__(self):
        return self.email
