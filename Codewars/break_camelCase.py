def solution(s):
    result = ""
    for x in s:
        if x.islower():
            result += x
        else:
            result += " " + x
    return result
