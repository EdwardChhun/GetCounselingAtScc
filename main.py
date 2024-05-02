"""
Making In-person appointments only for now at SCC
Website : "https://esars.scc.losrios.edu/esars/counseling_ip/eSARS.asp?WCI=Init&WCE=Settings"
Basics: Making an appointment for [Consortium]
To Do: Scrape the data and search for "Counselors" and "Times available"
"""
import requests 
from bs4 import BeautifulSoup
# Making a GET request 
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 
  
# check status code for response received 
# success code - 200 
print(r) 
print(".... \n")
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser') 

s = soup.find('div', class_='entry-content')

# This will find all the tags
content = s.find_all('p')

print(content)