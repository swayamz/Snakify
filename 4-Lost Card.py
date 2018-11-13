n = int(input())
a = 0
for i in range(1, n + 1):
    a += i
for i in range(n - 1):
    a -= int(input())
print(a)
#Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

