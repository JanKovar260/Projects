def longest(s1, s2):
    s = s1+s2
    result = ""
    for i in s:
        if i not in result:
            result += i
    return "".join(sorted(result))

"""
Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters, each taken only once - coming from s1 or s2.

a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'
longest(a, b) -> 'abcdefklmopqwxy'

a = 'abcdefghijklmnopqrstuvwxyz'
longest(a, a) -> 'abcdefghijklmnopqrstuvwxyz'
"""
