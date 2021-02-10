from database import database

class ReturnBook:

	def return_book():

		r_id = input("Enter Book Id to return: ")
		sep_id = input("Enter Individual Id of book: ")
		dict_book = database.Database.read_db()
		flag = False
		for x in dict_book['user_details']:
			if x['book_id'] == r_id and x['separate_id'] == sep_id:
				flag = True
				dict_book['user_details'].remove(x)
				for x in dict_book['book']:       
					if (x['book_id'] == r_id):
						x.update({'copies':x['copies']+1})
						print("Book returned...")
		if flag == False:
			print("Invalid ID")


		database.Database.write_db(dict_book)
