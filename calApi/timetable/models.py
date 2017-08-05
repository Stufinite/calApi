from django.db import models


class Department(models.Model):
    school = models.CharField(max_length=100, default='')
    degree = models.CharField(max_length=100, default='')
    code = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{} {}'.format(self.code, self.title)


class Course(models.Model):
    school = models.CharField(max_length=20, default='')
    semester = models.CharField(max_length=4, default='')
    code = models.CharField(max_length=20, default='', unique=True)
    credits = models.FloatField(default=0)
    title = models.CharField(max_length=40, default='')
    professor = models.CharField(max_length=20, default='')
    time = models.CharField(max_length=20, default='')
    location = models.CharField(max_length=20, default='')
    department = models.CharField(max_length=20, default='')
    obligatory = models.BooleanField(default=True)
    note = models.CharField(max_length=50, default='')
    discipline = models.CharField(max_length=20, default='')

    def __str__(self):
        return '{}: {} / {}'.format(self.semester, self.title, self.professor)


class SelectedCourse(models.Model):
    user_id = models.CharField(max_length=128, default='')
    code = models.CharField(max_length=64, default='')
    semester = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{}: {} ({})'.format(self.user_id, self.code, self.semester)
