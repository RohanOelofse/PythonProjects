#!/usr/bin/env python3

"""

"""

import csv

# The following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023-04-06'
__status__ = 'Development'


class PasswordException(Exception):

    def __innit__(self, password, error_type, min_required, char_count):
        """

        :param password:
        :param error_type:
        :param min_required:
        :param char_count:
        :return:
        """

        self.log = {'password': password,
                    'error_type': error_type,
                    'min_required': min_required,
                    'char_count': char_count}
        with open('password_log.txt', 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([password, error_type, min_required, char_count])
