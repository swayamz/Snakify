# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(input())
c = int(input())

if (a % 2) > 0:
    d = (a // 2) + 1
else:
    d = a // 2
    
if (b % 2) > 0:
    e = (b // 2) + 1
else:
    e = b // 2
    
if (c % 2) > 0:
    f = (c // 2) + 1
else:
    f = c // 2
    
print(d+e+f)
