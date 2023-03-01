from django.db import models

# Create your models here.
class Login(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    classTeacher = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ID)



class Department(models.Model):
    deptId = models.CharField(max_length=10, primary_key=True)
    deptName = models.CharField(max_length=30)
    def __str__(self):
        return self.deptId

class ClassTeacher(models.Model):
    ID = models.ForeignKey(Login,on_delete=models.CASCADE)
    deptId = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField()
    academicYear = models.CharField(max_length=10)



class Subjects(models.Model):
    subjectId = models.CharField(max_length=20)
    semester = models.IntegerField()
    subjectName = models.CharField(max_length=50)
    deptId = models.ForeignKey(Department, on_delete=models.CASCADE)

# class SemSubjects(models.model):
# class Resultinput(models.model):
# class FinalResult(models.model):
# class Statistics(models.model):