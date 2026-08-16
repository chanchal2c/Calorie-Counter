from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUser(AbstractUser):

    pass

    def __str__(self):
        return f'{self.username}'


class profileModel(models.Model):

    GENDER_OPTIONS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(customUser, on_delete=models.CASCADE, related_name='user_profile', null=True)
    name = models.CharField(max_length=100, null=True)
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=50, null=True)
    age = models.PositiveIntegerField(null=True, help_text='Age in years')
    height = models.FloatField(null=True, help_text='Height in centimeters')
    weight = models.FloatField(null=True, help_text='Weight in kilograms')
    bmr = models.FloatField(null=True)

    def __str__(self):
        return f'{self.name}'


class consumedColorieModel(models.Model):

    user = models.ForeignKey(customUser, on_delete=models.CASCADE, null=True, related_name='user_calorie')
    item_name = models.CharField(max_length=200, null=True)
    calorie = models.FloatField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.item_name}'