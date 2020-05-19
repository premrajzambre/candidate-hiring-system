from django.db import models
from phone_field import PhoneField
from postgres_copy import CopyManager

# Create your models here.
class applicant(models.Model):
    DEGREE_CHOICES = (
        ('BE/B.Tech','BE/B.Tech'),
        ('ME/M.Tech','ME/M.Tech'),
        ('B.Sc','B.Sc'),
        ('M.Sc','M.Sc')
    )
    DEGREE_SCORE_CHOICES = (
        (60,60),(61,61),(62,62),(63,63),(64,64),(65,65),(66,66),(67,67),(68,68),(69,69),
        (70,70),(71,71),(72,72),(73,73),(74,74),(75,75),(76,76),(77,77),(78,78),(79,79),
        (80,80),(81,81),(82,82),(83,83),(84,84),(85,85),(86,86),(87,87),(88,88),(89,89),
        (90,90),(91,91),(92,92),(93,93),(94,94),(95,95),(96,96),(97,97),(98,98),(99,99)
    )
    TYPE_CHOICS = (
        ('Fresher','Fresher'),
        ('Experienced','Experienced')
    )
    CATEGORY_CHOICES = (
        ('1','Selected'),
        ('0','Rejected')
    )
    email=models.EmailField(primary_key=True)
    full_name=models.CharField(max_length=100)
    contact=PhoneField(blank=True,help_text='Start with country code')
    degree=models.CharField(max_length=10,choices=DEGREE_CHOICES)
    degree_score=models.IntegerField(choices=DEGREE_SCORE_CHOICES)
    type=models.CharField(max_length=15,choices=TYPE_CHOICS)
    aptitude_score=models.IntegerField(default=0)
    technical_score=models.IntegerField(default=0)
    personality_score=models.IntegerField(default=0)
    average_score=models.IntegerField(default=0)
    category=models.CharField(max_length=10,choices=CATEGORY_CHOICES,null=True,blank=True)
    hr_id=models.CharField(max_length=10,blank=True,null=True)
    date_of_interview=models.DateField(blank=True,null=True)
    objects = CopyManager()

    def __str__(self):
        return self.email
