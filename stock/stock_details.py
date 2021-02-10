import tabulate
from database import database


class Stock:

	def stock_details():

		dict_book = database.Database.read_db()
		while True:
			print("""
				1. Books in Stock
				2. Issued Books
				3. Back to main menu 
				""")
			choice=int(input("Enter Choice:"))
			if choice==1:
				dataset = dict_book['book']
				header = dict_book['book'][0].keys()
				rows =  [x.values() for x in dataset]
				print (tabulate.tabulate(rows, header))

			elif choice==2:
				dataset = dict_book['user_details']
				header = dict_book['user_details'][0].keys()
				rows =  [x.values() for x in dataset]
				print (tabulate.tabulate(rows, header))
			else:
				break




