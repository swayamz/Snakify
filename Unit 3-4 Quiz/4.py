ax = int(input()) 
ay = int(input())
bx = int(input())
by = int(input())
cx = int(input())
cy = int(input())

if (ax == bx):
    if (ay == cy):
        print("The third coordinate is", "(",cx,",",by,")")
    else:
        print("The third coordinate is", "(",cx,",",ay,")")
if (bx == cx):
    if (by == ay):
        print("The third coordinate is", "(",ax,",",cy,")")
    else:
        print("The third coordinate is", "(",ax,",",by,")")
if (ax == cx):
    if (ay == by):
        print("The third coordinate is", "(",bx,",",cy,")")
    else:
        print("The third coordinate is", "(",bx,",",ay,")")
      
    
