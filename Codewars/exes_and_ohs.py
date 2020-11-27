# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

from collections import Counter

def xo(s):
    amounts = Counter(s.lower())
    x = amounts.get("x")
    y = amounts.get("o")
    if x == y:
        return True
    else:
        return False

"""
Examples:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
