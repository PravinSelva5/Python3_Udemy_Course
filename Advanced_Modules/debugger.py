'''
# Python Debugger

You've probably used a variety of print statements to try to find errors in your code. A better way of doing this is by using Python's built-in debugger module (pdb). The pdb module implements an interactive debugging environment for Python programs. 
It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, so you can understand what your program actually does and find bugs in the logic.
This is a bit difficult to show since it requires creating an error on purpose, but hopefully this simple example illustrates the power of the pdb module. <br>*Note: Keep in mind it would be pretty unusual to use pdb in an iPython Notebook setting.*

___
Here we will create an error on purpose, trying to add a list to an int

x = [1,2,3]
y = 2
z = 3

result = y + z
result2 = x + y 

ERROR WILl SHOW UP ---> TypeError: can only concatenate list (not "int") to list
'''

import pdb

x = [1,2,3]
y = 2
z = 3

result1 = y + z
# You can set a trace before the error line to get a better idea of what's happening with the help of the pdb library
# The trace always to see your variables current values and preform operations to help you better understand how to solve the error you're looking at
# TO QUIT THE DEBUGGER JUST TYPE 'q'

pdb.set_trace()
result2 = x + y 