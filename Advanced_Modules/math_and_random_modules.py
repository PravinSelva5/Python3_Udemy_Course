import math

value = 4.35

math.floor(value) # 4

math.ceil(value) # 5

round(4.5) # 4

round(5.5) # 6

print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
print(math.log(math.e))


# Look into pseudorandom number generator and random seed

import random

random.randint(0,100)

mylist = list(range(0,20))

'''
Setting a seed allows us to start from a seeded psuedorandom number generator, which means the same random numbers will show up in a series. 
Note, you need the seed to be in the same cell if your using jupyter to guarantee the same results each time. Getting a same set of random numbers can be important in situations where you will be trying different variations of functions and
want to compare their performance on random values, but want to do it fairly
'''

# SAMPLE WITH REPLACEMENT (some numbers will be duplicated when below is excuted)
random.choices(population=mylist, k=10)

# SAMPLE WITHOUT REPLACEMENT (all unique choices are picked)
random.sample(population=mylist,k=10)

random.shuffle(mylist)

# DISTRIBUTIONS EXAMPLE

random.uniform(a=0, b=100)

random.gauss(mu=0, sigma=1)

# look into python's numpy library