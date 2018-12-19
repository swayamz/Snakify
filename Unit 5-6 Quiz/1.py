s = input()
if (s[0] == s[-1]):
    print(s[0])
else:
    if (len(s) > 2):
        print(s[:2]+(s[-2:]))
    else:
        print("Empty String")

