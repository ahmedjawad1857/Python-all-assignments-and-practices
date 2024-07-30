import sys

print(sys.path)
name : str = "Pakistan"
print(name) # print
print(type(name)) # type
print(id(name)) # physcial address
print([i for i in dir(name) if "__" not in i]) # methods and attributes


