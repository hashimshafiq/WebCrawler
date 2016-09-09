import requests
from bs4 import BeautifulSoup
import csv

def spider(max_pages):
	pages = 1
	while pages <= max_pages:
		url = 'https://thenewboston.com/forum/search_forums.php?s=&orderby=popular&page='+str(pages)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,"html")
		for link in soup.findAll('a',{'class':'title text-semibold'}):
			href = link.get('href')
			#print(href)
			get_item_data(href)
		pages = pages+1

def get_item_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html")
	for link in soup.findAll('a',{'class':'title text-semibold'}):
		title = link.string
		print(title)
		
	
spider(1)
		
		
