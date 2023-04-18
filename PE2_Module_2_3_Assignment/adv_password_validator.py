#!/usr/bin/env python3

import inspect
import password_validator as PV
import password_exception as PE

"""
Advanced Password Validator
"""

# The following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023-04-06'
__status__ = 'Development'


class AdvPasswordValidator(PV.PasswordValidator):
    """

    """
    MIN_LIMIT = 8
    MAX_LIMIT = 30
    VALID_SYMBOLS = ('@', '!', '*', '$')

    # min requirement
    # max limit
    # specific symbols
    def __init__(self, debug_mode=False):
        """

        :param debug_mode:
        """
        super().__init__(debug_mode)

    def __validate_min(self):
        """

        :return:
        """

        char_count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count < AdvPasswordValidator.MIN_LIMIT:
            raise PE.PasswordException(self.password, 'min limit', AdvPasswordValidator.MIN_LIMIT, char_count)

    def __validate_max(self):
        """

        :return:
        """

        char_count = len(self.password)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count > AdvPasswordValidator.MAX_LIMIT:
            raise PE.PasswordException(self.password, 'max limit', AdvPasswordValidator.MAX_LIMIT, char_count)

    def __validate_symbols(self):
        """

        :return:
        """
        char_count = sum(1 for char in self.password if char in AdvPasswordValidator.VALID_SYMBOLS)

        if self.debug_mode:
            print(inspect.currentframe().f_code.co_name, "=", char_count)

        if char_count > AdvPasswordValidator.MAX_LIMIT:
            raise PE.PasswordException(self.password, f'specific symbols {AdvPasswordValidator.VALID_SYMBOLS}',
                                       super().SYMBOL_MIN, char_count)

    def is_valid(self, password=None):
        """

        :param password:
        :return:
        """
        super().is_valid(password)

        try:
            self.__validate_symbols()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_min()
        except PE.PasswordException as e:
            self.errors.append(e)

        try:
            self.__validate_max()
        except PE.PasswordException as e:
            self.errors.append(e)

        if len(self.errors) == 0:
            return True
        else:
            return False
