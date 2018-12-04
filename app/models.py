from django.db import models

from uuid import uuid4


class Room(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE,
                                primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name
