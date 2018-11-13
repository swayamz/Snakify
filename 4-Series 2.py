# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
if a > b or a == b:
    for i in range(a, b - 1, -1):
        print(i)

#Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.