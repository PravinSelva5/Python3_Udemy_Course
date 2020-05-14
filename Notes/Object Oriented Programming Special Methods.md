```python
mylist = [1,2,3]
```


```python
len(mylist)
```




    3




```python
class Sample():
    pass
```


```python
mysample = Sample()
```


```python
print(mysample)
```

    <__main__.Sample object at 0x10662a890>


## How do you use python standard functions on user defined objects?


```python
class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f" {self.title} by {self.author} "
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")
```


```python
b = Book('Python Rocks!', 'Jose', 200)
```


```python
print(b)
```

     Python Rocks! by Jose 


### The print function asks, "what is the string representation of the parameter?"
- Instead, you can use the special method related to the string call ( __str__)
    -  What does this do?
        - If there is a method that asks for the string representation of the class. Whatever the function in __str__ returns, is what the output will be
        - Which is what you see with "Python Rocks! by Jose" rather than the name of the memory the object is located at:
            - Example:  <__main__.Book object at 0x106594790>


```python
len(b)
```




    200




```python
# To delete variables from your computer, you can use the key word del(variable_name)
del(b)
```

    A book object has been deleted



```python

```
