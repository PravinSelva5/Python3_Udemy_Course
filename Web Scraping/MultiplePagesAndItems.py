'''
GOAL: Get a title of every book with a 2 star rating

'''

import requests, bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
len(soup.select(".product_pod"))   # will give you 20 which makes sense becuase there are 20 items in each page

products = soup.select(".product_pod")

example = products[0]
#print(example)

# The quick and dirty way to check if something is rated with two stars
'star-rating Two' in str(example)


# You can use the select soup method because example is a beautiful soup object
[] ==  example.select(".star-rating.Two")


# To grab the title of the book
print(example.select('a')[1]['title']) #because the example.select is a bs4 element tag ( if you check the type), you can call the parameters as a dictonary


# We can check if something is 2 strings (string call in  or example.select(rating))
# example.select('a')[1]['title'] to grab the book title

two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)

# OBJECT NOT CALLABLE, TYPE ERROER APPEARING. NEED TO CHECK IT OUT NEXT TIME


