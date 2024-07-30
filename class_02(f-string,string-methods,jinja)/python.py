# String and it's methods

# What is String?
# String is the collection/sequence of characters

name:str = "Ahmad"
print("name",name)

# What is f-string?
# F-strings in Python provide a concise and readable way to embed expressions inside string literals.

# Defining a f-string

full_name:str = f"{name} Jawad"
print("name",name)
print("full_name",full_name)

# we use \n for inserting a new line in string

pythonIntro:str = "I am learning python \nIt is easy to read"
print("python Intro \n"+pythonIntro)

# we use single quotes inside double quotes

ceo_of_openai:str = "openAi's ceo name is sam altman"
print(ceo_of_openai)

# we also use single qoute in double qoute string by using \'

qoute:str = "Ahmad Say\'s \'something...\'"
print(qoute)

# we use double quotes inside single quotes

double_qoute_example:str = ' this is the example of using double qoute in single qoutes "my name is ahmad" '
print(double_qoute_example)

# we also use double qoute in single qoute string by using \"

qoutes:str = "Ahmad Says \"something...\""
print(qoutes)

# if we want to use \ we use it in string like this \\\\

# convert any special character into simple in string  by adding \\ in the backside of the special character

forward_slash:str = "The chef prepared a delicious meal\\A delicious meal was prepared by the chef."
print(forward_slash)

# if you want to add  many line string you use ''' ''' or """" """

many_lines_double_qoutes:str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

many_lines_single_qoutes:str = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
print("with single qoutes",many_lines_single_qoutes)
print("with double qoutes",many_lines_double_qoutes)

# We check type using type() built-in function

hello="hello world"
print("type of hello",type(hello))

# concatenation of string

# we can concatenate string using "+" sign

print("a"+"b"+"c")

# we can also concatenate variables

first_name:str = "Ahmad"
last_name:str = " Jawad"

print("concatenation of variables",first_name+last_name)

# we cannot concat strings with integers

age:int = 14
student_name:str = "Ahmad"

# print("student name: "+student_name+"student age: "+age)
# it throws error

# we can concatenate it by using str() method. str() method is used to convert integer into string

print("student name: "+student_name+" student_age "+str(age))

# F-string and Jinja style

# f-string
print(f"student_name: {student_name}")

# format strings example ,it takes unlimited placeholders

txt:str = "My name is Ahmad, and I am {} years old."
print("format string example",txt.format(age))

# or we can use index to be sure that arguments are placed correctly

quantity:int = 3
item_no:int = 2
price:int = 50
myorder:str = "I want to pay {2} rupees for {0} pieces of item {1}."
print(myorder.format(quantity, item_no, price))

# capitalize() and lower() , upper() methods example
name1: str = "m.aHmAd"
print("Original name",name1)
print("upper() method example",name1.upper())
print("capitalize() method example",name1.capitalize())
print("lower() method example",name1.lower())

# another method which is better than f-string because we can also add python functions

student_code : str = """
print("My Name is Muhammad Ahmad")
a:int = 7
b:int = 8
print(a + b)
"""

exec(student_code)

# casefold() method


#variable_name.method()
print(name1)
print(name1.casefold())

# lstrip(),rstrip() and strip() method example 

name2:str = "     Muhammad       Ahmad         "
print("Original name",name2)
print("left strip method"+name2.lstrip())
print(name2.rstrip()+"right strip method")
print("strip method"+name2.strip())

# re.sub() method delte all the spaces only left one space in the center

import re

name3 : str = "      MuHammAd           ahmad         "

print(name3)

name4 : str = re.sub(' {2,100}',' ', name3).strip()
print(name4)