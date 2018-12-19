n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
    
#Given a non-negative integer n, print the nth Fibonacci number ϕn.
#This problem can also be solved with a for loop.

