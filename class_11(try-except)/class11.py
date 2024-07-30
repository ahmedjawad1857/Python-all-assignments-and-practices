a : list[str] = ['a','b'] # mutable
b : list[str] = ['c','d'] # mutable

print(id(a))
print(id(b))

print(a+b)
print(5 - 7) # test update

# try-except

print("logic1")
print("logic2")

l1: list[int] = [1, 2, 3]

try:
    print(5/0)  # This will raise a ZeroDivisionError , it does not check the next print() method
    print(l1[0])
    print(xyz)  # This will raise a NameError
except ZeroDivisionError:
    print("Zero Division Error!")
except IndexError:
    print("IndexError")
except NameError:
    print("NameError")
    
print("logic4")
print("logic5 \n")


# simple way to identify which type of error is this.
print("Simple Way Started")
print("logic1")
print("logic2")
try:
    print(5/2)
    print(l1[0])
    print(xyz)  # This will raise a NameError
except (ZeroDivisionError, IndexError, NameError) as e:
    print(f"Error: {e}")

print("logic4")
print("logic5")
