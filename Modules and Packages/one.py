#one.py

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print("ONE.PY is being run directly!")
else:
    print("ONE.PY has been imported")

'''
Typically people don't add a if statement,

if __name__ == '__main__':
    #RUN THE SCRIPT

    #You just call all your functions and whatever logic you want to add depending on how you want the script to work
    

'''
