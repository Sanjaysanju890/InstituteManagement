from django.db import models

class Student(models.Model):
    student_id=models.IntegerField()
    student_class=models.IntegerField()
    student_name=models.CharField(max_length=20)
    student_fathername=models.CharField(max_length=20)
    student_addr=models.CharField(max_length=15)
    student_tuitionfee=models.IntegerField()
    student_busfee=models.IntegerField()

    def __str__(self):
        return str(self.student_id)+self.student_name+str(self.student_fathername)+self.student_addr+str(self.student_tuitionfee)+str(self.student_busfee)
