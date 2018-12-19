#Even Indices
#Given a list of numbers, find and print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...). 
a = input().split()
for i in range(0, len(a), 2):    
    print(a[i])
    
#Even Elements
#Given a list of numbers, find and print all elements that are an even number. In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range() 
a = [int(i) for i in input().split()]
for elem in a:
    if elem % 2 == 0:
        print(elem)
        
#Greater than previous
#Given a list of numbers, find and print all the elements that are greater than the previous element. 
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:        
        print(a[i])

#Neighbors of the same sign
#Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank. 
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break

#Greater than neighbours
#Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.
#The first and the last items of the list shouldn't be considered because they don't have two neighbors. 
a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)

#The largest element
#Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest element and then the index number. If the highest element is not unique, print the index of the first instance. 
index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)

#The number of distinct elements
#Given a list of numbers with all of its elements sorted in ascending order, determine and print the quantity of distinct elements in it. 
a = [int(i) for i in input().split()]
num_distinct = 1
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        num_distinct += 1
print(num_distinct)

#Swap neighbours
#Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element in place. 
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

#Swap min and max
#Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list. 
a = [int(s) for s in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]
print(' '.join([str(i) for i in a]))

#The number of pairs of equal
#Given a list of numbers, count how many element pairs have the same value (are equal). Any two elements that are equal to each other should be counted exactly once. 
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            counter += 1
print(counter)

#Unique elements
#Given a list of numbers, find and print the elements that appear in the list only once. The elements must be printed in the order in which they occur in the original list. 
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
        
#Queens
#In chess it is known that it is possible to place 8 queens on an 8×8 chess board such that none of them can attack another. Given a placement of 8 queens on the board, determine if there is a pair of queens that can attach each other on the next move. Print the word NO if no queen can attack another, otherwise print YES. The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chess board with rows and columns numbered starting at 1. 
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False
if correct:
    print('NO')
else:
    print('YES')
    
#The bowling alley
#In bowling, the player starts wtih 10 pins at the far end of a lane. The object is to knock all the pins down. For this exercise, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled. The balls are numbered from 1 to N (inclusive) for this situation. The subsequent number pairs, one for each K represent the start to stop (inclusive) positions of the pins that were knocked down with each role. Print a sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked down. 
n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))