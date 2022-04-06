from django.db import models
import datetime
class timeTracking(models.Model):
    empname = models.CharField(max_length = 100)
    department = models.CharField(max_length= 100)
    currentweek = models.IntegerField()
    day1 = models.DateField(blank=True, null=True)
    time_worked1 = models.IntegerField()
    systemcode1 = models.CharField(max_length = 100, default = None)
    development_phase1 = models.CharField(max_length = 100)
    project1 = models.CharField(max_length = 100)
    day2 = models.DateField(blank=True, null=True)
    time_worked2 = models.IntegerField()
    systemcode2 = models.CharField(max_length = 100, default = None)
    development_phase2 = models.CharField(max_length = 100)
    project2 = models.CharField(max_length = 100)
    day3 = models.DateField(blank=True, null=True)
    time_worked3 = models.IntegerField()
    systemcode3 = models.CharField(max_length = 100, default = None)
    development_phase3 = models.CharField(max_length = 100)
    project3 = models.CharField(max_length = 100)
    day4 = models.DateField(blank=True, null=True)
    time_worked4 = models.IntegerField()
    systemcode4 = models.CharField(max_length = 100, default = None)
    development_phase4 = models.CharField(max_length = 100)
    project4 = models.CharField(max_length = 100)
    day5 = models.DateField(blank=True, null=True)
    time_worked5 = models.IntegerField()
    systemcode5 = models.CharField(max_length = 100, default = None)
    development_phase5 = models.CharField(max_length = 100)
    project5 = models.CharField(max_length = 100)
    day6 = models.DateField(blank=True, null=True)
    time_worked6 = models.IntegerField()
    systemcode6 = models.CharField(max_length = 100, default = None)
    development_phase6 = models.CharField(max_length = 100)
    project6 = models.CharField(max_length = 100)
    
    class Meta:
        db_table = "time_history"
      
    
