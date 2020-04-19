from django.urls import path
from django.conf.urls import url
from .views import StudentView, AttendanceRecordView, PostAttendanceRecordView, PostAttendanceNewView
from rest_framework.schemas import get_schema_view
from rest_framework import permissions


urlpatterns = [

    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi'),
    path('students/<student_id>/', StudentView.as_view(), name='student-details'),
    path('attendance/<room_no>/<int:from>/<int:to>', AttendanceRecordView.as_view(), name='attendance-record'),
    path('attendance/<room_no>/<password>/', PostAttendanceRecordView.as_view(), name='attendance-create'),
    path('attendance/<room_no>/', PostAttendanceNewView.as_view(), name='attendance-create-bulk')
]