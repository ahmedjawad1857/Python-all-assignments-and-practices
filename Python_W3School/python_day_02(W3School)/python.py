# You can loop through the list items by using a for loop:

thislist=["apple","mango","banana","cherry"]

for x in thislist:
 print("each item", x)
 
# You can loop through the list items by using a for loop with index:

for i in range(len(thislist)):
 print("thislist each item with an index",thislist[i])
 
# You can loop through the list items by using a while loop.

i=0
while i<len(thislist):
 print("thislsit each item using index with while loop",thislist[i]) 
 i+=1
 
# A short hand for loop that will print all items in a list:

[print("each item with shorthand for loop",x) for x in thislist ]

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.Without list comprehension you will have to write a for statement with a conditional test inside.

fruits=["apple","banana","kiwi","mango"]
fruitsContainA=[]
for x in fruits:
 if "a" in x:
  fruitsContainA.append(x)
print("list containg letter \'a\' in their name withOut list comprehension ",fruitsContainA)
       
# With list comprehension you can do all that with only one line of code:
 
fruitsContainA= [x for x in fruits if "a" in x]
print("list containg letter \'a\' in their name with list comprehension ",fruitsContainA)

# You can use the range() function to create an iterable:

newlist=[x for x in range(10)]
print("iterable with range 10",newlist)

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

fruitList=["apple","kiwi","banana","mango"]
print("list without sorted it",fruitList)
fruitList.sort()
print("sorted list",fruitList)

# To sort descending, use the keyword argument reverse = True:

print('original list ',fruitList)
fruitList.sort(reverse=True)
print("list sorted descendingly",fruitList)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

fruitList=["apple","Kiwi","banana","mango"]
print("original list",fruitList)
fruitList.sort()
print("case sensitive sort",fruitList)

# So if you want a case-insensitive sort function, use str.lower as a key function:

print("Original list",fruitList)
fruitList.sort(key=str.lower)
print("case insensitive sort",fruitList)

# The reverse() method reverses the current sorting order of the elements.

print("Original list",fruitList)
fruitList.reverse()
print("after reversing list",fruitList)

# There are ways to make a copy, one way is to use the built-in List method copy().

thislist = ["apple", "banana", "mango","cherry"]
mylist = thislist.copy()
print("copied list with \'copy()\' method",mylist)

# Another way to make a copy is to use the built-in method list().

mylist=list(thislist)
print("copied list with \'list()\' method",mylist)

# One of the easiest ways are by using the + operator.

list1=["a","b","c","d"]
list2=[1,2,3,4]
list3=list1+list2
print("joined list using \'+\' operator",list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

for x in list2:
 list1.append(x)
print("joined list with \'append method and for loop method\'",list1)    

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

list1=["a","b","c","d"]
list2.extend(list1)
print("joined list with \'extend()\' method",list2)

# tuples

# You can access tuple items by referring to the index number, inside square brackets. In negative indexes -1 refers to the last item, -2 refers to the second last item etc.

thistuple = ("apple", "banana", "cherry")
print("the second value of the tuple is",thistuple[1])
print("the last value of the tuple is",thistuple[-1])

# When specifying a range, the return value will be a new tuple with the specified items.By leaving out the start value, the range will start at the first item and by leaving out the end value, the range will go on to the end of the tuple:

print("the tuple items of range 0:2(not included)",thistuple[0:2])

# Specify negative indexes if you want to start the search from the end of the tuple:

print("the tuple items of negative range -3:-1(not included)",thistuple[-3:-1])

# To determine if a specified item is present in a tuple use the in keyword:

if "apple" in thistuple:
  print("Yes, 'apple' is in the thistuple tuple")
else:
 print("No, \'apple\' is in the thistuple tuple")     
 
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple. 
print("original tuple",thistuple)
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)

print("after changing it's values",thistuple)

# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
print("original tuple",thistuple)
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("after adding a value by \'convert into a list then append a value and the convert it into a tuple\' method",thistuple)

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

