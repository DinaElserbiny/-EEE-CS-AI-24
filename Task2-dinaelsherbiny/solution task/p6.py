"""
Write a program that asks the user for input and 
handles the possibility of the user entering a non-numeric value.

"""


while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)  # Convert the input to a float
        print("You entered:", number)
        break  # Break out of the loop if input is valid
    except ValueError:
        print("Error: Please enter a valid numeric value.")
