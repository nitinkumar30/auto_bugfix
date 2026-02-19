# sample_code/test_buggy.py
from buggy import add_numbers, multiply

def test_add():
    assert add_numbers(2, 3) == 5

def test_multiply():
    assert multiply(3, 4) == 12
