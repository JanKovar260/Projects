# You are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    n = [int(i) for i in numbers.split()]
    n.sort()
    result = str(n[-1]) + " " + str(n[0])
    return result

"""
Notes:
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""
