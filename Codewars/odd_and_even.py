"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. 
Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among 
the given numbers finds one that is different in evenness, and return a position of this number.
Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
"""

def iq_test(numbers, even=0, odd=0):
    x = numbers.split(" ")
    magic_index_even = 0
    magic_index_odd = 0
    for index, number in enumerate(x):
        if index + 1 <= len(numbers):
            if int(number) % 2 == 0:
                even += 1
                magic_index_even = index+1
            if int(number) % 2 == 1:
                odd += 1
                magic_index_odd = index+1
        index += 1
    if even == 1:
        return magic_index_even
    else:
        return magic_index_odd

"""
Examples:
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
"""
