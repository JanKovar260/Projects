def accum(s):
    result = ""
    for i, letter in enumerate(s):
        result += letter.upper() + i * letter.lower() + "-"
    return result[0:-1]
    
"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""
