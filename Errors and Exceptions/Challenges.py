'''
### Problem 1
Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.

'''

try:
    for i in ['a','b','c']:
        print(int(i**2))
except:
    print("Your list is not filled with integers")

# Output --> Your list is not filled with integers

'''
Problem 2
Handle the exception thrown by the code below by using <code>try</code> and <code>except</code> blocks.
Then use a <code>finally</code> block to print 'All Done.'
'''

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("You can't divide a number with 0")
finally:
    print("All Done.")

''' Ouput to the function:

    You can't divide a number with 0
    All Done.

'''

'''
Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
'''

def ask():
    while True:
        try:
            square = int(input('Please provide a number: '))
        except:
            print("Value given isn't an integer\nPlease try again!")
        else:
            print("All Done.")
            break
    print(square**2)

ask()

'''
Output:
Please provide a number: null
Value given isn't an integer
Please try again!
Please provide a number: 12
All Done.
144
'''
