from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=8, primary_key=True)
    name = models.TextField()

    def __str__(self):
        return f'{self.student_id} {self.name}'


class RoomConfiguration(models.Model):
    room_no = models.CharField(max_length=10, primary_key=True)
    password = models.TextField(default='')

    def __str__(self):
        return f'Ruang {self.room_no}'


class AttendanceRecord(models.Model):
    room_no = models.CharField(max_length=10)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    recorded_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
