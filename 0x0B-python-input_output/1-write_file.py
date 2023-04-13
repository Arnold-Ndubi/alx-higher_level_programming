#!/usr/bin/python3
"""Defines a function that writes a file."""


def write_file(filename="", text=""):
    """write a string to a .txt file  UTF8.

    Args:
        filename (str): the name of the file to be writen into.
        text (str): The text to write to the file.
    Returns:
         number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
