#!/usr/bin/env python3

"""

"""
import password_validator as PV
import adv_password_validator as APV

# The following are module level dunders (metadata) for the authorship information
__author__ = 'Rohan Oelofse'
__version__ = '1.0'
__date__ = '2023-04-06'
__status__ = 'Development'


def display_errors(pw):
    """

    :param pw:
    :return:
    """
    print("Invalid password")
    for e in pw.errors:
        print(f"{e.log['password']} Password must contain {e.log['min_required']} {e.log['error_type']} "
              f"but yours only contained {e.log['char_count']}")


def default_validator():
    """

    :return:
    """

    pw = PV.PasswordValidator(debug_mode=False)

    if pw.is_valid("Ab11!@"):
        print("Valid Password")
    else:
        display_errors(pw)

    print()

    if pw.is_valid("AAbb11!@"):
        print("Valid Password")
    else:
        display_errors(pw)


def advanced_validator():
    """

    :return:
    """

    apw = APV.AdvPasswordValidator(debug_mode=False)

    if apw.is_valid("Ab11!@"):
        print("Valid Password")
    else:
        display_errors(apw)
    print()

    if apw.is_valid("AAbb11!@"):
        print("Valid Password")
    else:
        display_errors(apw)


if __name__ == '__main__':
    default_validator()

    advanced_validator()
