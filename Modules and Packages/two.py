#two.py
import one


print("TOP LEVEL IN TWO.py")

one.func()

if __name__ == '__main__':
    print("TWO.py is being run directly")
else:
    print("TWO.py has been imported")
