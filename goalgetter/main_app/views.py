from django.shortcuts import render, redirect
from .models import Course, Assignment
from .forms import AssignmentForm

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def courses_index(request):
  courses = Course.objects.all()
  return render(request, 'courses/index.html', { 'courses': courses })

def courses_detail(request, course_id):
  course = Course.objects.get(id=course_id)
  return render(request, 'courses/detail.html', {'course': course})
