#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]  # include all characters starting from index n
word_last_2 = word[-2:]  # exclude all characters from the right starting from index n
middle_word = word[1:-1]  # remove the first and last character
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
