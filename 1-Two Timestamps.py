a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())
b3 = int(input())


a = (a1 * 60 * 60) + (a2 * 60) + a3
b = (b1 * 60 * 60) + (b2 * 60) + b3
print(abs(a-b))