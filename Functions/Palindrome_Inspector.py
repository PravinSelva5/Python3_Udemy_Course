'''
Write a Python function that checks whether a passed in string is palindrome or not.
'''

def palindrome(s):
    reversed_order = s[::-1]
    if s == reversed_order:
        return 'String is palindrome!'
    else:
        return 'String is not palindrome!'

# Check 1
palindrome('madam')

# Check 2
palindrome('helleh')

# Check 3
palindrome('Tesla')
