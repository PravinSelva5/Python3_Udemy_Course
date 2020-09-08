from collections import Counter

mylist = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,5,6]

# Count how many unique values are present in mylist with Counter

counts = Counter(mylist)
print(counts)

# this also works for strings

print(Counter('aaaasddddssrgseee'))

# What about for sentences?
sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.split()))

# Common patterns
letters = 'aaabbbbbbccccccdddddddddd'

c = Counter(letters)
print(c.most_common())

'''
------------------------------------------------
Common patterns when using the Counter() object
------------------------------------------------

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''

# Default Dictionary from the Collections Module

from collections import defaultdict

# If you ask for a key that isn't present in a default dictionary. It will assign it to with some default value.
# Example:

d = defaultdict(lambda: 0)

d['correct'] = 100
print(d['WRONG KEY'])
print(d)

'''
CONSTRUCTING A NAMEDTUPLE
'''
mytuple = (10,20,30)

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

sammy = Dog(age=5, breed='Husky', name='Sam')

