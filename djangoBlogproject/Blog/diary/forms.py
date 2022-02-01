from cProfile import label
from dataclasses import field
from unicodedata import name
from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title', 'content', 'feeling', 'score']
    # title = forms.CharField(max_length=50, label='제목')
    # content = forms.CharField(widget=forms.Textarea, label='내용')
    # feeling = forms.CharField(max_length=80, label='감정상태')
    # score = forms.IntegerField(label='감정점수')
    # dt_created = forms.DateTimeField(label='날짜')
    