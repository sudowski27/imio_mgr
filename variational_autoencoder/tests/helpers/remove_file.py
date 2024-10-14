"""version 0.1.0"""
import os


def remove_file(filename: str) -> None:
    """
    Remove file from disc

    Paremters
    ---------
    filename: str
    """
    os.remove(filename)
