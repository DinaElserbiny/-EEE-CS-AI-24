"""
Write a function that takes two sets as input and returns a new set containing the common elements.


"""
import random
import string

def generate_password():

    characters = string.ascii_letters + string.digits


    password = ''.join(random.choice(characters) for _ in range(8))
    
    return password


print("Random Password:", generate_password())
