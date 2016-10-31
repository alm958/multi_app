from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z-]*[a-zA-Z]+$')

class CourseManager(models.Manager):
    def add_course(self, **kwargs):
        message_list = []
        min_age = 13
        state = False
        if Course.objects.filter(name=kwargs['name']).exists():
            message_list.append('A Course with the same name already exists. Confirm this is a new course and change the name.  If this is replacing the old course of the same name consider updating or deleteing that course.')
        if (len(kwargs['name']) < 5 or len(kwargs['description']) < 10):
            message_list.append('The course name and descriptions are required.  Course name must be no less than 5 characters in length. Description must be no less than 10 characters in length.')
        if len(message_list) is 0 :
            Course.objects.create(name=kwargs['name'], description=kwargs['description'])
            message_list.append('Course {} successfully added'.format(kwargs['name']))
            state = True
        else :
            state = False
        return (state, message_list)

    def all_courses(self):
        all_courses = list(Course.objects.all())
        all_courses = [(course, len(course.users.all())) for course in all_courses]
        return all_courses
    # def login(self, **kwargs):



# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