print("original tuple",thistuple)
y = ("mango",)
thistuple += y

print("after adding value by \'add a tuple to tuple\' method",thistuple)

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items Or you can delete the tuple completely:

print("original tuple",thistuple)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print("thistuple after removing \'apple\'",thistuple)

del thistuple
print("there is nothing in tuple we delete even not the round bracket it completely delete it")

# we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(apple, banana, cherry) = fruits

print("this should print the value at 0 index",apple)
print("this should print the value at 1 index",banana)
print("this should print the value at 2 index",cherry)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list.If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.



(apple, *banana, ) = fruits

print("this should print the value at 0 index",apple)
print("this should print the remaining values",banana)

# You can loop through the tuple items by using a for loop.

for x in fruits:
 print("each item of fruits",x)   
 
# You can also loop through the tuple items by referring to their index number.Use the range() and len() functions to create a suitable iterable. 

for i in range(len(fruits)):
 print("each item in fruits using index",fruits[i])   
 
 # You can loop through the tuple items by using a while loop.Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
 
 i=0
while i<len(fruits):
 print("each item in fruits using while loop",fruits[i])    
 i+=1
 
 # To join two or more tuples you can use the + operator:

tuple1=("a","b","c","d")
tuple2=("e","f","g","h")
tuple3=tuple1+tuple2
print("joined tuples",tuple3)

# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

fruits=("apple","banana","mango","orange")
newTuple=fruits*3
print("fruits tuple after multiplying by 3",newTuple)

# Set
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Sets cannot have two items with the same value.But no any error come it will ignore Duplicate values.
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates.
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates.
# Once a set is created, you cannot change its items, but you can add new items.
# Note: If the item to remove does not exist, remove() will raise an error.
# Note: If the item to remove does not exist, discard() will NOT raise an error.
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# Note: Both union() and update() will exclude any duplicate items.

fruitsSet={"apple","banana","mango"}

# It is also possible to use the set() constructor to make a set.

fruitsSet=(("apple","banana","mango"))

# You cannot access items in a set by referring to an index or a key.But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Loop through the set, and print the values:

fruitsSet={"apple","banana","mango"}
for x in fruitsSet:
 print("accessing each item in fruits Set using loop", x)   
 
# Check if "banana" is present in the set:

if "banana" in fruitsSet:
 print("Yes, banana is present in fruits set ")   
else:
 print("No, banana is not present in fruits set")    
 
# To add one item to a set use the add() method.

print("Original set",fruitsSet)
fruitsSet.add("orange")
print("after adding a value in the set",fruitsSet)

# To add items from another set into the current set, use the update() method.

print("Original set",fruitsSet)
fruits2Set={"kiwi","cherry"}
fruitsSet.update(fruits2Set)
print("after extending a set with another set",fruitsSet)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

print("original set",fruitsSet)
fruits2=["papaya","melon","waterMelon"]
fruitsSet.update(fruits2)
print("after extending a set with list",fruitsSet)

# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:

print("Original set",fruitsSet)
fruitsSet.remove("banana")
print("set after removing \'banana\'",fruitsSet)

# Remove "kiwi" by using the discard() method:

print("Original set",fruitsSet)
fruitsSet.discard("kiwi")
print("set after removing \'kiwi\'",fruitsSet)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.The return value of the pop() method is the removed item.

print("Original set",fruitsSet)
fruitsSet.pop()
print("set after removing \'random\' value",fruitsSet)

# The clear() method empties the set:

print("Original set",fruitsSet)
fruitsSet.clear()
print("set after clearing values",fruitsSet)

# The del keyword will delete the set completely:

fruitsSet={"mango","banana","apple"}
print("Original set",fruitsSet)
del fruitsSet
print("there is nothing in set  del method delete all things even  the curly  bracket ")

# You can loop through the set items by using a for loop:

fruitsSet={"mango","banana","apple"}
for x in fruitsSet:
 print("each item in fruits set using for loop",x)
 
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
# The union() method returns a new set with all items from both sets:

