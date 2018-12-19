a = int(input())
b = int(input())
for i in range(a+1, b):
    if((i % 2) > 0 and (i % 3) > 0 and (i % 4) > 0 and (i % 5) > 0 and (i % 6) > 0 and (i % 7) > 0 and (i % 8) > 0 and (i % 9) > 0):
        print(i)
        