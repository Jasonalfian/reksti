from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    course_no = models.CharField(max_length=10, primary_key=True)
    course_name = models.TextField()

    def __str__(self):
        return f'{self.course_no} {self.course_name}'


class Student(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    name = models.TextField()

    def __str__(self):
        return f'{self.student_id} {self.name}'


class RoomConfiguration(models.Model):
    room_no = models.CharField(max_length=10, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    class_no = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course} in {self.room_no}'


class AttendanceRecord(models.Model):
    room_no = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    class_no = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    recorded_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
