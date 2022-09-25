class laibrary:
    def __init__(self, ListOfbook):
        self.books = ListOfbook

    def displayAvailibleBooks(self):
        print("book Avialible in laibrary ")
        for book in self.books:
            print(" *" + book)
          
    def BorrowBook(self, bookName):
        if bookName in self.books:
         print(f"This Book {bookName} have Been issue you  ")
         self.books.remove(bookName)
         
        else:
             print("Sorry This Book have been issued someone! ")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thank for using this book{bookName} in our laibrary ")
         
class Student:
    def requestBook(self):
        self.books = input("Enter The Book Name which one you Needed ")
        return self.books

    def returnBook(self):
        self.books = input("Enter The Book which one you return ")
        return self.books


if __name__ == "__main__":
     OurLaibrary = laibrary(["python", "css"])
     student = Student()


while(True):
    welcomemsg = '''WELCOME TO OUR LAIBRARY
      1.LIST OF ALL THE BOOKS
      2.REQUEST OF THE BOOKS
      3.RETURN/ADD BOOKS
      4.QIUT THE LAIBRARY

      '''
    print(welcomemsg)
    


    a = int(input("ENTER A CHOICE "))
    

    if a== ():
        print("please choose a number" )
    elif a == 1:
        OurLaibrary.displayAvailibleBooks()
    elif a == 2:
        OurLaibrary.BorrowBook(student.requestBook())
    elif a == 3:
        OurLaibrary.returnBook(student.returnBook())
    elif a == 4:
        print("THANKS FOR USING OUE LAIBRARY")

        exit()
    else:
        print("invalid sayntax!")
