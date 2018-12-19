maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1       
print(num_maximal)

#A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are equal to its largest element. 
