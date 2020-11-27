def duplicate_encode(word):
    counts = []
    result = ""
    for i in word.lower():
        counts.append(i)
    
    for i in counts:
        if counts.count(i) > 1:
            result += ")"
        else:
            result += "("
    return result
    
    """The goal of this exercise is to convert a string to a new string 
    where each character in the new string is "(" if that character 
    appears only once in the original string, or ")" if that character 
    appears more than once in the original string. Ignore capitalization 
    when determining if a character is a duplicate."""
