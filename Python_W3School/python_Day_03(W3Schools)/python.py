import myModule

# python Day_03

# Python Classes

# Create a class named MyClass, with a property named x:
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class myClass:
 x=5
 
# Create Object

# Now we can use the class named MyClass to create objects:

obj=myClass()
print("python object/class value",obj.x)

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
 def __init__(self,name,age): 
    self.name=name 
    self.age=age 
    
p1= Person("John",34)    

print("name of the person",p1.name)
print("age of the person",p1.age)

# If the __str__() function is not set, the string representation of the object is returned:

# The string representation of an object WITHOUT the __str__() function:

p2=Person("Robert",45)
print("whole class of a person without \'__str__()\' function",p1)

# The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"name:{self.name} age:{self.age}"

p1 = Person("John", 32)

print("whole class of a person with \'__str__()\' function",p1)

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class: in this example i named self parameter as ref

class Animal:
 def __init__(ref,name,sound):
  ref.name=name      
  ref.sound=sound  
 def __str__(abc):
  return f"Name Of the Animal:{abc.name} Sound of the animal:{abc.sound}"        

new_animal=Animal("Cat","Meow!")
print("name and sound of the animal is:",new_animal)

# we can also add our own function instead of __str__ function:

class Animal:
 def __init__(ref,name,sound):  
  ref.name=name      
  ref.sound=sound  
 def myFunc(abc):
  return f"Name Of the Animal:{abc.name} and sound of the animal:{abc.sound}"  

new_animal=Animal("Cat","Meow!")
print(new_animal.myFunc())
# Modify Object Properties.You can modify properties on objects like this:

print(f"before modifying object {new_animal.myFunc()}")
new_animal.sound="Woof!"
new_animal.name="Dog"
print(f"after  modifying object {new_animal.myFunc()}")

# Delete Object Properties.You can delete properties on objects by using the del keyword:

class Animal:
 def __init__(ref,name,sound):  
  ref.name=name      
  ref.sound=sound  
 def __str__(ref):
  return f"Name Of the Animal:{ref.name} and sound of the animal:{ref.sound}"  
new_animal=Animal("Cat","Meow!")


print(f"before deleting sound properties {new_animal}")
del new_animal.sound
print(f"it is throwing error due to sound propery is deleted")

# Delete Objects
# You can delete objects by using the del keyword:

del new_animal
print("it is throwing error after deleting due to nothing left in object")

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Employee:
 pass   

print("I don't write anything in class I only use pass statement if I don't use pass statement it would raise an error")

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:

# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
 def __init__(self,fName,lName):
  self.fName=fName        
  self.lName=lName        

 def printname(self):
  print(self.fName,self.lName)      
 
x=Person("John","Doe")
x.printname()

# Create a Child Class
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:  
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
 pass

# Now the Student class has the same properties and methods as the Person class.
# Use the Student class to create an object, and then execute the printname method:

y=Student("Robert","Edward")
y.printname()

# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
 
class Student(Person):
 def __init__(self,fname,lname):
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
  Person.__init__(self, fname, lname)

# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent and Add a property called graduationyear to the Student class and then Add a year parameter, and pass the correct year when creating objects and after this Add a method called welcome to the Student class:

class Student(Person):
  def __init__(self, fname, lname,year):
   super().__init__(fname,lname)     
   self.graduationyear=year
  def welcome(self):
   print(f"Welcome to {self.fName} {self.lName} to the class of {self.graduationyear}")       
  
x=Student("John","Doe",2023) 
x.welcome()

# Python Iterators
# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# All these objects have a iter() method which is used to get an iterator:

# Return an iterator from a tuple, and print each value:
# Even strings are iterable objects, and can return an iterator:

fruitTuple=("banana","apple","kiwi")
mystr="hello"
myitr=iter(fruitTuple)
myitrstr=iter(mystr)

print(f"trying 'iter()' function on tuple {next(myitr)}")
print(f"trying 'iter()' function on tuple {next(myitr)}")
print(f"trying 'iter()' function on tuple {next(myitr)}")
print(f"trying 'iter()' function on string {next(myitrstr)}")
print(f"trying 'iter()' function on string {next(myitrstr)}")
print(f"trying 'iter()' function on string {next(myitrstr)}")
print(f"trying 'iter()' function on string {next(myitrstr)}")
print(f"trying 'iter()' function on string {next(myitrstr)}")

# We can also use a for loop to iterate through an iterable object
# Iterate the values of a tuple 

for x in fruitTuple:
 print("each item in fruit tuple",x)   

# Iterate the characters of a string:

