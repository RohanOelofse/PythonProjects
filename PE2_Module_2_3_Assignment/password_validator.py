#!/usr/bin/env python3

"""
My Python Password Validator
"""

import inspect

# The following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023-04-06'
__status__ = 'Development'


class PasswordValidator:
    __UPPERCASE_MIN = 2
    __LOWERCASE_MIN = 2
    __DIGIT_MIN = 2
    __SYMBOL_MIN = 2

    def __init__(self, password=None, debug_mode=False):
        self.__password = password
        self.debug_mode = debug_mode

    def __str__(self):
        if self.__password is None:
            return "None"
        else:
            return self.__password

    def is_uppercase_valid(self):
        count = sum(1 for char in self.__password if char.isupper())

        if self.debug_mode:
            print(f"{count:3d} = {inspect.currentframe().f_code.co_name}")
        if count >= 2:
            return True
        else:
            print("Password must have at least", PasswordValidator.__UPPERCASE_MIN, "uppercase letters")
            return False

    def is_valid(self, password=None):

        self.__password = password

        if self.debug_mode:
            print("===============DEBUG MODE===============")
            print(f"password = {self.__password}")

        if password is None:
            raise Exception("Password can not be empty")

        uppercase_valid = self.is_uppercase_valid()

        if uppercase_valid:
            return True
        else:
            return False


pv = PasswordValidator(debug_mode=True)

if pv.is_valid("ABC123abc!*"):
    print("Valid Password")
else:
    print("Password is invalid")

print()

if pv.is_valid("a"):
    print("Valid Password")
else:
    print("Password is invalid")

print()

if pv.is_valid("1234"):
    print("Valid Password")
else:
    print("Password is invalid")

