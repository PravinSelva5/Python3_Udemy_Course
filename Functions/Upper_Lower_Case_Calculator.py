'''
**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output :
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: **.isupper()** and **.islower()**
'''

def up_low(s):
    Upper = 0
    Lower = 0
    for i in s:
        if i.isupper():
            Upper += 1
        elif i.islower():
            Lower += 1
        else:
            continue
    print("Expected Output: \n")
    print(f'No. of Upper case characters: {Upper}')
    print(f'No. of Lower case characters: {Lower}')


# Use sample string above to check if your function is working accordingly.
