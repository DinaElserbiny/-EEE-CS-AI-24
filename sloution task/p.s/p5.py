"""
Problem 5
-Write a Python program that checks if a given word is a palindrome. A palindrome is a word that reads the same backward as forward.
Input: "level"
Output: "The word 'level' is a palindrome."


"""
word = input("Enter a word: ")
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

if word == reversed_word:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")
