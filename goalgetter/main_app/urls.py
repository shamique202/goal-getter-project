from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about, name='about'),
  path('courses/', views.courses_index, name='index'),
  path('courses/<int:course_id>/', views.courses_detail, name='detail'),
  path('courses/<int:course_id>/add_assignment/', views.add_assignment, name='add_assignment'),
  path('courses/create/', views.CourseCreate.as_view(), name='course_create'),
  path('courses/<int:course_id>/update_assignment/<int:assignment_id>/', views.update_assignment, name='update_assignment'),
  path('courses/<int:course_id>/delete_assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
  # path('assignment/<int:pk>/delete/', views.AssignmentDelete.as_view(), name='delete_assignment'),
  path('accounts/signup/', views.signup, name='signup'),
]
