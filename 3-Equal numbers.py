a = input()
b = input()
c = input()

if a==b and b==c:
    print("3")
if a==b and b!=c:
    print("2")
if a==c and b!=a:
    print("2")
if a!=b and b!=c and a!=c:
    print("0")
if a!=b and b==c:
    print("2")