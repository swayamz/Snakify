import random
secret = random.randint(1,9)
win = int(0);
while (win == 0):
    s = int(input())
    if (s == secret):
        print ("Well done you guessed it.")
        win = int(1)
    else:
        print ("You guessed wrong ")
        win = int(0)