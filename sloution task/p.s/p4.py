"""
Problem 4
-Write a Python program that takes a sentence as input and reverses the order of words in the sentence.
Input: "Hello World"
Output: "World Hello"

"""
# Input sentence
input_sentence = input("Enter a sentence: ")

reversed_sentence = ""
current_word = ""

for char in input_sentence:
    if char != " ":
        current_word += char
    else:
        reversed_sentence = current_word 
        current_word = " "

reversed_sentence = current_word + " " + reversed_sentence

print("Reversed sentence:", reversed_sentence.strip())

