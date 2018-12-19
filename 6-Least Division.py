#Given an integer not less than 2. Print its smallest integer divisor greater than 1. 
i = 2
while n % i != 0:
    i += 1
print(i)