"""Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. 
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead 
to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
"""

def delete_nth(order,max_e):
    new_list = []
    repeats = {}
    for i in order:
        if i not in repeats and max_e != 0:
            repeats[i] = 1
            new_list.append(i)
        elif repeats[i] < max_e:
            repeats[i] += 1
            new_list.append(i)
    return new_list
