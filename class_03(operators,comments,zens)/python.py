# Python Operators


# Python Arithmetic Operators

# No. Operator	Name	   Example
# 1	  +	    Addition	    x + y 
# 2	  -	    Subtraction	    x - y 
# 3	  *	    Multiplication  x * y 
# 4	  /	    Division	    x / y 
# 5	  %	    Modulus	        x % y 
# 6	 **	    Exponentiation	x ** y
# 7	 //	    Floor division	x // y 

a : int|float = 7
b : int = 2

print(f"{a} + {b} = {a+b}") # addtition
print(f"{a} - {b} = {a-b}") # subtraction
print(f"{a} * {b} = {a*b}") # multiplication
print(f"{a} / {b} = {a/b}") # division
print(f"{a} % {b} = {a%b}") # Modulus(give remainder after division)
print(f"{a} ** {b} = {a**b}") # Exponential(x(value before operator) raise to the power y(value after operator))
print(f"{a} // {b} = {a//b}") # Float division(It gives the nearest whole number of the answer of division)

# Python Assignment Operators

# No. Operator Example   Same As	
# 0	 =	     x = 5	    x = 5	
# 1	 +=	     x += 3	    x = x + 3	
# 2	 -=	     x -= 3	    x = x - 3	
# 3	 *=	     x *= 3	    x = x * 3	
# 4	 /=	     x /= 3	    x = x / 3	
# 5	 %=	     x %= 3	    x = x % 3	
# 6	 //=	 x //= 3	x = x // 3	
# 7	 **=	 x **= 3	x = x ** 3	
# 8	 &=	     x &= 3	    x = x & 3	
# 9	 |=	     x |= 3	    x = x | 3	
# 10 ^=	     x ^= 3	    x = x ^ 3	
# 11 >>=	 x >>= 3	x = x >> 3	
# 12 <<=	 x <<= 3	x = x << 3	

# We mostly use first 7 operators other are not use mostly.
# The recommendable syntax is to use simple(a=a+3) because the other method is complex

# assign
a=5
# assigning and adding same value
a+=3
# assigning and subtracting same value
a-=3
# assigning and multiplication same value
a*=3
# assigning and dividing same value
a/=3
# assigning and modulus same value
a%=4
# assigning and FLOAT DIVISION same value
a//=2
# assigning and exponential same value
a**=4

#:=
print(a := 7)


# Python Comparison Operators

# Comparision operators alwaya return boolean(true or false)

# Comparison operators are used to compare two values:

# No.     Operator	     Name                      Example
#  0	       ==	        Equal	                    x == y	
#  1	       !=	        Not equal	                x != y	 
#  2	       >	        Greater than	            x > y	
#  3	       <	        Less than	                x < y	
#  4	       >=	        Greater than or equal to	x >= y	
#  5	       <=	        Less than or equal to	    x <= y	

x=6
y=7
print(f"{x} == {y}: {x==y}") # Equal Operator
print(f"{x} != {y}: {x!=y}") # Not equal Operator
print(f"{x} > {y}: {x>y}") # Greater than Operator
print(f"{x} < {y}: {x<y}") # Less than Operator
print(f"{x} >= {y}: {x>=y}") # Greater than or equal to Operator
print(f"{x} <= {y}: {x<=y}") # Less than or equal to Operator


# Python Logical Operators

# No.  Operator	            Description	                                    Example	
# 0	  and	    Returns True if both statements are true	            x < 5 and x < 10	
# 1	  or	    Returns True if one of the statements is true           x < 5 or x < 4	
# 2	  not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	

# Logical operators are used to combine conditional statements, it is used with comparision operators

# and لازمی
# or = optional
# not
#1        2        3        4
print(True and True and True and True  )
print(True and True and False and True)
print(False and False and False and True)
print(not(True and True)) # it returns false

# and لازمی
# or = optional
#1        2        3        4
print(True or True or True or True  )
print(True or True or False or True)
print(False or False or False or True)
print(False or False or False or False)

c=3
d=5
print(f"{d} > {c} and {c} <= {d}: {d > c and c <= d}") # and operator example(here both conditions are true)
print(f"{d} > {c} and {c} >= {d}: {d > c and c >= d}") # and operator example(here only one condition is true)
print(f"{d} > {c} or {d} <= {c}: {d > c or d <= c}") # or operator example(here first condition is true)
print(f"not({d} > {c} or {d} <= {c}): {not(d > c or d <= c)}") # or operator example(here first condition is true and the answer is true but it gives false due to not)

name : str = "Qasim"
print(not name=="Qasim")
# name == "Qasim"
# "Qasim" == "Qasim"
# True

# Python Identity Operators

# Operator	               Description	                        Example	
# is 	    Returns True if both variables are the same object	    x is y
# is not	Returns True if both variables are not the same object	x is not y

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

e:list[str] = ["apple", "banana"]
f:list[str] = ["apple", "banana"]
z = e

print(e is z)

# returns True because z is the same object as e

print(e is f)

# returns False because e is not the same object as f, even if thef have the same content

print(e == f)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because e is equal to f

print(e is not z)

# returns False because z is the same object as e

print(e is not f)

# returns True because e is not the same object as f, even if thef have the same content

print(e != f)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because e is equal to f


# Membership Operators

# No. Operator	            Description	                           Example	
# 0	   in	    Returns True if a sequence with the specified ...	x in y	
# 1	   not in	Returns True if a sequence with the specified ...	x not in y	

# Membership operators are used to test if a sequence is presented in an object:

names: list[str] = [chr(i) for i in range(65,91)]
print(names)

print("It give False because Pakistan is not in names(due to we use in operator)","Pakistan" in names)
print("It give True because Pakistan is not in names(due to we use not in operator instead of in operator)","Pakistan" in names)

# Presidency of Arithmetic Operators Or PEDMAS,BODMAS

print(3 + 2 - 2 * 4 /2 + 2)
#     3+2−2×4÷2+2
#     3 + 2 - 4 + 2
#      6    - 8

# Alright, let's solve the equation step by step. We'll use the order of operations, often remembered by the acronym PEMDAS/BODMAS:

# Parentheses/Brackets
# Exponents (ie Powers and Square Roots, etc.)/Orders (ie Powers and Square Roots, etc.)
# MD Multiplication and Division (left-to-right)
# AS Addition and Subtraction (left-to-right)
# Given the expression:

# [ 3 + 2 - 2 \times 4 \div 2 + 2 ]

# Let's solve it step by step:

# Multiplication and Division:
# [ 2 \times 4 = 8 ] [ 8 \div 2 = 4 ]

# Replacing these values in the expression, we get:

# [ 3 + 2 - 4 + 2 ]

# Addition and Subtraction (from left to right):
# [ 3 + 2 = 5 ] [ 5 - 4 = 1 ] [ 1 + 2 = 3 ]

# So, the final answer is:

# [ 3 ]



# If we multiply a string with 3(any int)

print(3*"a")
# aaa

# Without walrus operator
x = 10
if x > 5:
    print(x)

# With walrus operator
if (x := 10) > 5:
    print(x)
    
for i in range(0,228):
 print(i,  chr(i))       
    
