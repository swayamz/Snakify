a1= int(input())
a2= int(input())
b1= int(input())
b2= int(input())

if (abs(a1-b1) == 1 and abs(a2-b2) ==1) or (abs(a1-b1) == 0 and abs(a2-b2) ==1) or (abs(a1-b1) == 0 and abs(a2-b2) ==0) or (abs(a1-b1) == 1 and abs(a2-b2) ==0):
    print("YES")
else:
    print("NO")