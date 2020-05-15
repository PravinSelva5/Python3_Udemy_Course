```python
def add(n1,n2):
    print(n1+n2)
```


```python
add(10,20)
```

    30



```python
number1 = 10
```


```python
number2 = input('Please provide a number: ')
```

    Please provide a number: 14


This command will result in the below error because number2 is a string in this case and the function 'add' isn't designed to accomodate that yet

add(number1,number2)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-aae8f329fc42> in <module>
----> 1 add(number1,number2)

<ipython-input-1-48bddae7e371> in add(n1, n2)
     
    1 def add(n1,n2):
    
----> 2     print(n1+n2)

TypeError: unsupported operand type(s) for +: 'int' and 'str'
 ---------------------------------------------------------------------------


```python
try: 
    # WANT TO ATTEMPT THIS CODE 
    # MAY HAVE AN ERROR
    result = 10 + 10

except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well")
    print(result)
```

    Add went well
    20



```python
result
```




    20



## New Example


```python
try: 
    f = open('testfile','w')
    f.write('Write a test line')
except TypeError:
    print("There was a type error!")
except OSError:
    print('Hey you have an OS error!')
except:
    print("All other exceptions!")
finally:
    print("finally, block of code wil always run")
```

    finally, block of code wil always run



```python
def ask_for_int():
    try:
        result = int(input('Please provide number: '))
    except:
        print('Whoops! This is not a number')
    finally:
        print("End of try/except/finally")
```


```python
ask_for_int()
```

    Please provide number: 12
    End of try/except/finally



```python
ask_for_int()
```

    Please provide number: 14
    End of try/except/finally



```python
def ask_for_int():
    while True:
        try:
            result = int(input('Please provide a number:\n'))
        except:
            print('Whoops! This is not a number')
            continue
        else:
            print("Yes thank you for the number")
            break
        finally:
            print("End of try/except/finally")
```


```python
ask_for_int()
```

    Please provide a number:
    raptors
    Whoops! This is not a number
    End of try/except/finally
    Please provide a number:
    14
    Yes thank you for the number
    End of try/except/finally



```python

```


```python

```
