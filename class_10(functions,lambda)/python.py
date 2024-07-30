from typing import Callable

def my_decorator(func: Callable[[int], None]) -> Callable[[int], None]:
    def wrapper(num1: int) -> None:
        print("Something is happening before the function is called.")
        func(num1)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(num1: int) -> None:
    print(num1)

say_hello(100)

# gloabal keyword
def my_func(num1: int) -> None:
    global c
    c=num1+num1+num1    
    d="hello world"

    print(list(locals()))
# Call the function to define the variable 'c' in the global scope
my_func(5)

# Now you can print 'c' because it has been defined in the global scope
print("c",c)
print(list(globals()))
print("hello")

