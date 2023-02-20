#!/usr/bin/env python3

"""

"""

import data_validation as dv  # user input data validation


def list_students(students):
    if len(students) == 0:
        print('There are no students to list. ')
        return
    else:
        print(f"{'ID':>{4}}  {'First Name':<{12}} {'Last Name':>{12}}")
        print("==== ================ ===================")
        for student_id, student_name in students.items():
            first_name, last_name = student_name.values()
            print(f"{student_id:>{4}} {first_name:<{12}} {last_name:>{12}}")


def add_student(students, next_student_id):
    print("Add Student")
    print("-----------")
    first_name = dv.get_string("Pleas enter the Student\'s First Name: ")
    last_name = dv.get_string("Pleas enter the Student\'s Last Name: ")

    students[next_student_id] = {'first_name': first_name, 'last_name': last_name}

    print('#' + str(next_student_id), first_name, last_name, 'was just added successfully')


def update_student(students):
    if len(students) == 0:
        print("There are no students to update")
        return
    else:
        student_id = int(input("Please enter student id number: "))
        student = students[student_id]
        first_name, last_name = student.values()

        confirm = str(input(f"Do you want to update Student ID #{student_id} {first_name} {last_name} (y=Yes, n=No): "))
        if confirm == 'n':
            return

        new_first_name = input(f'Please enter the Student\'s First Name or press enter to keep {first_name}: ').title()
        new_last_name = input(f'Please enter the Student\'s Last Name or press enter to keep {last_name}: ').title()

        if new_first_name == '' and new_last_name == '':
            print("No data changed. update canceled")
            return

        if first_name > '':
            student['first_name'] = new_first_name

        if last_name > '':
            student[last_name] = new_last_name


def delete_student(students):
    if len(students) == 0:
        print("There are no students to delete")
        return