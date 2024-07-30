# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All three numbers are equal")
    equal_count = 3
    distinct_count = 0
elif num1 == num2:
    print(f"The first and second numbers, {num1} and {num2}, are equal")
    equal_count = 2
    distinct_count = 1
elif num2 == num3:
    print(f"The second and third numbers, {num2} and {num3}, are equal")
    equal_count = 2
    distinct_count = 1
elif num1 == num3:
    print(f"The first and third numbers, {num1} and {num3}, are equal")
    equal_count = 2
    distinct_count = 1
else:
    greatest = max(num1, num2, num3)
    print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")
    equal_count = 0
    distinct_count = 3

# Compare counts
if equal_count > distinct_count:
    print(f"The numbers that are equal ({equal_count}) are greater than the distinct numbers ({distinct_count})")
elif equal_count < distinct_count:
    print(f"The distinct numbers ({distinct_count}) are greater than the numbers that are equal ({equal_count})")
else:
    print("The counts of equal and distinct numbers are the same")
