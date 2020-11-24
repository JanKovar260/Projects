# deletes occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    new_list = [] # building the resulting list
    repeats = {} # for tracking the number of repeats in a dict
    for i in order:
        if i not in repeats and max_e > 0:
            repeats[i] = 1
            new_list.append(i)
        elif repeats[i] < max_e:
            repeats[i] += 1
            new_list.append(i)
    return new_list


input = [1,1,3,3,7,2,2,2,2,7,2,2,3,7,1,1,7]

max_e = 2

test = delete_nth(input, max_e)
print(test)