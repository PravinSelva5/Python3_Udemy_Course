'''
Write a function that checks whether a number is in a given range (inclusive of high and low)
'''

def ran_check(num,low,high):
    if num <= high and num >= low:
        print(f'{num} is in the range between {low} and {high}')

# Check
ran_check(5,2,7)

'''
If you wanted the function to return a bool value. The function would look like this:

def ran_bool(num,low,high):
    if num <= high and num >= low:
        return True
    else:
        return False

ran_bool(3,1,10)

'''
