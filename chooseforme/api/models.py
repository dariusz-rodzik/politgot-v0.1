from django.db import models

# Create your models here.
class Answers(models.Model):
    host = models.CharField(max_length=50, default="")
    mainGenre = models.CharField(max_length=20, default="")
    secGenre = models.CharField(max_length=20, default="")
    yearOfRelease = models.PositiveSmallIntegerField(null=False, default=2021)
    checkedAt = models.DateTimeField(auto_now_add=True)
    