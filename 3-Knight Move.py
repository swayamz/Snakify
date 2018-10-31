x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
xchange = abs(x1 - x2)
ychange = abs(y1 - y2)
if xchange == 1 and ychange == 2 or xchange == 2 and ychange == 1:
    print('YES')
else:
    print('NO')