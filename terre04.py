import sys


list_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
a = ""
for i in list_alphabet[list_alphabet.index(sys.argv[1]):]:
    a = a + i
print(a)
