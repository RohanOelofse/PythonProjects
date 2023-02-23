#!/usr/bin/env python3

"""
Contains functions for managing student information
"""

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023.02.20'
__status__ = 'Finished'

import data_validation as dv  # user input data validation


def list_students(students):
    """
    This function lists all the students that the user has added
    :param students: The dictionary of students
    :return: None
    """
    if len(students) == 0:
        print('There are no students to list...')
        print('')
        return

    print(f"{'ID':>{4}}  {'First Name':<{12}} {'Last Name':>{12}}")
    print("==== ================ ===================")

    for student_id, student_name in students.items():
        first_name, last_name = student_name.values()

        print(f"{student_id:>{4}} {first_name:<{16}} {last_name}")

    print('')


def add_student(students, next_student_id):
    """
    This function prompts the user to add the first name and last name of a student they want to add
    :param students: The dictionary of students
    :param next_student_id: Next id in list, can not be repeated
    :return: Adds a new student to dictionary
    """
    print("Add Student")
    print("-----------")
    first_name = dv.get_string("Pleas enter the Student\'s First Name").title()
    last_name = dv.get_string("Pleas enter the Student\'s Last Name").title()

    students[next_student_id] = {'first_name': first_name, 'last_name': last_name}

    print('')
    print('#' + str(next_student_id), first_name, last_name, 'was just added successfully!')
    print('')


def update_student(students):
    """
    This function prompts the user to select a student id of a student they want to change.
    :param students: The dictionary of students
    :return: None
    """
    if len(students) == 0:
        print("There are no students to update")
        print('')
        return

    try:
        student_id = dv.get_positive_num("Please enter student ID number")

        if student_id not in students:
            print('This student ID does not exist')
            return

        student = students[student_id]
        first_name, last_name = student.values()

        print('')

        if not dv.get_yes_no(f"Do you want to update Student ID #{student_id} {first_name} {last_name}"):
            print("Student update canceled...")
            return
        print('')

        new_first_name = input(f'Please enter the Student\'s First Name or press enter to keep {first_name}: ').title()
        new_last_name = input(f'Please enter the Student\'s Last Name or press enter to keep {last_name}: ').title()
        print('')

        # if no new names were entered the update would be canceled
        if new_first_name == '' and new_last_name == '':
            print("No data changed. update canceled")
            return

        if new_first_name > '':
            student['first_name'] = new_first_name
        else:
            new_first_name = first_name
            student['first_name'] = new_first_name

        if new_last_name > '':
            student['last_name'] = new_last_name
        else:
            new_last_name = last_name
            student['last_name'] = new_last_name

        print(f'Student ID #{student_id} {first_name} {last_name} was changed to {new_first_name} {new_last_name}')
        print('')
    except KeyError:
        print(f'Student ID #{student_id} was not found')
        print('')


def delete_student(students):
    """
    This function prompts the user to enter the id of a student they want to delete.
    :param students: The dictionary of students
    :return: None
    """
    if len(students) == 0:
        print("There are no students to delete...")
        print('')
        return

    try:

        student_id = dv.get_positive_num("Please enter the Student ID to be deleted: ")

        if student_id not in students:
            print('This student ID does not exist')
            return

        student = students[student_id]
        first_name, last_name = student.values()

        if not dv.get_yes_no(f"Please confirm deleting Student ID #{student_id} {first_name} {last_name}"):
            print("Student delete canceled...")
            print('')
            return
        else:
            del students[student_id]
            print(f"Student ID #{student_id} {first_name} {last_name} is deleted...")
            print('')

    except KeyError:
        print(f'Student ID #{student_id} could not be found.')
