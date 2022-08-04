import re


def find_missing_letters(letter):
    for i in range(1, len(letter)):
        a = re.findall(r'[a-zA-Z]', letter)
        if i not in a:
            return i


w = ["a", "b", "c", "d", "f"]
e = ["O", "Q", "R", "S"]

print(find_missing_letters(w))
