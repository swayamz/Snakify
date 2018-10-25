#Hour hand turned by degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.
a = float(input())
print(a % 30 * 12)