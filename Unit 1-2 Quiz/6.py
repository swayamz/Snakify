import math
day = int(input())
#thursday = 1
if ((day + 3) % 7)==1:
    print("Monday")
if ((day + 3) % 7)==2:
    print("Tuesday")
if ((day + 3) % 7)==3:
    print("Wed")
if ((day + 3) % 7)==4:
    print("Thursday")
if ((day + 3) % 7)==5:
    print("Friday")
if ((day + 3) % 7)==6:
    print("Saturday")
