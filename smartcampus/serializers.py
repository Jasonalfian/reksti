from rest_framework import serializers
from .models import Student, RoomConfiguration, AttendanceRecord


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name']


class RoomConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomConfiguration
        fields = ['room_no']


class AttendanceRecordSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False, read_only=True)
    class Meta:
        model = AttendanceRecord
        fields = ['student', 'room_no', 'recorded_at']


class PostAttendanceRecordSerializer(serializers.Serializer):
    student_id = serializers.CharField(max_length=8)
    timestamp = serializers.IntegerField()