set1={1,2,3,4,5,6,7}
set2={8,9,10,1,2,3,4}
set3 = set1.union(set2)
print("joining two sets using \'union method\'",set3)
 
# The update() method inserts the items in set2 into set1:

set1.update(set2) 
print("we extend a set with another",set1)

# The intersection_update() method will keep only the items that are present in both sets.The intersection() method will return a new set, that only contains the items that are present in both sets.

set1={1,2,3,4,5,6,7}
set2={8,9,10,1,2,3,4}
set3=set1.intersection(set2)
set1.intersection_update(set2)
print("we are doing intersectione of one set to another which keep only the items which exist in both sets",set3)
print("we are doing intersection_update of one set to another which keep only the items which exist in both sets and joined the both sets",set1)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

set1={1,2,3,4,5,6,7}
set2={8,9,10,1,2,3,4}
set3=set1.symmetric_difference(set2)
set1.symmetric_difference_update(set2)
print("we are doing symmetric_difference of one set to another which keep only the items which not exist in both sets",set3)
print("we are doing symmetric_difference_update() of one set to another which keep only the items which not exist in both sets and joined the both sets",set1)

# Python Dictionaries
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

cardict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# It is also possible to use the dict() constructor to make a dictionary.

cardict=dict( brand= "Ford",
  model= "Mustang",
  year= 1964)

# You can access the items of a dictionary by referring to its key name, inside square brackets.There is also a method called get() that will give you the same result:

cardict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("accessing a brand key in cardict dictionary using \'squareBrackets\' methods",cardict["brand"])
print("accessing a brand key in cardict dictionary using \'get()\' methods",cardict.get("brand"))

# The keys() method will return a list of all the keys in the dictionary.

print("keys of cardict are as follows before changing it:",cardict.keys())

# Add a new item to the original dictionary, and see that the keys list gets updated as well:

cardict["color"]="white"
print("keys of cardict are as follows after changing it:",cardict.keys())

# The values() method will return a list of all the values in the dictionary.
cardict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("values of cardict are as follows before changing it:",cardict.values())

# Add a new item to the original dictionary, and see that the values list gets updated as well:

cardict["color"]="white"
print("values of cardict are as follows after changing it:",cardict.values())

# The items() method will return each item in a dictionary, as tuples in a list.

cardict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("items of cardict are as follows before changing it:",cardict.items())

# Make a change in the original dictionary, and see that the items list gets updated as well:

cardict["color"]="white"
print("items of cardict are as follows after changing it:",cardict.items())

# To determine if a specified key is present in a dictionary use the in keyword:

if "model" in cardict:
  print("Yes, 'model' is one of the keys in the cardict dictionary")
else:
   print("No, 'model' is not one of the keys in the cardict dictionary")     
   
# You can change the value of a specific item by referring to its key name:

print("before changing the value of year in cardict",cardict) 
cardict["year"]=2009  
print("after changing the value of year in cardict",cardict) 

# The update() method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with key:value pairs.

print("before changing the value of year in cardict",cardict) 
cardict.update({"color":"black"})
print("after changing the value of year in cardict",cardict) 

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

print("before adding the mileage item in cardict",cardict) 
cardict['mileage']= 25000
print("after adding the new item in cardict",cardict) 

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.The argument must be a dictionary, or an iterable object with key:value pairs.

print("before adding the new item in cardict using \'update\' mehtod",cardict) 
cardict.update({"fuel-type":"petrol"})
print("after adding the new item in cardict using \'update\' mehtod",cardict) 

# The pop() method removes the item with the specified key name:

