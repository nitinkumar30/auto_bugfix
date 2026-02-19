# sample_code/buggy.py
def add_numbers(a, b):
    # bug: returns string instead of sum
    return str(a + b)

def multiply(a, b):
    return a * b
