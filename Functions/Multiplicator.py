'''
Write a Python function to multiply all the numbers in a list.**

    Sample List : [1, 2, 3, -4]
    Expected Output : -24
'''

def multiply(numbers):
    product = numbers[0]
    for i in numbers[1:]:
        product = product * i
    return product

#Check 1 = -24
multiply([1,2,3,-4])

# Check 2 = 120
multiply([5,4,3,2,1])
