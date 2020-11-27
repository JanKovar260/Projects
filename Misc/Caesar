# funkce encrypt posune zadany text o uzivatelem dany pocet znaku
def encrypt(plaintext, key):
    result = ""
    for i in plaintext:
        if i.isupper():
            i_index = ord(i) - ord("A")
            i_shifted = (i_index + key) % 26 + ord("A")
            znak = chr(i_shifted)
            result += znak
        elif i.islower():
            i_index = ord(i) - ord("a")
            i_shifted = (i_index + key) % 26 + ord("a")
            znak = chr(i_shifted)
            result += znak
        elif i.isdigit():
            i_index = ord(i) - ord("0")
            i_shifted = (i_index + key) % 10 + ord("0")
            znak = chr(i_shifted)
            result += znak
        else:
            result += i
    return result

text = "V 9:OO hodin jdu do prace."
cyphered_message = encrypt(text, 5)
print(cyphered_message)

# decryptor pro prevod textu zpet do srozumitelne podoby
def decrypt(plaintext, key):
    result = ""
    for i in plaintext:
        if i.isupper():
            i_index = ord(i) - ord("A")
            i_shifted = (i_index - key) % 26 + ord("A")
            znak = chr(i_shifted)
            result += znak
        elif i.islower():
            i_index = ord(i) - ord("a")
            i_shifted = (i_index - key) % 26 + ord("a")
            znak = chr(i_shifted)
            result += znak
        elif i.isdigit():
            i_index = ord(i) - ord("0")
            i_shifted = (i_index - key) % 10 + ord("0")
            znak = chr(i_shifted)
            result += znak
        else:
            result += i
    return result

print(decrypt(cyphered_message, 5))

# zobrazi vsechny mozne posuny
def hack_the_cipher(sifrovana_zprava):
    results = []
    for key in range(1, 27):
        result = ""
        for i in sifrovana_zprava:
            if i.isupper():
                i_index = ord(i) - ord("A")
                i_shifted = (i_index - key) % 26 + ord("A")
                znak = chr(i_shifted)
                result += znak
            elif i.islower():
                i_index = ord(i) - ord("a")
                i_shifted = (i_index - key) % 26 + ord("a")
                znak = chr(i_shifted)
                result += znak
            elif i.isdigit():
                i_index = ord(i) - ord("0")
                i_shifted = (i_index - key) % 10 + ord("0")
                znak = chr(i_shifted)
                result += znak
            else:
                result += i
        results.append(result)
    return results


test = hack_the_cipher(cyphered_message)
print(test)
