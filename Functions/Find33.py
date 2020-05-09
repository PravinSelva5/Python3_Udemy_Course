'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
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
