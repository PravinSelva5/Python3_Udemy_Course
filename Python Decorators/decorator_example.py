"""
In the previous example we actually manually created a Decorator. Here we will modify it to make its use case clear:

"""

def new_decorator(func):
    
    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

'''
HOW TO USE THE @ OPERATOR TO REDUCE THE ABOVE SYNTAX


@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator)


THE OUTPUT WILL BE THE SAME:

Code would be here, before executing the func
This function is in need of a Decorator
Code here will execute after the func()

'''