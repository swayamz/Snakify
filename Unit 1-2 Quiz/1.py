import math
print("Input your name")
name = str(input())
print("Input length/radius")
length = int(input())
print("Input width, doesn't matter for spherical")
width = int(input())
print("Input height")

height = int(input())

print(name, "needs", (5.78 * ((length ** 2) * height * math.pi)), "Gallons Required for Spherical Pool")
print(name, "needs", (7.5 * (length * width * height)), "Gallons Required for Rectangular/Square Pool")