# Following Instructor: Object Oriented Programming


```python
# Rmr for defining classes, we use camelcasing. 
# With Camel Case, the first letter of the first word in the identifier is lower case, 
# and all subsequent words use proper case, thus firstName:='Ozz';

class Dog():
    # By defining attriubtes above your __init__ function, you create a CLASS OBJECT ATTRIBUTE
    # These are the SAME for ANY INSTANCE of a CLASS
    
    species = 'mammal'
    
    # when def is used inside a class, it is referred to as a method
    # self, keyword represents the instance of the object itself
    
    def __init__(self, breed, name):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        
    # OPERATIONS/Actions ---> Methods
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))
        
```


```python
my_dog = Dog('Lab', "Sammy")
```


```python
type(my_dog)
```




    __main__.Dog



You can see above, that my_dog is an instance of the Dog class


```python
my_dog.name
```




    'Sammy'




```python
my_dog.bark(5)
```

    WOOF! My name is Sammy and the number is 5


When calling an attribute, you dont need to use "()", because the attribute is a characteristic of the class and you aren't trying to execute any function. For methods, the PARENTHESIS needs to be used for the OPERATION TO BE EXECUTED.


```python
my_dog.bark(5)
```

    WOOF! My name is Sammy and the number is 5



```python

```


```python

```


```python

```


```python
class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi  # self.pi could also be written as " Circle.pi ", this type of naming is only possible for CLASS OBJECT attributes
        
    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
```


```python
my_circle = Circle(30)
```


```python
my_circle.pi
```




    3.14




```python
my_circle.get_circumference()
```




    188.4




```python
my_circle.radius
```




    30




```python
my_circle.area
```




    2826.0



## Inheritance

- From a high level, Inheritance is a way of making a new class using classes that have already been defined
- This helps reduce the complexity of a program


```python
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(animal):
        print("I am eating")
```


```python
myanimal = Animal()
```

    ANIMAL CREATED



```python
myanimal.eat()
```

    I am eating


- Animal class will be used as the base class for the Dog class 
    - Because of this, the Dog class is a derived class
    -  You can reuse the methods that are found in the Animal Class


```python
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    #To overide one of the older methods
    # Write the method with the same name as the older method
    
    def who_am_i(self):
        print("I am a dog")
    
```


```python
mydog = Dog()
```

    ANIMAL CREATED
    Dog created



```python
mydog.who_am_i()
```

    I am a dog


## Polymorphism

- Methods belong to the object they act on
- If you look at the two classes below, each of them have the SPEAK METHOD
    - Each object's speak method is unique to the object (meow vs woof)
- Essentially, the same blocks of code however, each block of code can take in a slightly different type of argument, variable, or input


```python
class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"
```


```python
class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"
```


```python
niko = Dog("Niko")
felix = Cat("Felix")
```


```python
print(niko.speak())
```

    Niko says woof!



```python
print(felix.speak())
```

    Felix says meow!



```python
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())
```

    <class '__main__.Dog'>
    Niko says woof!
    <class '__main__.Cat'>
    Felix says meow!



```python
def pet_speak(pet):
    print(pet.speak())
```


```python
pet_speak(niko)
```

    Niko says woof!



```python
pet_speak(felix)
```

    Felix says meow!



```python
# You can also create an Abstract Class that is used as the base class and never insantiated

class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')
```

myanimal = Animal('fred')

If you execute the above code, you'll get the following error. It's expecting you to inherit the Animal class and over write the speak method

myanimal.speak()

![image.png](attachment:image.png)


```python
class Dog(Animal):
    
    def speak(self):
        return self.name + " says woof!"
    
```


```python
class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow!"
```


```python
fido = Dog("Fido")
```


```python
sarah = Cat("Sarah")
```


```python
print(fido.speak())
```

    Fido says woof!



```python
print(sarah.speak())
```

    Sarah says meow!


A real-world example would be, opening files. There are many different kinds of files. You would essentially have a base class for opening files. And then create derived classes that would open different types of files
