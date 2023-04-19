#!/usr/bin/env python3

"""
My Python Password Validator
GitHub: https://github.com/RohanOelofse/PythonProjects/tree/main/PE2_Module_2_3_Assignment
"""
import inspect
import password_exception as PE

# The following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023-04-06'
__status__ = 'Development'


class PasswordValidator:
    """
    This class tests the password for minimum uppercase letter, minimum lowercase letters, minimum digits,
    and valid symbols
    """
    UPPERCASE_MIN = 2
    LOWERCASE_MIN = 2
    DIGIT_MIN = 2
    SYMBOL_MIN = 2
    VALID_SYMBOLS = ('@', '!', '*', '$')

    def __init__(self, password=None, debug_mode=False):
        """

        :param password: The password
        :param debug_mode: Debug mode set to True or false
        """
        self.password = password
        self.debug_mode = debug_mode
        self.errors = []

    def __str__(self):
        """
        This function tests if the password is empty
        :return: None if password is empty, else returns the password
        """
        if self.password is None:
            return "None"
        else:
            return self.password

    def __validate_uppercase(self):
        """
        This function tests the number of uppercase letters in the password
        :return: None
        """
        char_count = sum(1 for char in self.password if char.isupper())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.UPPERCASE_MIN:
            raise PE.PasswordException(self.password, 'uppercase', PasswordValidator.UPPERCASE_MIN, char_count)

    def __validate_lowercase(self):
        """
        This function tests the number of lowercase letters in  the password
        :return: None
        """
        char_count = sum(1 for char in self.password if char.islower())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.LOWERCASE_MIN:
            raise PE.PasswordException(self.password, 'lowercase', PasswordValidator.LOWERCASE_MIN, char_count)

    def __validate_digit(self):
        """
        This function tests the number of digits in the password
        :return: None
        """
        char_count = sum(1 for char in self.password if char.isdigit())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.DIGIT_MIN:
            raise PE.PasswordException(self.password, 'digit', PasswordValidator.DIGIT_MIN, char_count)

    def __validate_symbol(self):
        """
        This function tests the number of symbols in the password
        :return: None
        """
        char_count = sum(1 for char in self.password if not char.isdigit() and not char.isalpha())

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < PasswordValidator.LOWERCASE_MIN:
            raise PE.PasswordException(self.password, 'lowercase', PasswordValidator.LOWERCASE_MIN, char_count)

    def is_valid(self, password=None):
        """
        This function tests the validation and appends eny errors it picks up
        :param password: The password provided
        :return: True or False
        """

        self.password = password

        self.errors.clear()

        if self.debug_mode:
            print("===============DEBUG MODE===============")
            print("password = ", self)

        try:
            self.__validate_uppercase()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_lowercase()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_digit()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_symbol()
        except PE.PasswordException as e:
            self.errors.append(e)

        if len(self.errors) == 0:
            return True
        else:
            return False
