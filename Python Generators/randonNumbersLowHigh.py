'''
Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library.
'''
import random
def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)

'''
CHECK ANSWER WITH

for num in rand_num(1,10,12):
    print(num)

'''



'''
------------
PROBLEM 4
------------

Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

    - If the output has the potential to take up a lot of memory and you only intend to iterate through it and you don't want the entire thing at once. It may be better to use the yeild statement

-----------------------
### Extra Credit!
---------------------
Can you explain what *gencomp* is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)


my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

    - Exactly like the name sounds, just like a list comprehension, gencomp is a GENERATOR COMPREHENSION

'''