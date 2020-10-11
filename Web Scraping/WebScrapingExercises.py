import requests, bs4

'''
TASK 1: USE REQUESTS LIBRARY & BEAUTIFUL SOUP TO CONNEC TO WEBSITE AND GET THE HTML TEXT FROM THE HOMEPAGE
'''

res = requests.get('http://quotes.toscrape.com/')
# print(res.text)


'''
TASK 2: GET THE NAMES OF ALL THE AUTHORS ON THE FIRST PAGE
'''

soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.author')

authors = set()

for name in soup.select('.author'):
    authors.add(name.text)

print(authors)


'''
TASK 3: Create a list of all the quotes on the first page
'''
quotes = []

for quote in soup.select('.text'):
    quotes.append(quote.text)

print(quotes)


'''
TASK 4: INSPECT THE SITE & USE BEAUTIFUL SOUP TO EXTRACT THE TOP TEN TAGS FROM THE REQUESTS TEXT SHOWN ON THE TOP RIGHT 
        FROM THE HOME PAGE
        *** KEEP IN MIND, THERE ARE ALSO TAGS UNDERNEATH EACH QUOTE, TRY TO FIND A CLASS ONLY PRESENT IN THE TOP RIGHT TAGS ***
'''

for item in soup.select(".tag-item"):
    print(item.text)


'''
TASK 5: NOTICE HOW THERE IS MORE THAN ONE PAGE, AND SUBSEQUENT PAGES LOOK LIKE THIS http://quotes.toscrape.com/page/2/.
        Figure out how to loop through all the pages AND GET ALL THE UNIQUE AUTHORS ON THE WEBSITE
'''

url = 'http://quotes.toscrape.com/page/'

authors = set()
page_still_valid = True
page = 1

while(page_still_valid):

    page_url = url + str(page)

    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        break

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select(".author"):
        authors.add(name.text)

    page += 1


print('All unique authors')
print(authors)
