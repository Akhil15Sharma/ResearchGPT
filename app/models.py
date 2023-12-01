from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userdetail(User):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,parent_link=True)    


class Question(models.Model):
    user=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
    ques=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.ques

class Docfile(models.Model):
    user=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
    doc=models.FileField(upload_to="files")
class Pdffile(models.Model):
    user=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
    pdf=models.FileField(upload_to="files")

class Excelfile(models.Model):
    user=models.ForeignKey(Userdetail,on_delete=models.CASCADE)
    excel=models.FileField(upload_to="files")