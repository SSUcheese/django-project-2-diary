from pyexpat import model
from tkinter.tix import Tree
from django.db import models
from .validators import validate_score, validate_title_content, validate_feeling


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length= 50, validators=[validate_title_content], unique=True, error_messages={'unique':'이미 있는 제목'})
    content = models.TextField(validators=[validate_title_content])
    feeling = models.CharField(max_length= 80, validators=[validate_feeling])
    score = models.IntegerField(validators=[validate_score])
    dt_created = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title