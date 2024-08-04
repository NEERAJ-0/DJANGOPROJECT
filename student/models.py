from django.db import models

# Create your models here.
class BatchMasterModel(models.Model):
    batchid = models.IntegerField(unique=True)
    batchno = models.CharField(max_length =9, unique=True)
    def __str__(self):
        return self.batchno

class CourseMasterModel(models.Model):
    courseid = models.IntegerField(unique=True)
    course   = models.CharField(max_length =4, unique=True)
    def __str__(self):
        return self.course

class SemMasterModel(models.Model):
    semid = models.IntegerField(unique=True)
    sem   = models.CharField(max_length =3,unique=True)
    def __str__(self):
        return self.sem

class ExamMasterModel(models.Model):
    examid   = models.IntegerField(unique=True)
    examtype = models.CharField(max_length =13, unique=True)
    def __str__(self):
        return self.examtype

class PaperMasterModel(models.Model):
    papercode    = models.CharField(max_length =8, unique=True)
    papertype    = models.CharField(max_length =18)
    papershtname = models.CharField(max_length=10, unique=True)
    papername    = models.CharField(max_length =50,unique=True)
    def __str__(self):
        return self.papername
    
class StudentMasterModel(models.Model):
    batchno   = models.ForeignKey(BatchMasterModel,on_delete =models.CASCADE)
    sem       = models.ForeignKey(SemMasterModel,on_delete =models.CASCADE)
    course    = models.ForeignKey(CourseMasterModel,on_delete =models.CASCADE)
    studregno = models.IntegerField(unique=True)
    studname  = models.CharField(max_length =30)
    def __str__(self):
        return self.studname

class StudentInternalTransModel(models.Model):
    course    = models.ForeignKey(CourseMasterModel,on_delete =models.CASCADE)
    batchno   = models.ForeignKey(BatchMasterModel,on_delete =models.CASCADE)
    sem       = models.ForeignKey(SemMasterModel,on_delete =models.CASCADE)
    examtype  = models.ForeignKey(ExamMasterModel,on_delete =models.CASCADE)
    studname  = models.ForeignKey(StudentMasterModel, on_delete =models.CASCADE)
    #studregno  = models.ForeignKey(StudentMasterModel, on_delete =models.CASCADE)
    papername = models.ForeignKey(PaperMasterModel, on_delete =models.CASCADE)
    #papercode = models.ForeignKey(PaperMasterModel, on_delete =models.CASCADE)
    marks     = models.IntegerField()
    
    def __str__(self):
        return str(self.studname.studregno)
    