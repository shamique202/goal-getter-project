from django.forms import ModelForm 
from django import forms
from .models import Assignment

class AssignmentForm(ModelForm):
  class Meta:
    model = Assignment 
    fields = ['name', 'date', 'category', 'todo']