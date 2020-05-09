# Lambda Expressions, Map, and Filter

# Following Instructor


```python
def square(num):
    return num ** 2
```


```python
my_nums = [1,2,3,4,5]
```


```python
map(square, my_nums)
```




    <map at 0x1084c4410>




```python
for item in map(square, my_nums):
    print(item)
```

    1
    4
    9
    16
    25



```python
list(map(square,my_nums))
```




    [1, 4, 9, 16, 25]




```python
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
```


```python
names = ['Pravin', 'Selvarajah', 'lesant', 'roosan','eve']
```


```python
list(map(splicer,names))
```




    ['EVEN', 'EVEN', 'EVEN', 'EVEN', 'e']




```python
def check_even(num):
    return num%2 == 0
```


```python
mynums = [1,2,3,4,5,6]
```


```python
filter(check_even,mynums)
```




    <filter at 0x1084c8f50>




```python
for n in filter(check_even,mynums):
    print(n)
```

    2
    4
    6



```python
def square(num):
    result = num ** 2
    return result
```


```python
square(2)
```




    4



## Now we will slowly turn the square function into a Lambda Function


```python
square = lambda num: num ** 2
```




    <function __main__.<lambda>(num)>




```python
square(5)
```




    25




```python
### lambda function preforms the same operation as the previously defined square function. It then applies to function to mynums
### returns a list of numbers using the list function

list(map(lambda num: num ** 2, mynums))
```




    [1, 4, 9, 16, 25, 36]




```python
### We will replace the check_even with a lambda function
### def check_even(num):
###    return num % 2 == 0

# results will be applied to mynums and then filtered into a list format.
list(filter(lambda num: num%2 == 0, mynums))

```




    [2, 4, 6]




```python
names
```




    ['Pravin', 'Selvarajah', 'lesant', 'roosan', 'eve']




```python
list(map(lambda name: name[0], names))
```




    ['P', 'S', 'l', 'r', 'e']




```python
### Lambda functions should be only used if it is still easily readable when you come back to review your code
```


```python

```