for x in mystr:
 print("each character in string",x)   

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
   if self.a <= 20:
      x = self.a
      self.a += 1
      return x
   else:
      raise StopIteration

new_number=MyNumbers()   
myiter=iter(new_number)
for x in myiter:
 print("x print only 20 time",x)   

# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
  
  
# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?
# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:  
 
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

  
  
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print("all inherited vehicle brand",x.brand)
  print("all inherited vehicle model",x.model)
  x.move()
  
# local scope Example

def myFunc():
  x=300
  return print("here x is the local scoped variable and both has name x but both values are differ from each other",x)  
myFunc()

# global scope example

x=500
print("here x is the global scoped variable and both has name x but both values are differ from each other",x)

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

# If you use the global keyword, the variable belongs to the global scope,Also, use the global keyword if you want to make a change to a global variable inside a function.

def myfunc():
  global x
  x=300
  return x 
  
print("this is x in function but this x is global scoped because it has global keyword",myfunc())
print("x is printed",x)

# Python Modules

# importing a module function

myModule.greeting("Ahmad")

# importing a module variables

print(f"person details: {myModule.person1}")

# imported object value

name=myModule.person1["name"]
age=myModule.person1["age"]
country=myModule.person1["country"]

print(f" person name is {name} and his age is {age} and he lives in {country} (getted without re-naming module)")

# ranaming module

import myModule as mx

name=mx.person1["name"]
age=mx.person1["age"]
country=mx.person1["country"]

print(f"person name is {name} and his age is {age} and he lives in {country} (getted with re-naming module)")

# Import and use the platform module which is built in:

import platform

x = platform.system()
print("using built in module 'platform'",x)

# List all the defined names belonging to the platform module using "dir()" function.
# Note: The dir() function can be used on all modules, also the ones you create yourself.



y = dir(platform)
print("whole list of platform exports",y)

# Import only the person1 dictionary from the module.
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

from myModule import person1

print ("person age is ",person1["age"])

# Import the datetime module and display the current date:

import datetime

dateNow=datetime.datetime.now()
print("date time now",dateNow)

# Full Date

print(f"full date {dateNow.date()} {dateNow.hour}:{dateNow.minute}:{dateNow.second}")

# creating date objects
# The datetime() class requires three parameters to create a date: year, month, day.
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

x = datetime.datetime(2020, 5, 17)
print("our own date object",x)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# Display the name of the month:

month = datetime.datetime(2018, 6, 1)

print("this will give the name of month of date we give us to it as parameter",month.strftime("%B")) 

# Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

miin=(8,2,4,4,2,20)
maax=(8,2,4,4,2,20)

print(f"min number in this tuple {miin} and this is the smallest number from that tuple {min(miin)}")
print(f"max number in this tuple {maax} and this is the smallest number from that tuple {max(maax)}")

# The abs() function returns the absolute (positive) value of the specified number:

x=-2.93
print(f"the abs value of {x} is {abs(x)}")

# The pow(x, y) function returns the value of x to the power of y (xy).

n=2
e=3
print(f"the ans of number {n} raise to the power of number {e} is {pow(n,e)}")

#importing math

import math

# The math.sqrt() method for example, returns the square root of a number:

sqroot=9
print(f"the square root of {sqroot} is {math.sqrt(sqroot)}")

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

num=58.8

# math.ciel

print(f"after applying math.ceil method on {num} it becomes {math.ceil(num)}")

# math.floor

print(f"after applying math.floor method on {num} it becomes {math.floor(num)}")

# The math.pi constant, returns the value of PI (3.14...):

piValue=math.pi

print(f"the piValue is {piValue}, it become pi value using math.pi")

# JSON

# importing json

import json

# Convert from JSON to Python:

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("this is a python format person detail",y)

# Convert from Python to JSON:

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("this is a json format person detail",y)

# Convert Python objects into JSON strings, and print the values:

print("converting python set type into json",json.dumps({"name": "John", "age": 30}))
print("converting python lsit type into json",json.dumps(["apple", "bananas"]))
print("converting python tuple type into json",json.dumps(("apple", "bananas")))
print("converting python string type into json",json.dumps("hello"))
print("converting python int type into json",json.dumps(42))
print("converting python float type into json",json.dumps(31.76))
print("converting python boolean(true) type into json",json.dumps(True))
print("converting python boolean(false) type into json",json.dumps(False))
print("converting python None type into json",json.dumps(None))

# Convert a Python object containing all the legal data types:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print("Convert a Python object containing all the legal data types:",json.dumps(x))

