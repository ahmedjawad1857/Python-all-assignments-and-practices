from typing import Any
import random
from time import sleep
class Lottery:
    def __init__(self)->None:
        self.persons:list[dict[str,Any]] = []
        self.l1:list[int] = [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
    def show_lottery_number(self)->None:
        print("Select Your Lottery Number.")  
        sleep(1)
        for i,num in enumerate(self.l1,1):
            print(f"{i}. '{num}'")
            
            
    def select_lottery(self,number:int,username:str)->None:

        for num in self.l1: 
            if num == number:
                
                newLottery:dict[str,Any] = {"Name":username,"Lottery_Number":num}
                self.persons.append(newLottery)
                self.l1.remove(num)
                   
                print(f"Congratulations!The number '{num}' is allotted to you.")
                # print(f"Congratulations! The number '{num}' is allotted to you ")
                print("list of lettery",self.l1)
                print("list of persons",self.persons)
                break
        else:
                print("this number is not available! Please Try again.")
    def delete_lottery(self,Lottery_Number:int)->None:
        for person in self.persons:
          if person["Lottery_Number"] == Lottery_Number:
            ind:int=self.persons.index(person)
            popped:dict[str,Any] = self.persons.pop(ind)
            self.l1.append(popped["Lottery_Number"])
            print(f"The user whose name is {popped["Name"]} with Lottery Number '{popped["Lottery_Number"]}' is deleted.")
            self.l1.sort()
            print(self.l1)
            break
        else:
            print(f"An error occurred")                  
     
    def withdraw_lottery(self)->None:  
        num:int = random.randint(1001,1010)
        for person in self.persons:
          if person["Lottery_Number"] == num:
            print(f"The User whose name is {person['Name']} and lottery number is {num},won the lottery.")
            break
        else:
            print(f"An error occurred")    
app:Lottery=Lottery()

while True :
    print("====================Lottery Management System================")
    if len(app.l1) != 0:
        print("1.Choose Lottery Number")
        print("2.Delete Lottery")
        print("3.Exit")
    
        choice:int=int(input("Select Your Choice!   "))
        match choice:
         case 1:
            app.show_lottery_number() 
            Lottery_Num:int = int(input("Please enter your Lottery Number:   "))
            name:str = input("Please enter your Name:   ")
            app.select_lottery(Lottery_Num, name)  
         case 2:
             lotteryNumber:int = int(input("Please enter your lottery Number:"))
             app.delete_lottery(lotteryNumber)
         case 3:
            print("Good Bye!")
            break
         case _:
            print("Please enter Valid Choice...")
    else:
        app.withdraw_lottery() 
        break   
          
# # from typing import Any
# # import random
# # from time import sleep

# # class Lottery:
# #     def __init__(self) -> None:
# #         self.persons: list[dict[str, Any]] = []
# #         self.l1:list[int] = [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
# #     def show_lottery_number(self) -> None:
# #         print("Select Your Lottery Number.")
# #         sleep(1)
# #         for i, num in enumerate(self.l1, 1):
# #             print(f"{i}. '{num}'")

# #     def select_lottery(self, number: int, username: str) -> None:
# #         for num in self.l1:
# #             if num == number:
# #                 newLottery: dict[str, Any] = {"Name": username, "Lottery_Number": num}
# #                 self.persons.append(newLottery)
# #                 self.l1.remove(num)
# #                 print(f"Congratulations! The number '{num}' is allocated to You.")
# #                 break
# #         else:
# #             print("This number is not available. Try Again")

# #     def withdraw_lottery(self) -> None:
# #         num: int = random.randint(1001, 1010)
# #         for person in self.persons:
# #             if person["Lottery_Number"] == num:
# #                 print(f"The Winner is {person['Name']}, and the winning number is {person['Lottery_Number']}.")
# #                 break

# # app: Lottery = Lottery()

# # while True:
# #     print("====================𝕃𝕠𝕥𝕥𝕖𝕣𝕪 𝕄𝕒𝕟𝕒𝕘𝕖𝕞𝕖𝕟𝕥 𝕊𝕪𝕤𝕥𝕖𝕞================")
# #     print("1. Choose Lottery Number")
# #     print("2. Exit")
# #     choice: int = int(input("Select Your Choice!   "))

# #     match choice:
# #         case 1:
# #             l1: list[int] = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
# #             app.show_lottery_number()
# #             name: str = input("Please enter your Name:   ")
# #             Lottery_Num: int = int(input("Please enter your Lottery Number:   "))
# #             app.select_lottery(Lottery_Num, name)

# #         case 2:
# #             print("Good Bye!")
# #             break

# #         case _:
# #             print("Please enter Valid Choice...")

# #     if len(app.persons) == 10:
# #         app.withdraw_lottery()
# from typing import Any
# import random
# from time import sleep

# class Lottery:
#     def __init__(self) -> None:
#         self.persons: list[dict[str, Any]] = []
#         self.l1: list[int] = [1001, 1002, 1003]

#     def show_lottery_number(self) -> None:
#         print("Select Your Lottery Number.")
#         sleep(1)
#         for i, num in enumerate(self.l1, 1):
#             print(f"{i}. '{num}'")
            
#     # def select_lottery(self, number: int, username: str) -> None:
#     #     if len(self.l1) > 1:
#     #         for num in self.l1:
#     #             if num == number:
#     #                 newLottery: dict[str, Any] = {"Name": username, "Lottery_Number": num}
#     #                 self.persons.append(newLottery)
#     #                 self.l1.remove(num)
#     #                 print(f"Congratulations! The number '{num}' is allotted to you.")
#     #                 print("List of lottery:", self.l1)
#     #                 print("List of persons:", self.persons)
#     #                 break
#     #         else:
#     #             print("This number is not available! Please try again.")
#     #     else:
#     #         num = self.l1[0]
#     #         newLottery1: dict[str, Any] = {"Name": username, "Lottery_Number": num}
#     #         self.persons.append(newLottery1)
#     #         self.l1.remove(num)
#     #         print(f"Ohh! So, sorry but the last number is left which is allotted to you.")
#     #         print(f"The number is {num}")
#     def select_lottery(self, number: int, username: str) -> None:
#       if len(self.l1) > 1:
#         for num in self.l1:
#             if num == number:
#                 newLottery: dict[str, Any] = {"Name": username, "Lottery_Number": num}
#                 self.persons.append(newLottery)
#                 self.l1.remove(num)
#                 print(f"Congratulations! The number '{num}' is allotted to you.")
#                 print("List of lottery:", self.l1)
#                 print("List of persons:", self.persons)
#                 break
#         else:
#             print("This number is not available! Please try again.")
#       elif len(self.l1) == 1 and self.l1[0] == number:
#         num = self.l1[0]
#         newLotter: dict[str, Any] = {"Name": username, "Lottery_Number": num}
#         self.persons.append(newLotter)
#         self.l1.remove(num)
#         print(f"Ohh! So, sorry but the last number is left which is allotted to you.")
#         print(f"The number is {num}")
#       else:
#         print("Invalid lottery number!")

#     def withdraw_lottery(self) -> None:  
#         num: int = random.randint(1001, 1003)
#         for person in self.persons:
#             if person["Lottery_Number"] == num:
#                 print(f"The user, {person['Name']}, with lottery number {num}, won the lottery.")
#             else:
#                 print(f"There Was an error occuring while processing. ")

# app = Lottery()

# while True:
#     print("==================== Lottery Management System ====================")
#     if len(app.l1) != 0:
#         print("1. Choose Lottery Number")
#         print("2. Exit")
    
#         choice = int(input("Select Your Choice!   "))
#         match choice:
#             case 1:
#              if len(app.l1) != 1:  
#               app.show_lottery_number() 
#               Lottery_Num:int = int(input("Please enter your Lottery Number:   "))
#              name:str = input("Please enter your Name:   ")
#              app.select_lottery(Lottery_Num, name) 
#             case 2:
#                 print("Good Bye!")
#                 break
            
#             case _:
#                 print("Please enter Valid Choice...")
#     else:
#         app.withdraw_lottery()  
