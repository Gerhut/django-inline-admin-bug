from django.contrib import admin

from .models import Room, Teacher, Student


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    class StudentInline(admin.TabularInline):
        model = Student

    inlines = [StudentInline]
