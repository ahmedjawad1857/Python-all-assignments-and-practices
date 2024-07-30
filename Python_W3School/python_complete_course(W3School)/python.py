# Python Day_01 Start

from typing import Final
import random


print('hello world')

X:Final[dict]={
    "hello":20,
    'blue':"hello world"
    
}

print("X",X)
# print("y",y)
print("X type",type(X))
# print("y type",type(y))


x = 1    
y = 2.8  
z = 1j  

a = float(x)

b = int(y)

c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



print("random number ",random.randint(9,99))
#multiline string
a="""  lorem i
pu
uh  """
#for accessing any character of string we use variable[index]
print("first character of a",a[-1])


# for loop


for char in a:
 print('char',char)
    
    
# string length
 print('length of a',len(a))    
 
 


print("loremg"in a)


# in with if else statement
if 'lorem' in a:
 print('yes it has lorem')
else:   
 print('no it not has lorem')  
 
 # To check if a certain phrase or character is not present in a string, we can use the keyword not in.

print("lorem" not in a)


# not in with if else statement
if 'lorem' not in a:
 print('no it not has lorem')
else:   
 print('yes it  has lorem')  
 
 
# Get the characters from position 2 to position 5 (not included) we use : between to position For Example 2:5


 print('sliced a', a[2:5])
 
 # By leaving out the start index, the range will start at the first character:

print("silced a without giving first index",a[:5])


# By leaving out the end index, the range will go to the end:

print("silced a without giving last index",a[2:])

# Use negative indexes to start the slice from the end of the string:

print("sliced with negative indexes",a[-2:-5])


# The upper() method returns the string in upper case:

print("converting lower case string to uppercase",a.upper())

# The lower() method returns the string in lower case:

upperCase="HELLO WORLD!"

print("converting upper case string to lowercase",upperCase.lower())

# The strip() method removes any whitespace from the beginning or the end:

print("a without trailing spaces",a.strip())

# The replace() method replaces a string with another string:

print("replacing lorem with hello.",a.replace('lorem',"hello"))

# The split() method splits the string into substrings if it finds instances of the separator:

splittingVar="hello ... yellow"

print('splitting variable',splittingVar.split('.'))

# To concatenate, or combine, two strings you can use the + operator.

q="hello"
e="world"
r=q+' '+e
print('printing the concatenation of q,w,e variables.',r)

# Use the format() method to insert numbers into strings:

age=14
birthYear=2009
text="My name is ahmad and I am {} years old and I born in {} "

print('concatenating numbers and string with each other',text.format(age,birthYear))


# We can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

text="My name is ahmad and I am {1} years old and I born in {0} "

print('concatenating numbers and string with each other with indexes',text.format(birthYear,age))


# Single Quote (\')
single_quote = 'This is a single quote (\') inside a string.'
print(single_quote)

# Backslash (\\)
backslash = 'This is a backslash (\\) inside a string.'
print(backslash)

# New Line (\n)
new_line = 'This is a line with a new line character (\n) in the middle.'
print(new_line)

# Carriage Return (\r)
carriage_return = 'This is a line with a carriage return character (\r) in the middle.'
print(carriage_return)

# Tab (\t)
tab = 'This is a line with a tab character (\t) in the middle.'
print(tab)

# Backspace (\b)
backspace = 'This is a line with a backspace character (\b) in the middle.'
print(backspace)

# Form Feed (\f)
form_feed = 'This is a line with a form feed character (\f) in the middle.'
print(form_feed)

# Octal Value (\ooo)
octal_value = 'This is an octal value: \110\145\154\154\157'  # \110 is 'H', \145 is 'e', and so on
print(octal_value)

# Hex Value (\xhh)
hex_value = 'This is a hex value: \x48\x65\x6c\x6c\x6f'  # \x48 is 'H', \x65 is 'e', and so on
print(hex_value)

# boolean 

print(2>4)
print(2<4)
print(2==4)

# The bool() function allows you to evaluate any value, and give you True or False in return,

d="hello"
f=23
g=["hello","blue"]
h=("hello","rio")
i={
    "hello":56,
    "red":"welcome"
}

print("converting string into boolean",bool(d))
print("converting number into boolean",bool(f))
print("converting array into boolean",bool(g))
print("converting tuple into boolean",bool(h))
print("converting dict into boolean",bool(i))
print("converting true into boolean",bool(True))

# , it always give fall if we give empty string,array,dict,tuple,0,None,False


d=""
f=0
g=[]
h=()
i={
    }

print("converting blank string into boolean",bool(d))
print("converting 0 number into boolean",bool(f))
print("converting blank array into boolean",bool(g))
print("converting blank tuple into boolean",bool(h))
print("converting blank dict into boolean",bool(i))
print("converting false boolean into boolean",bool(False))
print("converting None  into boolean",bool(None))

# python ARITHMETIC operators

# we use the + operator to add together two values:

a=2
b=6
print("sum of a,b is", a+b)

# we use the - operator to subtract two values:

print("difference between a,b is", b-a)

