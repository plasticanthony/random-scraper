import requests
from bs4 import BeautifulSoup
import random

# Enter valid username and password for Princeton account.
username = 'USERNAME'
password = 'PASSWORD'

url = 'https://www.princeton.edu/collegefacebook/search/'

# Select the number of random names you would like.
num_to_scrape = 30

# Format query based on desired population.
year = '2021';
og_query = '?year=' + year

r = requests.get(url + og_query, auth=(username, password))  
page = r.content

soup = BeautifulSoup(page, "html5lib")
num_pages_html = soup.find_all("span", {"class": "total"}, limit=1)
num_pages = ''.join(i for i in num_pages_html[0] if not i.isdigit()).replace('of ', '')

chosen_ones = []

while len(chosen_ones) < num_to_scrape:
	# go to a random page of the filtered search results
	rand_page = random.randint(1, int(num_pages) + 1)
	# reset query and get page html
	query = og_query + '&page=' + str(rand_page)
	
	print "Selecting from page number: " + str(rand_page) + "  query is: " + query

	r = requests.get(url + query, auth=(username, password))  
	page = r.content

	soup = BeautifulSoup(page, "html5lib")
	people = soup.find_all("div", {"class": "result"})

	index = random.randint(0, len(people) - 1)
	rand_person = people[index]
	name = rand_person.contents[1].find("div", {"class", "name"}).string
	email = rand_person.contents[1].find("div", {"class", "email"}).string

	info = (name, email)

	if (info not in chosen_ones):
		chosen_ones.append((name, email))


for chosen in chosen_ones:
	print chosen[0] + "   " + chosen[1]




