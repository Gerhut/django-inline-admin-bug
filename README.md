# Reproduce Steps:

1. `$ ./manage.py migrate`
2. `$ ./manage.py createsuperuser`
3. `$ ./manage.py runserver`
4. <http://127.0.0.1:8080/admin>
5. Create a new room
6. Create a new teacher with the room, with a new student.
   "Save and continue editing"
7. Create another student with the teacher.
   "Save"
8. Reproduced: "Please correct the error below." without any errors.
