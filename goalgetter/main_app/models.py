from django.db import models

# Create your models here.

class Course(models.Model):
  name = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.name} has id of {self.id}'


TASK=(
  ('E', 'Essay'),
  ('P', 'Project'),
  ('H', 'Homework'),
  ('T', 'Test'),
  ('O', 'Other'),
)

class Assignment(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField('Due Date')
  category = models.CharField(
    max_length=1, 
    choices=TASK,
    default=TASK[2][0]
  )
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} {self.get_category_display()} on {self.date}'
