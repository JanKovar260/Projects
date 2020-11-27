# Evaluates the required reading level of a reader based on the difficulty of the inserted English text; calculated via Coleman-Liau index

text = input("Text: ")

letters = 0
words = 0
sentences = 0

for index, letter in enumerate(text):
    if letter.isalpha():
        letters += 1
    if index + 1 < len(text):
        if letter == " ":
            words += 1
        if (letter == "!" or letter == "?" or letter == ".") and text[index+1] == " ":
            sentences += 1
    if index + 1 == len(text):
        if (letter == "!" or letter == "?" or letter == "."):
            sentences += 1
            words += 1

L = letters * 100 / words
S = sentences * 100 / words

#Coleman-Liau index
index = (0.0588 * L) - (0.296 * S) - 15.8

grade = round(index)

if grade < 1:
    print("Before Grade 1")
elif (grade >= 1) and (grade <= 16):
    print(f"Grade {grade}")
else:
    print("Grade 16+")

# print(letters)
# print(words)
# print(sentences)
# print(index)

"""
TEST CASES
One fish. Two fish. Red fish. Blue fish. (Before Grade 1)
Would you like them here or there? I would not like them here or there. I would not like them anywhere. (Grade 2)
Congratulations! Today is your day. You're off to Great Places! You're off and away! (Grade 3)
Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more 
than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, 
in the dead of the night. And he also happened to be a wizard. (Grade 5)
In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since. (Grade 7)
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: 
once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it,
 "and what is the use of a book," thought Alice "without pictures or conversation?" (Grade 8)
 
When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed,
 and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious
  about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the
   back of his hand was at right angles to his body, his thumb parallel to his thigh. (Grade 8)
   
There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy. (Grade 9)
It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith,
 his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly
  through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl
   of gritty dust from entering along with him. (Grade 10)
A large class of computational problems involve the determination of properties of graphs, digraphs, 
integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains. (Grade 16+)
"""
