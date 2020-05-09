'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

def paper_doll(text):
    list = []
    for i in range(len(text)):
        list += text[i] * 3
    return "".join(list)

# Check 1
paper_doll('Hello')

# Check 2
paper_doll('Mississippi')
