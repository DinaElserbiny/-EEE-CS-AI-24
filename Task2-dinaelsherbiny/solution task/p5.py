
"""
Create a dictionary representing a library catalogue. 
Each book should have a title, author, and publication year.
"""

library_catalogue = {
    "book1": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925
    },
    "book2": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960
    },
    "book3": {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949
    },

}


book1_title = library_catalogue["book1"]["title"]
book1_author = library_catalogue["book1"]["author"]
book1_publication_year = library_catalogue["book1"]["publication_year"]

print("Book Title:", book1_title)
print("Author:", book1_author)
print("Publication Year:", book1_publication_year)
