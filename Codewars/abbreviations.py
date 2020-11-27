# creates abbreviations of words of length 4 and longer while maintaining all the other symbols
def abbreviate(s):
    result = ""
    to_list = []

    for i in s:
        if i.isalpha():
            result += i
        else:
            if result > "":
                to_list.append(result)
                result = i
                to_list.append(result)
                result = ""
            else:
                to_list.append(" ")
                result = ""
    if len(result) > 1:
        to_list.append(result)
        result = ""

    for x in to_list:
        if len(x) >= 4:
            result += x[0] + str(len(x) - 2) + x[-1]
        else:
            result += x

    return result

if __name__ == '__main__':
    s = "elephant-rides are really fun!"
    test = abbreviate(s)
    print(test)

# kod je trochu vice komplikovany nez by musel byt, protoze se pri testovani objevily problemy s dublovanim/mizenim mezer
# priklad testovaciho kodu Testing: "is-monolithic; is'monolithic. balloon_cat is. sits_", expecting: "is-m8c; is'm8c. b5n_cat is. s2s_"
