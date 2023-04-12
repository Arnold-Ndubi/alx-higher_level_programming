#!/usr/bin/python3
"""Defines a method that adds an attribute to an object."""


def add_attribute(obj, att, value):
    """Append a new attribute to an object where it is possible.

    Args:
        obj (any): this the object to be appended to an attribute.
        att (str): this is the name of the attribute to be added to obj.
        value (any): this the value of att.
    Raises:
        TypeError: if it is impposible to add.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
