from django.shortcuts import render, redirect
from .models import Course, Assignment
from .forms import AssignmentForm
from django.views.generic.edit import CreateView

# from django.contrib.auth import login 

# Add the following import
from django.http import HttpResponse

class CourseCreate(CreateView):
  model = Course
  fields = '__all__'

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
  assignment_form = AssignmentForm()
  return render(request, 'courses/detail.html', {'course': course, 'assignment_form': assignment_form})

def add_assignment(request, course_id):
  form = AssignmentForm(request.POST)
  if form.is_valid():
    new_assignment = form.save(commit=False)
    new_assignment.course_id = course_id
    new_assignment.save()
  return redirect('detail', course_id=course_id)  
