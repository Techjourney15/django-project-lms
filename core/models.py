from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
SUBJECT=[('BCT001','Software Engineering'),
         ('BCT002','Database Management System'),
         ('BCT003','Computer Networks'),
         ('BCT004','Operating System'),
         ('BCT005','Data Structures and Algorithms'),
         ('BCT006','Object Oriented Programming'),
         ('BCT007','Web Technologies'),
         ('BCT008','Mobile Application Development')
         ]
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
    
class Assignment(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Assignment Title')
    start_date= models.DateField(default='N/A',null=False, blank=False, verbose_name='Start Date')
    due_date = models.DateField(default='N/A',null=False, blank=False, verbose_name='Due Date')
    question_file= models.FileField(upload_to='assignments/questions',null=True, blank=True, verbose_name='Select Assignment File')
    remark=models.CharField(max_length=100,null=False, blank=False, verbose_name='Assignment Remark')
    full_mark=models.FloatField(null=False, blank=False)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Uploaded By')
    SUBJECT= models.CharField(max_length=20, choices=SUBJECT,default='N/A', null=False, blank=False, verbose_name='Subject')

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'
        ordering = ['-title']

    def __str__(self):
        return self.title

class Material(models.Model):
    MATERIAL_CATEGORY = [
       ('SLIDE','Chapter Slide'),
       
       ('TEXT_BOOK','A Text Book'),
       ('REFERENCE_BOOK','A Reference Book'),
       ('AUDIO','Audio Material')
   ]
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Material Title')
    category = models.CharField(max_length=20, choices=MATERIAL_CATEGORY, null=False, blank=False, verbose_name='Material Category')
    description=models.CharField(max_length=500, null=False, blank=False, verbose_name='Material Description')
    SUBJECT= models.CharField(max_length=20, choices=SUBJECT, default='N/A',null=False, blank=False, verbose_name='Subject')
    file = models.FileField(upload_to='material/', null=False, blank=False, verbose_name='Material File Name')
    upload_date=models.DateTimeField(default=datetime.now(),verbose_name='Upload Date')
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE,default=0)
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ['-title']

    def __str__(self):
        return self.title