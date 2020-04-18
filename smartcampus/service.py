from django.db import transaction
from rest_framework import exceptions
from .models import Student, AttendanceRecord, RoomConfiguration


class AttendanceService:
    @transaction.atomic
    def record_attendee(self, room_no, password, student_id, recorded_time):
        room = RoomConfiguration.objects.get(room_no__exact = room_no)

        if room.password != password:
            raise exceptions.APIException(detail='Invalid password')

        try:
            student = Student.objects.get(student_id__exact = student_id)
        except Student.DoesNotExist:
            raise exceptions.APIException(detail='Invalid student ID')

        attendance = AttendanceRecord.objects.create(
            student=student,
            room_no=room_no,
            recorded_at=recorded_time
        )

        return attendance
