"""version 0.1.1"""
import os
import time


def remove_file(filename: str) -> None:
    """
    Remove file from disc

    Paremters
    ---------
    filename: str
    """
    os.remove(filename)
    while os.path.exists(filename):
        time.sleep(0.001)
