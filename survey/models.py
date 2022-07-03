from django.db import models


# CharField 활용
class SurveySimple(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=32)
    address = models.CharField(max_length=256)
    suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# CharField(choices)
class SurveyChoices(models.Model):
    age = models.IntegerField()
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=256)
    suggestions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
