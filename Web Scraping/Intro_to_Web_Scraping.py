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

'''
----------------------------------
GRABBING A TITLE FROM A WEB PAGE
----------------------------------
'''

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

'''
----------------------------------
  GRABBING A ELEMENTS OF A CLASS
----------------------------------
'''

res2 = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup2 = bs4.BeautifulSoup(res2.text, "lxml")

first_item = soup2.select('.toctext')[0]

# print(first_item.text)

for item in soup2.select('.toctext'):
    print(item.text)


'''
-----------------------------------------
        GRABBING AN IMAGE
-----------------------------------------
- ALWAYS check copyright permissions 
  before downloading from a website
-----------------------------------------
'''


res3 = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res3.text, 'lxml')

computer = soup.select('.thumbimage')[0]

print(computer['src']) # take the URL given and create a new request


image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

# print(image_link.content)

f = open('my_computer_image.jpg', 'wb') # wb = write binary, binary representation of the image

f.write(image_link.content)

f.close()


