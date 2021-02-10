from database import database


class IssueBook:

	def issue_book():
	
		i_id = input("Enter Book Id to issue: ")
		sep_id = input("Enter Individual Book Id: ")
		dict_book = database.Database.read_db()
		flag = False
		for x in dict_book['book']:
			for z in dict_book['book_details']: 
				if x['book_id'] == i_id and z['separate_id'] == sep_id:
					print("book_id : ",x['book_id'],"\nTitle: ",x['title'],"\nAuthor :",x['author'],"\nNo.of copies Available: ",x['copies'])
					if x['copies'] != 0:
						flag = True
						user_name = input("Enter Name: ")
						user_phone =  input("Enter Phone: ")
						user_place = input("Enter place: ")
						for x in dict_book['book']:       
							if (x['book_id'] == i_id):
								x.update({'copies':x['copies']-1})

								dict_book['user_details'].append({'name':user_name, 'phone':user_phone, 'place':user_place, 'book_id':i_id, 'separate_id':sep_id})
								print("Book issued successfully")
		if flag == False:
			print("Invalid ID")

		database.Database.write_db(dict_book)
