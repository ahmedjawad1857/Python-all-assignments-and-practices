import sys

print("line1")
print("line2")

print(type(sys.argv))

if len(sys.argv) > 1 and sys.argv[1] == '-g':
    print("I will install this package globally on your system!")
else:
 print("it doesn't installed")       

print(sys.argv)
