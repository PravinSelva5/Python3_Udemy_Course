'''
-------------------------
   Timing your code
-------------------------

Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project. Python has a built-in timing module to do this. 
'''

def func_one(n):
    return [str(num) for num in range(n)]

def func_two(n):
    return list(map(str, range(n)))


# Same answer but which function is MORE EFFICIENT?
print(func_one(10))
print(func_two(10))

import time

# CURRENT TIME BEFORE
start_time = time.time()

# RUN CODE
result = func_one(1000000)

# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()

# ELAPSED TIME
elapsed_time = end_time - start_time
print("Elapsed time for Function 1")
print(elapsed_time)


# CURRENT TIME BEFORE
start_time = time.time()

# RUN CODE
result = func_two(1000000)

# CURRENT TIME AFTER RUNNING CODE
end_time = time.time()

# ELAPSED TIME
elapsed_time = end_time - start_time
print("Elapsed time for Function 2")
print(elapsed_time)


'''
TO CHECK IF WHICH FUNCTION IS MORE EFFICIENT
'''

import timeit

stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=100000))

