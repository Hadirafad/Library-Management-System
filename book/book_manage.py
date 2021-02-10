from database import database

class Book:

    flag = False

#Add book

    def add_book():
        Book.flag = False
        database.Database.create_db()
        dict_book = database.Database.read_db()
        book_id = input("Book ID: ")
        for x in dict_book['book']:
            if book_id == x['book_id']:
                Book.flag = True
                print("Book already exists")

        if Book.flag == False:
            title = input("Enter the book name :")
            author = input("Author: ")
            try:
                copies = int(input("No.of copies: "))
                dict_book['book'].append({'book_id':book_id, 'title':title, 'author':author, 'copies':copies, 'permanent_count':copies})
                print("Book added successfully")
            except:
                print("Enter a number")
            
        #generate separate id for each book
        try:
            i = 1
            while i<=copies:
                separate_id = book_id + str(i)
                dict_book['book_details'].append({'book_id':book_id, 'separate_id':separate_id})
                i+=1
        except:
            pass

        database.Database.write_db(dict_book)
            

#Delete book using separate ID

    def delete_book():
        del_bid = input("Enter Book id to delete: ")
        del_id = input("Enter individual id of book: ")
        dict_book = database.Database.read_db()
        for x in dict_book['book_details']:
            if x['separate_id'] == del_id:
                Book.flag = True
                dict_book['book_details'].remove(x)
                for x in dict_book['book']:       
                    if (x['book_id'] == del_bid):
                        x.update({'copies':x['copies']-1, 'permanent_count':x['permanent_count']-1})
                        print("Book removed successfully")         
        if Book.flag == False:
            print("Invalid ID")

        database.Database.write_db(dict_book)

#Search book using ID, Title, Author

    def search_book():
        dict_book = database.Database.read_db()

        while True:
            print("""
                1. Search by Title
                2. Search by Author
                3. Search by ID
                4. Back to main menu
                """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                s_title = input("Enter Title: ")
                for x in dict_book['book']:
                    if x['title'] == s_title:
                        Book.flag = True
                        print("book_id : ",x['book_id'],"\nauthor: ",x['author'],"\nNo.of copies Available: ",x['copies'])
                if Book.flag == False:
                    print("Invalid title")
            
            elif choice==2:
                s_author = input("Enter author: ")
                for x in dict_book['book']:
                    if x['author'] == s_author:
                        Book.flag = True
                        print("book_id : ",x['book_id'],"\nTitle: ",x['title'],"\nNo.of copies Available: ",x['copies'])
                if Book.flag == False:
                    print("Invalid author name")

            elif choice==3:
                s_id = input("Enter Book ID: ")
                for x in dict_book['book']:
                    if x['book_id'] == s_id:
                        Book.flag = True
                        print("book_id : ",x['book_id'],"\nTitle: ",x['title'],"\nAuthor :",x['author'],"\nNo.of copies Available: ",x['copies'])
                if Book.flag == False:
                    print("Invalid ID")
            else:
                break
                
#Update book details such as author and title

    def update_book():
        update_id = input("Enter Book id to update: ")
        dict_book = database.Database.read_db()
        for x in dict_book['book']:
            if x['book_id'] == update_id:
                Book.flag = True
                new_title = input("Enter new title: ")
                new_author = input("Enter author: ")
                x.update({'book_id':update_id, 'title':new_title, 'author':new_author})
                print("Book updated successfully")
        if Book.flag == False:
            print("Invalid ID")

        database.Database.write_db(dict_book)

#Update count of books

    def addbook_count():
        book_id = input("book id: ")
        dict_book = database.Database.read_db()

        try:
            new_copies = int(input("No.of copies: "))
            for x in dict_book['book']:
                if x['book_id'] == book_id:
                    cp = x['permanent_count'] +1
                    x.update({'copies':x['copies']+new_copies, 'permanent_count':x['permanent_count']+new_copies})
        except :
            print("Invalid count...")
        
            #generate separate id for each book
        try:
            i = 1
            while i<=new_copies:
                separate_id = book_id + str(cp)
                dict_book['book_details'].append({'book_id':book_id, 'separate_id':separate_id})
                i+=1
                cp+=1
            print("Book count Updated...")
        except:
            print("Invalid ID")
            
                
        database.Database.write_db(dict_book)
