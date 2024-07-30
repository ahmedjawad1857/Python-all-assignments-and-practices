# Python loops

# python has two main loops
# 1.for loop
# 2.while loop

# for loop

names:list[str]=["Ahmad","Moosa","Jawad"]
for name in names:
 print("The guy name is",name,"using for loop")  
 
# for loop has a shortcut syntax called comprehensive loop

[print("The guy name is",name,"using for loop shotcut syntax also known as comprehensive loop") for name in names]  
 
# while loop

i:int=0
while i<len(names): # names length =3
    print("The guy name is",names[i], "using while loop")
    i += 1  
    
    