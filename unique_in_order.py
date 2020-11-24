def unique_in_order(iterable):
    into_list = list(iterable)
    new_list = []
    for i, value in enumerate(into_list):
        current_value = value
        next_value = into_list[i + 1] if i < len(into_list) - 1 else None
        if current_value != next_value:
            new_list.append(into_list[i])
    return new_list

text = "AAAABBBCCDAABBB"

test = unique_in_order(text)

print(test)