from book import book_manage
from database import database
from issue_book import issue_book
from return_book import return_book
from stock import stock_details

class Main:

    def main():

        
        while True:
            print(""" ======LIBRARY MENU=======
                1. Add New Book
                2. Add Book Count
                3. Issue Book
                4. Return Book
                5. Update Book
                6. Search Book
                7. View Books
                8. Delete Book
                9. Exit
                """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                book_manage.Book.add_book()
            elif choice==2:
                book_manage.Book.addbook_count()
            elif choice==3:
                issue_book.IssueBook.issue_book()
            elif choice==4:
                return_book.ReturnBook.return_book()
            elif choice==5:
                book_manage.Book.update_book()
            elif choice==6:
                book_manage.Book.search_book()
            elif choice==7:
                stock_details.Stock.stock_details()
            elif choice==8:
                book_manage.Book.delete_book()
            else:
                break
                    
Main.main()