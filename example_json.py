import json
from pprint import pprint

with open ('add_recept_book.json') as add_recept_book_file:
	movie = json.load(add_recept_book_file)
	pprint(movie)