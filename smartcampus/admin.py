from django.contrib import admin
from .models import Student, RoomConfiguration, AttendanceRecord
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    fields = ['student_id', 'name']
    list_display = ('student_id', 'name')


class RoomConfigurationAdmin(admin.ModelAdmin):
    fields = ['room_no', 'password']
    list_display = ['room_no']


class AttendanceRecordAdmin(admin.ModelAdmin):
    fields = ['room_no', 'student', 'recorded_at']
    list_display = ('room_no', 'student', 'recorded_at')


admin.site.register(Student, StudentAdmin)
admin.site.register(RoomConfiguration, RoomConfigurationAdmin)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)