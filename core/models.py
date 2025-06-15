from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    SEMESTER=[
        ('SEM_ONE','Semester One'),
        ('SEM_TWO','Semester Two'),
        ('SEM_THREE','Semester Three'),
        ('SEM_FOUR','Semester Four'),
        ('SEM_FIVE','Semester Five'),
        ('SEM_SIX','Semester Six'),
        ('SEM_SEVEN','Semester Seven'),
        ('SEM_EIGHT','Semester Eight'),
    ]
    full_name=models.CharField(max_length=200,null=False,blank=False,verbose_name='Student Full Name')
    email=models.CharField(max_length=100,unique=True,null=False,blank=False,verbose_name='Student Email')
    semester=models.CharField(max_length=20,null=True,blank=True,choices=SEMESTER,default='N/A')
    phone_number=models.IntegerField(null=False,blank=False)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['full_name'] #highest ordering priority

    def __str__(self):
        return self.full_name
    
class Teacher(models.Model):
    DEPARTMENT=[
        ('CSE','Computer Science and Engineering'),
        ('ECE','Electronics and Communication Engineering'),
        ('ME','Mechanical Engineering'),
        ('CE','Civil Engineering'),
        ('EE','Electrical Engineering'),
        ('IT','Information Technology'),
    ]
    full_name=models.CharField(max_length=200,null=False,blank=False,verbose_name='Teacher Full Name')
    email=models.CharField(max_length=100,unique=True,null=False,blank=False,verbose_name='Teacher Email')
    department=models.CharField(max_length=5,null=True,blank=True,choices=DEPARTMENT,default='N/A')
    phone_number=models.IntegerField(null=False,blank=False)
    join_date=models.DateField(default='JOIN_DATE')
    user=models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name