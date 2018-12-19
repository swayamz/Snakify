s = input()
first = s[0]
length = len(s)
a = []

a.append(first)
for i in range(2, length + 1):
    currentletter = s[i-1]
    if (currentletter == first):
        a.append("$")
    else:
        a.append(currentletter)

print(a)