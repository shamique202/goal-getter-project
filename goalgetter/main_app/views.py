from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')
def about(request):
  return render(request, 'about.html')
def courses_index(request):
  return render(request, 'courses/index.html', { 'courses': courses })

