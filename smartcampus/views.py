from rest_framework.response import Response
from rest_framework import generics
from .models import Student, RoomConfiguration, AttendanceRecord
from .serializers import StudentSerializer, RoomConfigurationSerializer, AttendanceRecordSerializer, PostAttendanceRecordSerializer, PostAttendanceNewSerializer
from datetime import datetime
from .service import AttendanceService
import pytz


class StudentView(generics.RetrieveAPIView):
    serializer_class = StudentSerializer
    lookup_field = 'student_id'
    queryset = Student.objects.all()


class RoomConfigurationView(generics.RetrieveAPIView):
    serializer_class = RoomConfigurationSerializer
    queryset = RoomConfiguration.objects.all()


class AttendanceRecordView(generics.ListAPIView):
    serializer_class = AttendanceRecordSerializer

    def get_queryset(self):
        tz = pytz.timezone("Asia/Jakarta")
        room_no = self.kwargs['room_no']
        from_timestamp = datetime.fromtimestamp(self.kwargs['from'], tz)
        to_timestamp = datetime.fromtimestamp(self.kwargs['to'], tz)
        return AttendanceRecord.objects.filter(room_no=room_no, recorded_at__range=(from_timestamp, to_timestamp))


class PostAttendanceRecordView(generics.CreateAPIView):
    serializer_class = PostAttendanceRecordSerializer

    def post(self, request, format=None, *args, **kwargs):
        request_serializer = PostAttendanceRecordSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        room_no = self.kwargs['room_no']
        password = self.kwargs['password']
        student_id = request.data['student_id']

        tz = pytz.timezone("Asia/Jakarta")
        recorded_time = datetime.fromtimestamp(request.data['recorded_at'], tz)

        attendance = AttendanceService().record_attendee(room_no, password, student_id, recorded_time)
        response_serializer = AttendanceRecordSerializer(attendance)
        return Response(data=response_serializer.data)

# new & updated untuk bulk
class PostAttendanceNewView(generics.CreateAPIView):
    serializer_class = PostAttendanceNewSerializer

    def post(self, request, format=None, *args, **kwargs):
        request_serializer = PostAttendanceNewSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        room_no = self.kwargs['room_no']
        password = request.data['password']
        tz = pytz.timezone("Asia/Jakarta")

        attendancelist = []
        for n in request.data['records']:
            student_id = n['student_id']
            recorded_time = datetime.fromtimestamp(n['recorded_at'], tz)
            results = AttendanceService().record_attendee(room_no, password, student_id, recorded_time)
            attendancelist.append(results)
        
        response_serializer = AttendanceRecordSerializer(attendancelist, many=True)
        return Response(data=response_serializer.data)