# Use the indent parameter to define the numbers of indents, seperators parameter to define seperators and sort_keys parameter to sort the keys:

print("Convert a Python object containing all the legal data types with indent parameter:",json.dumps(x,indent=4,separators=(". ", " = "),sort_keys=True ))

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:

import re

# Search the string to see if it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


# The findall() Function
# The findall() function returns a list containing all matches.The list contains the matches in the order they are found.If no matches are found, an empty list is returned:

# Print a list of all matches:

x=re.findall("ai",txt)

print(f"{len(x)} times the word 'ai' comes ")

# Return an empty list if no match was found:

x=re.findall("portugalnhdiihdhhuqhhrwuhi",txt)

print(f"{len(x)} times the word 'portugalnhdiihdhhuqhhrwuhi' comes ")

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:

# Search for the first white-space character in the string:

x=re.search("\s",txt)

print("The first white-space character is located in position:", x.start()) 

# If no matches are found, the value None is returned:

# Make a search that returns no match:

x = re.search("Portugaleehyeh", txt)
print(f"the word is {x} in this Portugaleehyeh")

# The split() Function
# The split() function returns a list where the string has been split at each match,You can control the number of occurrences by specifying the maxsplit parameter:

# Split at each white-space character:

x = re.split("\s", txt)
print(f"without spliting at space it is like '{txt}' after spliting it become '{x}'")

# Split the string only at the first occurrence:

x = re.split("\s", txt, 1)
print(f"without spliting at first space it is like '{txt}' after spliting it become '{x}'")

# The sub() Function
# The sub() function replaces the matches with the text of your choice.You can control the number of replacements by specifying the count parameter:

# Replace every white-space character with the number 9:

x = re.sub("\s", "v", txt,2)
print(f"it replace first 2 white space in the sentence {txt} with v and the result is {x}")

# Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.

# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S":

x = re.search(r"\bS\w+", txt)
print("span tells that which index the word or char occur in sentence",x.span())

# Print the string passed into the function:

x = re.search(r"\bS\w+", txt)
print("The string property returns the search string:",x.string)

# Print the part of the string where there was a match.

# The regular expression looks for any words that starts with an upper case "S":
# Note: If there is no match, the value None will be returned, instead of the Match Object.

x = re.search(r"\bS\w+", txt)
print(" group property Search for an upper case 'S' character in the beginning of a word, and print the word:",x.group())

# The exceptions(error) can be handled using the try statement:
# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:

number1=94
try:
    print("number in try statement",number1)

except:
      print("An exception occurred")

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error: 

# Print one message if the try block raises a NameError and another for other errors:

try:
  print("number in try statement with two exceptions",number1)
except NameError:
  print("Variable number1 is not defined")
except:
  print("Something else went wrong")
  
# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:  

try:
  print("number with else statement",number1)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print("number with finally statement",number1)
except:
  print("Something went wrong")
finally:
  print("finally always execute")  
  
# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
# Raise an error and stop the program if x is lower than 0:

x=2

if x>0:
  print("x is greater than 0")
else:
   raise Exception("Sorry,number is below than zero")    
 
# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.    

num=2

if not type(num) is int:
  raise TypeError("Only integers are allowed")

# The following example asks for the username, and when you entered the username, it gets printed on the screen:
# Python 3.6

username = input("Enter username:")
print("Username is: " + username)

# To make sure a string will display as expected, we can format the result with the format() method.

# Add a placeholder where you want to display the price:

price = 49
text = "The price is {} dollars"
print("this is an example of 'format()' method",text.format(price))

# Format the price to be displayed as a number with two decimals:

text = "The price is {:.2f} dollars"
print("this is an example of 'format()' method with specifying how to convert the value:",text.format(price))

# Multiple Values
# If you want to use more values, just add more values to the format() method:

quantity=3
itemNo=345
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print("this is an example of 'format()' method with specifying how to convert the value with multiple values:",myorder.format(quantity,itemNo,price,))

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders,Also, if you want to refer to the same value more than once, use the index number:

myorder = "I want {0} pieces of item number {2} for {1:.2f} dollars.Remind it I want {0} pieces"
print("this is an example of 'format()' method with specifying how to convert the value with multiple values(while giving index):",myorder.format(quantity,price,itemNo))

# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

myCar = "Make:{carname}, Model:{model}."
print("my car details",myCar.format(carname = "Ford", model = "Mustang"))

# Sort the list based on how close the number is to 50:

def close50(n):
  return abs(n - 50)
thislist=[2,5,7,8,200,52] 
thislist.sort(key=close50)
print("Example of customize sort",thislist)
