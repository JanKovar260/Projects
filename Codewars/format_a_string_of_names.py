"""Given: an array containing hashes of names; Return: a string formatted as a list of names 
separated by commas except for the last two names, which should be separated by an ampersand."""

def namelist(names):
    just_names = []
    for d in names:
        for i in d.values():
            just_names.append(i)
    result = ""
    if len(just_names) == 2:
        result = " & ".join(just_names)
    elif len(just_names) > 2:
        result = ", ".join(just_names[:-1])
        result = result + " & " + str(*just_names[-1:])
    elif len(just_names) == 1:
        result = just_names[0]
    else:
        result = result
    return result
