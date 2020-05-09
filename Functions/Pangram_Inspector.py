'''
Write a Python function to check whether a string is pangram or not

    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"

'''
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    letter_counter = list(alphabet)
    #Checking whether the string contains every letter of the alphabet at least once by removing a letter from the alphabet list every time the string contains the letter
    for i in str1.lower():
        for j in letter_counter:
            if i == j:
                letter_counter.remove(j)
            else:
                continue
    #Checking whether the alphabet list is empty. If it is empty, then the string provided is an pangram
    if len(letter_counter) == 0:
        return 'String is a pangram'
    else:
        return 'String is not a pangram'

# Check 1 = Pass
ispangram("The quick brown fox jumps over the lazy dog")

#Check 2 = Pass
ispangram('Pack my box with five dozen liquor jugs')

#Check 3 = Pass
ispangram('Waltz, nymph, for quick jigs vex Bud.')

#Check 4 = Fail
ispangram("I like bikes")


# The set function can also be used to simplify the code 
