
"""
Create a program that reads a text file, counts the occurrences of each word, and prints the results.
Sample.txt



"""
file_name = "Sample.txt"

try:
    with open(file_name, 'r') as file:

        content = file.read()


        words = content.split()


        word_counts = {}


        for word in words:
            word = word.lower()  
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1


        print("Word counts:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except PermissionError:
    print(f"Error: Permission denied to read file '{file_name}'.")
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")
