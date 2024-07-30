
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

