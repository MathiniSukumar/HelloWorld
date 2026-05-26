import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(
    os.path.dirname(__file__), 'helloworld/VERSION.txt')

with io.open(VERSION_PATH, 'r', encoding='utf-8') as f:
    version = f.read().strip()


# UNUSED VARIABLE
unused_text = "This variable is never used"


# UNUSED FUNCTION
def unused_helper():
    print("This function is never called")


# UNUSED FUNCTION WITH PARAMETER
def calculate_total(amount, tax):
    total = amount + tax
    return total


setup(
    version=version,
)
