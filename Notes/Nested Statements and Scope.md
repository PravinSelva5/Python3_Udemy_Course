# Following Instructor


```python
x =25

def printer():
    x=50
    return x
```


```python
print(x)
```

    25



```python
print(printer())
```

    50


## LEGB Rule

This rule is basically the order in which python will look for variables in.
It starts off my checking:
1. L: Local [Is it in my local namespace?]
        - Names assigned in any way within a function and isn't declared globally in that function
2. E: Enclosing function locals
        - Names in the local scope of any and all enclosing functions, from inner to outer
3. G: Global (module)
        - Names assigned at the top-level of a module file, or declared global in a def within the file
4. B: Built-in (Python)
        - Names preassigned in the built-in names module


```python
# Example of a local
# num is local to the below num value

lambda num: num**2
```




    <function __main__.<lambda>(num)>




```python
# Example of an enclosing function locals

# GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    #E NCLOSING
    name = 'Sammy'
    def hello():
        #LOCAL
        name = "I'M A LOCAL"
        print("Hello " + name)
    hello()

greet()

# Beause the variable name isn't defined within the hello function. Python will check for enclosing function locals.
# As you can see, name is defined within the greet function, therefore, it'll use that variable when hello is executed.
# If you commented out name = 'Sammy', the output will be Hello THIS IS A GLOBAL STRING,
#because python will look for a global variable in the python module
```

    Hello I'M A LOCAL



```python
x = 50

def func(x):
    print(f' X is {x}')

    # LOCAL RE-ASSIGNMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')

```


```python
func(x)
```

     X is 50
    I JUST LOCALLY CHANGED X TO 200



```python
print(x)

# the reason why x isn't 200 is because, x = 200 change is only present in the local namespace of the function.
# Globally, the value of x is still 50
# If you did want to change the global value of x, you would define the x as a global variable within the function.
```

    50



```python
# Defining a global variable within a function
# you don't accept x as a parameter
# In Python, parameters are added as local variables within the function's scope.
# One of the rules instructed by the Python IDE is for any given block of code, you can't have variables that are in both local and global namespace
# Since parameters are maintained as local variables, they can't be named as a global variable within the function.
x = 50

def func():
    global x
    print(f' X is {x}')
    # LOCAL RE-ASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f' I JUST LOCALLY CHANGED GLOBAL X TO {x}')
```


```python
print(x)
```

    50



```python
# X value has changed after calling this function, you can see this when you print x's value in the next line of code
func()
```

     X is 50
     I JUST LOCALLY CHANGED GLOBAL X TO NEW VALUE



```python
print(x)
```

    NEW VALUE



```python
# Typically you want to avoid using the global keyword unless it is absolutely necessary
# if you do want to chage a global variable, grab it as a parameter and once you change the value,
# return the re-assignment as an object itself

x = 50

def func(x):
    print(f' X is {x}')
    # LOCAL RE-ASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f' I JUST LOCALLY CHANGED  X TO {x}')
    return x

```


```python
print(x)
```

    50



```python
x = func(x)
```

     X is 50
     I JUST LOCALLY CHANGED  X TO NEW VALUE



```python
print(x)
```

    NEW VALUE



```python

```
