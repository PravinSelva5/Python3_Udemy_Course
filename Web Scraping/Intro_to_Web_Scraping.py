'''
----------------------------------
     RULES FOR WEB SCRAPING
----------------------------------

- Always try to get permission before scraping, 
- If you don't and make too many attempts/requests, your IP maybe blocked


----------------------------------
    LIMITATIONS OF WEB SCRAPING
----------------------------------

- Every website it unique, therefore every web scraping script is UNIQUE
- A slight change or update to a website MAY completely break your web scraping script


AT COMMAND LINE:    

pip3 install requests  -- allows you to make a request to a website and get information from it
pip3 install lxml -- allows you to decipher whatever requests returns
pip install bs4 
'''

# GRABBING THE TITLE OF A WEB PAGE

import requests
import bs4

result = requests.get('http://www.example.com')
print(type(result))

#print(result.text)

soup = bs4.BeautifulSoup(result.text, 'lxml')
#print(soup)  # it'll make it easier to read

soup.select('title') # will return a list when printed

title = soup.select('title')[0].getText()

print(title)