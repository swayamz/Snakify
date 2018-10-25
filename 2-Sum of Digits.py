#Takes three digit number and prints the sum of the digits
a = int(input())
one = int(a % 10)
two = int(((a % 100) - (a % 10))/10)
thr = int(((a % 1000) - (a % 100))/100)
print(one+two+thr)