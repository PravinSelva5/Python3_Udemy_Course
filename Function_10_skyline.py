'''
Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
Assume that the incoming string contains letters, and don't worry about numbers, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate through the string.
'''

def myfunc(*arg):
    new = []
    for i in range(len(arg)):
        args = list(arg)
        for j in range(len(args[i])):
            if j%2 == 0:
                tmp = args[i][j].upper()
                new.append(tmp)
            else:
                new.append(args[i][j])
        return "".join(new)
