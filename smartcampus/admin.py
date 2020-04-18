from django.contrib import admin
from .models import Course, Student, RoomConfiguration, AttendanceRecord
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    fields = ['course_no', 'course_name']
    list_display = ('course_no', 'course_name')


class StudentAdmin(admin.ModelAdmin):
    fields = ['student_id', 'name']
    list_display = ('student_id', 'name')


class RoomConfigurationAdmin(admin.ModelAdmin):
    fields = ['room_no', 'course', 'class_no']
    list_display = ('room_no', 'course', 'class_no', 'updated_at')


class AttendanceRecordAdmin(admin.ModelAdmin):
    fields = ['room_no', 'course', 'class_no', 'student', 'recorded_at']
    list_display = ('room_no', 'course', 'class_no', 'student', 'recorded_at')


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(RoomConfiguration, RoomConfigurationAdmin)
admin.site.register(AttendanceRecord, AttendanceRecordAdmin)