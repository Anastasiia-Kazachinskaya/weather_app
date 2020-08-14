from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class People(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city

class Meta(ModelForm):
    class Meta:
        model = People
        fields = ['city']


