## Match statement

userInput=int(input("Enter Number From 1 to 7 to check the name of the day\t"))

#  match statement          
match  userInput:                                         
    case 1: 
        print("Monday")
    case 2:
        print("Tuesday")   
    case 3:
        print("WednesDay")       
    case 4:
        print("Thursday")   
    case 5:
        print("Friday")   
    case 6:
        print("Saturday")   
    case 7:
        print("Sunday")   
    case _:
         print("Please Enter Number Between 1-7")
             
            
print("if statement code started")            
# Same code in if,elif,else statement

if (userInput==1):
    print("Monday")  
elif (userInput==2):
    print("Tuesday")  
elif (userInput==3):
    print("Wednesday")  
elif (userInput==4):
    print("Thursday")  
elif (userInput==5):
    print("Friday")  
elif (userInput==6):
    print("Saturday")  
elif (userInput==7):
    print("Sunday")  
else:
    print("Please Enter Number between 1 - 7")
    
    
    
    
    
    
    
                  