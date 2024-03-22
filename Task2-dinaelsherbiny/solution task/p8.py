"""
Generate a random password of 8 characters, including a mix of uppercase letters, lowercase letters, and numbers.

"""

import random
import string

def generate_password():

    characters = string.ascii_letters + string.digits


    password = ''.join(random.choice(characters) for _ in range(8))
    
    return password


print("Random Password:", generate_password())
