a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
a = str()
b = str()

if ((a1 % 2) != 0 and (a2 % 2) == 0) or ((a1 % 2) == 0 and (a2 % 2) != 0):
    a="WHITE"
if ((a1 % 2) != 0 and (a2 % 2) != 0) or ((a1 % 2) == 0 and (a2 % 2) == 0):
    a="BLACK"

if ((b1 % 2) != 0 and (b2 % 2) == 0) or ((b1 % 2) == 0 and (b2 % 2) != 0):
    b="WHITE"
if ((b1 % 2) != 0 and (b2 % 2) != 0) or ((b1 % 2) == 0 and (b2 % 2) == 0):
    b="BLACK"
    
if a==b:
    print("YES")
else:
    print("NO")
