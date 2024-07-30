# Counter App

class Counter:
    def __init__(self)->None:
        self.count:int = 0
    def addCount(self)->None:
        self.count += 1   
    def removeCount(self)->None:
        self.count -= 1
    def resetCount(self)->None:
         self.count = 0
counter:Counter = Counter()         
while True:
    print("\n=========== Counter Management System ==========================")
    print(f"Current Value Of Counter:  {counter.count}")
    print("1. increase Count.")
    print("2. decrease count.") 
    print("3. Reset count to zero")
    print("4. Exit") 
    choice:str = input("Enter Your Choice:  ") 
    match choice:
        case "1":
            counter.addCount()
            
        case "2":
            counter.removeCount()
            
        case "3":
            counter.resetCount()
            
        case "4":
            break
        case _:
            print("Invalid Choice")
    