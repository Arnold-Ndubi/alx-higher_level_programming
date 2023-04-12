#!/usr/bin/python3
"""Defines a class that checks function."""


def is_same_class(obj, a_class):
    """Checks if an object is the same as the instance of a given class.

    Args:
        obj (any): object that is being checked.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