# we use the * operator to Multiply two values:

print("Product of a,b is", a*b)

# we use the / operator to divide two values:

print("division of a,b is", b/a)

# we use the % operator to check the remainder of two values after division:

print("remainder of a,b after division is", a%b)

# we use the ** operator to give the power, first value(base) raise to the power second value(exponent) :

print("ans of a raise to the power of b is", a**b)

# we use the // operator to divide first value to the second and it give us value in whole number 

b=7
print("ans of a divided by b in whole number is", b//a)

# comparision operator it always return boolean

# we use == operator to check that the first value equal to the second value 

x=6
y=2

print("checking is x equals to the y",x==y)

# we use != operator to check that the first value not equal to the second value 


print("checking is x not equals to the y",x!=y)

# we use > operator to check that the first value greater then the second value 


print("checking is x greater than the y",x>y)

# we use < operator to check that the first value smaller then the second value 


print("checking is x smaller than the y",x<y)

# we use >= operator to check that the first value greater then or equal to the second value 


print("checking is x greater than or equal to the y",x>=y)

# we use >= operator to check that the first value smaller then or equal to the second value 


print("checking is x smaller than or equal to the y",x<=y)

# logical operators , they always return boolean

# we use "and" operator to check the first and second condition both are true or false

z=4

print("we are using \'and\' operator to check that x is greater than y and z",x>y and x>z) 

# we use "or" operator to check that one of the first and second condition  are true or false

print("we are using \'or\' operator to check that x is greater than y or z(one of them)",x>y or x>z) 
 
# we use "not" operator to reverse the result, returns False if the result is true


print("we are using \'not\' operator to check that x is not greater than y and z",not(x>y and x>z))  


# list

thislist = ["apple", "banana", "cherry", "apple", "cherry","orange"]

# To determine how many items a list has, use the len() function:

print("length of thislist is",len(thislist))

# From Python's perspective, lists are defined as objects with the data type 'list':

print("type of thislist is",type(thislist))

# It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry"))
print("thislist with out using square brackets,by using list() function",thislist)

# accessing list items, List items are indexed and you can access them by referring to the index number:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print('the first item of thislist is',thislist[0])

# negative indexing, Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.

print("the last item of thislist is ", thislist[-1])

# to slice a range of items in an array we use index1(where from it start):index2(the next one index from where you want to end) For Example:2:5(not included)

print("this will print the item from 2 to 5(not included) index",thislist[2:5])

# By leaving out the start value, the range will start at the first item:

print('ranging list item without giving start index',thislist[:5])

# By leaving out the end value, the range will end at the last item:

print('ranging list item without giving end value',thislist[2:])

# slicing in negative number

print('slicing list item negative values',thislist[-4:-2])

# we can also use "in" keyword in the lists

if 'apple' in thislist:
 print('yes it has apple')
else:   
 print('no it not has apple')  
 
 # To change the value of a specific item, refer to the index number:

print("Original list",thislist)
thislist[0]="mango"
print("After changing first item",thislist)

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

print("Original list",thislist)
thislist[0:3]="mango","orange","pear"
print("After changing the range of item list",thislist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

print("Original list",thislist)
thislist[0:2]="mango","orange","pommegrante"
print("After changing the range of item list and adding one more at the index which is not exist in range ",thislist)

# The insert() method inserts an item at the specified index:

print("Original list",thislist)
thislist.insert(2,'watermelon')
print("Afteradding one more at the second index  ",thislist)

# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
print('original list',thislist)
thislist.append("orange")
print("list after adding a list item at the end",thislist)

# To append elements from another list to the current list, use the extend() method. we can also extend it with tuple for example

print("original list",thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("list after extending with an other list",thislist)

tuple1=("watermelon","melon")
print("original list",tropical)
tropical.extend(tuple1)
print("list after extending with tuple",tropical)

# The remove() method removes the specified item.if there are more than one item with the specified value, the remove() method removes the first occurance

thislist = ["apple", "banana", "cherry","banana"]
print("original list ",thislist)
thislist.remove("banana")
print("after removing banana from a list",thislist)

# The pop() method removes the specified index.If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
print("original list",thislist)
thislist.pop(1)
print("list after removing first index",thislist)
print("original list",thislist)
thislist.pop()
print("list without giving the value in pop function",thislist)


# The del keyword also removes the specified index. The del keyword can also delete the list completely.

thislist=["apple","banana","mango","cherry"]
print("original list",thislist)
del thislist[0]
print("list after deleting first index",thislist) 
thislist2=["apple","mango","cherry"]

del thislist2
print("there is nothing in list we delete even not the square bracket it completely finish it")

# The clear() method empties the list.The list still remains, but it has no content.

thislist1=["apple","cherry","banana"]
print("Original list",thislist1)
thislist1.clear()
print("list after clearing the list",thislist1)

# Python Day_01 End

# Python Day_02 Start

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

# python Day_02 End

# python Day_03 start

import myModule


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

# python Day_03 End

# Python also Ends approximately