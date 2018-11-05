#Given an integer number, print its last digit.
a = int(input())
second = int(a % 10)
first = int(((a % 100) - (a % 10))/10)

print(str(second) + str(first))