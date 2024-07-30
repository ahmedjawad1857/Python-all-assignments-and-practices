import string
import random
from pyperclip import copy 

def generate_random_string() -> None:
   try:
    length:int = int(input("Enter the length of the string(0-1000000) you want to generate...  "))
    if length > 0 and length <= 1000000:
        random_string:str = ''.join(random.choice(string.ascii_letters + '\n') for _ in range(length))
        print(random_string)
        
        copy(random_string)
        print('\nCopied to clipboard paste it anywhere!')
    else:    
        print('Please enter a value between "0" and "1000000"!')
   except ValueError:
        print('Please enter a numeric value between "0" and "1000000"!')

generate_random_string()
