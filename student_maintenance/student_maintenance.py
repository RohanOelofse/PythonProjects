#!/usr/bin/env python3

"""

"""

import data_validation as dv  # user input data validation


def list_students(students):
    if len(students) == 0:
        print('There are no students to update. ')
        return
    else:
        print('')


def add_student(students, next_student_id):
    print("Add Student")
    print("-----------")
    first_name = dv.get_string("Pleas enter the Student\'s First Name: ")
    last_name = dv.get_string("Pleas enter the Student\'s Last Name: ")

    students[next_student_id] = {'first_name': first_name, 'last_name': last_name}

    print('#' + next_student_id, first_name, last_name, 'was just added successfully')


def update_student(students):
    print('')


def delete_student(students):
    print('')