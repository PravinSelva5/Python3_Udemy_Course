'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14
'''

def summer_69(arr):
    sum = 0
    sum_69 = False
    for i in range(len(arr)):
        if sum_69:
            if arr[i] == 9:
                sum_69 = False
        elif arr[i] == 6:
            sum_69 = True
        else:
            sum += arr[i]
    return sum

# Check 1
summer_69([1, 3, 5])

# Check 2
summer_69([4, 5, 6, 7, 8, 9])

# Check 3
summer_69([2, 1, 6, 9, 11])
