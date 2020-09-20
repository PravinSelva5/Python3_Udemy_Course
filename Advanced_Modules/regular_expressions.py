'''
PART 1

Regular expressions are text-matching patterns described with a formal syntax. You'll often hear regular expressions referred to as 'regex' or 'regexp' in conversation. 
Regular expressions can include a variety of rules, from finding repetition, to text-matching, and much more. 
As you advance in Python you'll see that a lot of your parsing problems can be solved with regular expressions (they're also a common interview question!).
'''

import re

text = "The agent's phone number is 408-555-1234. Call soon!"

print('phone' in text)

# Using regular expressions

pattern = 'phone'

print(re.search(pattern, text))  # tells you if there is a match AND WILL RETURN THE FIRST OCCURENCE and where the actual index location spans too (start_index, finish_index)

pattern2 = 'NOT IN TEXT'

print(re.search(pattern2, text)) # Will return none because the pattern 'phone' is not present

match = re.search(pattern, text)

# Methods you can use with the return object of the search function

print(match.span()) # Span of the index location will be printed

print(match.start()) # Beginning index

print(match.end()) # print end index location


text2 = 'my phone once, my phone twice'

match2 = re.search('phone', text2) # you will only get the indexes of the first 'phone' occurence. The other occurence won't be returned

# To return all possible occurences of the pattern we are searching for:

matches = re.findall('phone', text2)

print(len(matches))

# You can use match as an iterable object as well
for matches in re.finditer('phone',text):
    print(match)
    print(match.span())


'''
PART 2 --- BUILDING PATTERNS WITH IDENTIFIER SYNTAX

Character Identifiers:

\d -- a digit
\w -- alphanumeric
\s -- whitespace
\D -- a non digit
\W -- Non-alphanumeric
\S -- Non-whitespace

Quantifiers:

+ -- occurs on or more times
{3} -- occurs exactly 3 times
{2,4} -- occurs 2 to 4 times
{3,} -- occurs 3 or more
* -- occurs zero or more times
? -- once or none

'''

text3 = 'My phone number is 408-555-1234'
phone3 = re.search(r'\d{3}-\d{3}-\d{4}', text3)
print(phone3)



# You can call from group position because of re.compile. It allows you to grab sub-sections of a pattern

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern, text)

print(results.group(1)) 
print(results.group(2))
print(results.group(3))
print(results.group())


'''
PART 3 - Additional Regex Syntax
'''

print(re.search(r'cat|dog','The cat is here'))

print(re.findall(r'at', 'The cat in the hat sat there.'))

print(re.findall(r'...at', 'The cat in the hat went splat.'))

print(re.findall(r'^\d', '1 is a number'))  # Checks to see if the string starts with a number



phrase = 'There are three numbers 34 inside 5 this sentence'

# To exclude a char or an int when searching a string

pattern3 = r'[^\d]'

no_numbers = re.findall(pattern3, phrase)

print(no_numbers)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

no_punctuation = re.findall(r'[^!.?]+', test_phrase)

print(no_punctuation)