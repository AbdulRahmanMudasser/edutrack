"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Function Based View's URLs
    # path('student/create/', views.create_student, name='create-student'),
    # path('students/', views.list_students, name='list-students'),
    # path('student/<int:pk>/', views.student_details, name='student-details'),
    # path('student/update/<int:pk>/', views.update_student, name='update-student'),
    # path('student/delete/<int:pk>/', views.delete_student, name='delete-student'),

    # Class Based View's URLs
    path('student/create/', views.CreateStudent.as_view(), name='create-student'),
    path('students/', views.ListStudents.as_view(), name='list-students'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path('student/update/<int:pk>/', views.UpdateStudent.as_view(), name='update-student'),
    path('student/delete/<int:pk>/', views.DeleteStudent.as_view(), name='delete-student'),
]
