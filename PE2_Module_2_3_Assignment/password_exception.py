#!/usr/bin/env python3

"""
Password Exception handling
GitHub: https://github.com/RohanOelofse/PythonProjects/tree/main/PE2_Module_2_3_Assignment
"""

import csv

# The following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023-04-06'
__status__ = 'Development'


class PasswordException(Exception):
    """
    This class handles the exceptions picked up
    """

    def __init__(self, password, error_type, min_required, char_count):
        """
        This function writes the errors it picks up to a text file.
        :param password: The password
        :param error_type: Type of error
        :param min_required: min required amount
        :param char_count: The char count
        :return: None
        """

        self.log = {'password': password,
                    'error_type': error_type,
                    'min_required': min_required,
                    'char_count': char_count}
        with open('password_log.txt', 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([password, error_type, min_required, char_count])
