# List,list-Methods

# ->                    0        1         2
fruits : list[str] = ["Banana","Kiwi", "Apple"]
# <-                    -3     -2          -1

print(fruits[-2]) # it prints Kiwi

# all methods/attributes

[print(i) for i in dir(list) if "__" not in i]

