# Create a liberary class
# display book
# lend book - who owns the book if not present
# add book
# return book
# AniketLiberary = Liberary(listofbooks, liberary_name)
#dictionary books-nameofpreson

class PublicLiberary () :
    def __init__(self,list_of_books,library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.dictionary_of_book = {}



    def display_book(self):
        print(f"We have following books in {self.library_name} :")
        for book in self.list_of_books:
            print(book)
        # for index,books in enumerate(self.list_of_books) :
        #     print(f"{index} - {books}")
        # # return f"Books in Liberary are \n{self.list_of_books}"



    def lend_book(self, username, bookname):
        if bookname  in self.dictionary_of_book.keys() :
            print(f"Sorry this book is lend by :- {self.dictionary_of_book[bookname]}")
            # liste = list()
            # var = self.dictionary_of_book.items()
            # for item in var:
            #     if item[1] == bookname:
            #         list.append([0])
            #
            # for key in liste :
            #     print ('book is taken by ', key)
        else :
            self.dictionary_of_book.update({username: bookname})
            print("Lender book data has been updated")




    def add_book(self, bookname):
        self.list_of_books.append(bookname)

    def delete_book (book_name) :
        pass

    def return_book(self, username):
        if username in self.dictionary_of_book.keys() :
            del self.dictionary_of_book[username]

def main () :
    list_of_books = ["book1", "book2", "book3", "book4", "book5", "book6", "book7"]
    library_name = "Public Liberary"
    secret_key = 123456
    book = PublicLiberary(list_of_books,library_name)
    print(f"Welcome to {library_name} \nTo exit enter 'q' \nTo Display book enter 'd' \nTo Lend book enter 'l' \nTo Return book enter 'r' \nTo Donate book enter 'do' \nTo Delete book enter 'del' \n")
    exit = False
    while (exit is not True) :
        _input = input("Enter your option :- ")
        # user_name = str(input("Enter your name :- "))
        # display = int(input("enter 1 to display book :- "))
        if _input == 'q':
            exit = True
        elif _input == 'd' :
            print(book.display_book())

        elif _input == "l" :
            _input2 = input("Enter your name :- ")
            _input3 = input("Which book you want to lend :- ")
            book.lend_book(_input2,_input3)
            print(book.dictionary_of_book)

        elif _input == "do" :
            book_name = str(input("Enter name of book which you want to donate :- "))
            book.add_book(book_name)
            print(book.list_of_books)

        elif _input == "del" :
            _input_secret = int(input("Enter secret key :- "))
            if _input_secret == secret_key :
                _input2 = input("Which book you want to delete :- ")
                book.delete_book (_input2)

        elif _input == "r" :
            _input2 = input("Enter your name :- ")
            _input3 = input("Which book you want to return :- ")
            book.return_book(_input2)

if __name__ == "__main__" :
    main()






