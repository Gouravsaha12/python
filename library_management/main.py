books = [{'name':"behave", 'value':800, "author":"robert sapolsky", 'type':"biology"}]

def add_book(book_dict):
    books.append(book_dict)
    return f"Book '{book_dict['name']}' added successfully"

while True:
    print("\n1. Add a book")
    print("\n2. Display all books")
    print("\n3. Exit")

    inp = int(input("\n"))
    if inp==1:
        name = input("Enter book name: ")
        value = float(input("Enter book value: "))
        author = input("Enter book author: ")
        type = input("Enter book type: ")
        add_book({'name':name, 'value':value, 'author':author, 'type':type})
    
    elif inp==2:
        print("\nAll books:")
        for book in books:
            print(f"{book['name']}: ${book['value']} - by {book['author']} ({book['type']})")
    
    elif inp==3:
        print("\nExiting...")
        break