print("before deleting item having key:fuel-type in cardict using \'pop\'",cardict)
cardict.pop("fuel-type")
print("after deleting item having key:fuel-type in cardict using \'pop\'",cardict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

print("before deleting last inserted item in cardict using \'popitem\'",cardict)
cardict.popitem()
print("after deleting last inserted item in cardict using \'popitem\'",cardict)

# The del keyword removes the item with the specified key name:

print("before deleting item having key:color in cardict using \'del\' method",cardict)
del cardict["color"]
print("after deleting item having key:color in cardict using \'del\' method",cardict)

# The del keyword can also delete the dictionary completely:

print("before deleting cardict using \'del\' method",cardict)
del cardict
print("there is nothing in dictionary del method delete all things even the curly bracket")

# You can loop through a dictionary by using a for loop.When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one.You can use the keys() method to return the keys of a dictionary:

cardict = {
    'make': 'Toyota',
    'model': 'Camry',
    'year': 2020,
    'color': 'Blue'}


for x in cardict:
 print("all the keys of cardict are as follows using for loop:",x)   
 
for x in cardict.keys():
 print("all the keys of cardict are as follows using for loop, keys():",x)   

# Print all values in the dictionary, one by one.You can also use the values() method to return values of a dictionary:

for x in cardict:
 print("all the values of cardict are as follows using for loop:",cardict[x])   

for x in cardict.values():
 print("all the values of cardict are as follows using for loop,values():",x)   

# Loop through both keys and values, by using the items() method:

for x in cardict.items():
 print("all the items of cardict are as follows using for loop,items():",x)   

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

cardict1=cardict.copy()
print("copying cardict in cardict1 using \'copy()\' method",cardict1)

# Another way to make a copy is to use the built-in function dict().

cardict1=dict(cardict)
print("copying cardict in cardict1 using \'dict()\' method",cardict1)

# A dictionary can contain dictionaries, this is called nested dictionaries.

# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "birthYear" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "birthYear" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "birthYear" : 2011
  }
}
print("a dictionary having three nested dictionaries",myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print("three dictionaries in one dictionary",myfamily)

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

print("accessing the name of the child2(nested dictionary) name ",myfamily["child2"]["name"])

# An "if statement" is written by using the if keyword.

a = 33
b = 200
if b > a:
  print("b is greater than a")

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".


if b < a:
  print("b is smaller than a")
elif a < b:
  print("a is smaller than b")

# The else keyword catches anything which isn't caught by the preceding conditions.
a=33
b=33
if b < a:
  print("b is smaller than a")
elif a < b:
  print("a is smaller than b")
else:
 print("a and b are equal")   
 
 # If you have only one statement to execute, you can put it on the same line as the if statement.

a=100
b=33
if a > b: print("a is greater than b")

# One line if else statement, with 3 conditions the first else and second if refer to elif

a=2
b=33
print("A is greater than B") if a>b else print("B is equal to A") if a==b else print("B is greater than A")

# another example of shorthand if else with three conditions

print("number is zero(0)") if a==0 else print("number is even") if a%2==0 else print("number is odd")

# The and keyword is a logical operator, and is used to combine conditional statements:

a=2 
b=3
c=4
if a>b and a>c:
 print("a is the largest number ")
elif b>a and b>c:
 print("b is the largest number ")
elif c>a and c>b:
 print("c is the largest number ")
else:
 print("they are equal ")
   
# The or keyword is a logical operator, and is used to combine conditional statements:
if a>b or a>c:
 print("a is the greater than b or c ")
elif b>a or b>c:
 print("b is the greater than a or c ")
elif c>a or c>b:
 print("c is the greater than a or b ")
else:
 print("they are equal ")
   
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

if b > a:
  pass

# You can have if statements inside if statements, this is called nested if statements.

# userInput=int(input("Enter Your Age..."))
userInput=20
if userInput>=18:
 print("you are eligible to vote.")
 if userInput>=23:
  if userInput>=23:
   print("You are also eligible to stand for election.")   
  else:
   print("you can vote,but you are not eligible to stand for election.")    
else:
  print("you are not eligible to vote.")   
  
# python loops

# while loop
# Note: remember to increment i, or else the loop will continue forever.

# With the while loop we can execute a set of statements as long as a condition is true.

# Print i as long as i is less than 6:

i=1
while 6>=i:
 print("i is print 6 times ",i)   
 i+=1
 
# With the break statement we can stop the loop even if the while condition is true:
i=1
while 6>=i:
 print("i is print 3 times due to break",i) 
 if i==3:break  
 i+=1
 
# With the continue statement we can stop the current iteration, and continue with the next:

i = 1
while i <= 6:
  i += 1
  if i == 3:
     continue
  print("i is print 2-7 due to continue statement",i)
 
# With the else statement we can run a block of code once when the condition no longer is true:
i=1
while i <= 6:
  print("trying else with while loop",i)
  i += 1
else:
 print("i is no lorger smaller or equal to 6")  
 
# for loop
# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Print each fruit in a fruit list:

fruit=["apple","kiwi","banana","cherry"]
for x in fruit:
 print("each item in fruit list",x)
 
# Even strings are iterable objects, they contain a sequence of characters:

# Loop through the letters in the word "banana":

for x in "banana":
 print("each character in banana",x) 
 
# With the break statement we can stop the loop before it has looped through all the items:

for x in fruit: 
 print("each item in fruits before banana comes, it is the last due to break statement",x)  
 if x=="banana":break
 
# Exit the loop when x is "kiwi", but this time the break comes before the print:

for x in fruit:   
 if x=='kiwi':
  break 
 print("each item in fruits before banana comes, the item before banana is last due to break statement ",x)     
 
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

for x in fruit:   
 if x=='banana':
  continue 
 print("it skip banana due to continue statement",x)
 
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print("printing range from 0-6(not included)",x)
else:
  print("Finally finished!")
 
# Print each adjective for every fruit using nested loop.

adj=["big","tasty"]
for x in adj:
 for y in fruit:   
  print("the fruit is",x,y)
  
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in "hello": 
 pass    

# Python Functions

# In Python a function is defined using the def keyword:

def my_function():
  print("hello python functions")
 
# To call a function, use the function name followed by parenthesis like this,

my_function()  

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
 
def printFname(fname):
 print(fname+" "+"doe" )    

printFname("John") 
printFname("Robert") 
printFname("Kevin") 

# This function expects 2 arguments, and gets 2 arguments,If you try to call the function with 1 or 3 arguments, you will get an error:


def printFullName(fName,lName):
 print(fName+" "+lName)

printFullName("John","Doe")
printFullName("Robert","Ben")
printFullName("Kevin","harry")

# If the number of arguments is unknown, add a * before the parameter name:

def functionExample(*kids):
 print("youngest child is",kids[2])   
 
functionExample("Emil", "Tobias", "Linus") 
  
# You can also send arguments with the key = value syntax.This way the order of the arguments does not matter.  

def keyPairFunc(child3,child1,child2):
 print("the youngest child is",child3)     
 
keyPairFunc(child1="Emil",child3="Tobias",child2="Linus") 

# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def unKnownParamKey(**kid):
 print("his first name is", kid["fname"])   
 
unKnownParamKey(fname="John",lname="Doe")

# The following example shows how to use a default parameter value.If we call the function without argument, it uses the default value:

def countryPrint(country="Pakistan"):
 print("I am from "+country)   
 
countryPrint("Sweden") 
countryPrint("Norway") 
countryPrint("India") 
countryPrint()

# list as an argument

def listArg(fruits):
 for x in fruits:
  print("each item of fruits",x)      
  
fruit=["apple","banana","kiwi"]  
listArg(fruit)
  
# To let a function return a value, use the return statement:

def returnFunc(x): 
 return 5*x

print("retun func with value 3",returnFunc(3))
print("retun func with value 6",returnFunc(6))
print("retun func with value 2",returnFunc(2))

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def passFunc():
  pass

# Recursion Example

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("result of recursion",result)

# Add 10 to argument a, and return the result:

x=lambda a:a+10
print("lambda example",x(4))

# Lambda functions can take any number of arguments:

y=lambda a,b:a**b
print("lambda example where \'a\' raise to the power \'b\'",y(3,2))

def lambdaInFunc(n):
 return lambda a:a-n   
mydoubler=lambdaInFunc(2)
print("lambda in function example",mydoubler(11))