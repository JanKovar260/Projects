"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items
without any elements with the same value next to each other and preserving the original order of elements."""

def unique_in_order(iterable):
    into_list = list(iterable)
    new_list = []
    for i, value in enumerate(into_list):
        current_value = value
        next_value = into_list[i + 1] if i < len(into_list) - 1 else None
        if current_value != next_value:
            new_list.append(into_list[i])
    return new_list

"""
Examples:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
