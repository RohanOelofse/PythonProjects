#!/usr/bin/env python3

import csv
import re
from datetime import datetime

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023.05.01'
__status__ = 'Development'
"""
This program validates data from a csv file and rewrites it into 2 separate csv file for 
valid data and invalid data. Valid data also changes format

GitHub = https://github.com/RohanOelofse/PythonProjects/tree/main/PE2Module4_DataValidation
"""


def validate_id(id):
    """
    This function validates that the id is a valid number
    :param id:  The id from the input file, index 0
    :return:    The error string if it was invalid
    """
    regex = "^[0-9]+$"
    if re.fullmatch(regex, id):
        return ""
    else:
        return "I"


def validate_name(name):
    """
    This function validates the name to make sure it contains a first name and last name
    :param name:    The name from the input file, index 1
    :return:        The error string if it was invalid
    """
    name = name.split(",")

    if len(name) == 2:
        return ""
    else:
        return "N"


def validate_email(email):
    """
    This function validates the email by making sure it has a '@' and a '.'
    :param email:   The email from input file, index 2
    :return:        The error string if it was invalid
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(email_regex, email):
        return ""
    else:
        return "E"


def validate_phone(phone):
    """
    This function validates the phone number by making sure it is in format of '3numbers-3numbers-4numbers'
    :param phone:   The phone number from input file, index 3
    :return:        The error string if it was invalid
    """
    phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

    if re.fullmatch(phone_regex, phone):
        return ""
    else:
        return "P"


def validate_date(date):
    """
    This function validates the date by making sure it is in the correct format
    :param date:    The date form the input files, index 4
    :return:        The error string if it was invalid
    """
    date_format = "%m/%d/%Y"
    try:
        res = bool(datetime.strptime(date, date_format))
    except ValueError:
        res = False
    if res:
        return ""
    else:
        return "D"


def validate_time(time):
    """
    This function validates the time by making sure it is in the correct format
    :param time:    The time from the input file, index 5
    :return:        The error string if it was invalid
    """
    time_format = "%H:%M"
    try:
        valid_time = datetime.strptime(time, time_format)
    except ValueError:
        valid_time = False
    if valid_time:
        return ""
    else:
        return "T"


def process_name(name):
    """
    This function splits the first name and last name into two different indexes
    :param name:    The name from the input file
    :return:         first name and last name
    """
    name = name.split(",")
    return name[0], name[1]


def process_phone(phone):
    """
    This function replaces all instances of '-' with '.'
    :param phone:   phone number from input file
    :return:        phone number in new format
    """
    phone = phone.replace("-", ".")
    return phone


def process_date(date):
    """
    This function changes the format of date
    :param date:    the date from input file
    :return:        Date in new format
    """
    date = datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
    return date


def process_file():
    """
    This function calls all the functions if the length of the row is 6. After that it writes the valid data to the
    valid file and invalid data to the invalid file
    :return:    N/a
    """

    process_file.valid_count = 0
    process_file.invalid_count = 0

    with open('input.csv', mode='r') as input_file, open('valid.csv', 'w', newline='') as valid_file, \
            open('invalid.csv', mode='w') as invalid_file:
        input_reader = csv.reader(input_file, delimiter='|')
        for line in input_reader:
            error_string = ""
            data_count = len(line)
            if data_count == 6:
                error_string += validate_id(line[0])
                error_string += validate_name(line[1])
                error_string += validate_email(line[2])
                error_string += validate_phone(line[3])
                error_string += validate_date(line[4])
                error_string += validate_time(line[5])
            else:
                error_string = "C"
            if error_string == "":
                process_file.valid_count += 1
                first_name, last_name = process_name(line[1])
                new_date = process_date(line[4])
                phone_number = process_phone(line[3])

                data = [line[0], first_name, last_name, line[2], phone_number, new_date, line[5]]

                writer = csv.writer(valid_file, delimiter=',')
                writer.writerow(data)
            else:
                process_file.invalid_count += 1
                line.insert(0, error_string)
                writer = csv.writer(invalid_file, delimiter='|')
                writer.writerow(line)


def validation_report():
    print("Validation Report")
    print("---------------------------------------")
    print("Records successfully validated = ", process_file.valid_count)
    print("Records unsuccessfully validated = ", process_file.invalid_count)


if __name__ == '__main__':
    process_file()
    validation_report()
