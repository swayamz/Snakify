#H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.
hours = int(input())
minutes = int(input())
seconds = int(input())

han = ((hours * 30) + ((minutes + seconds/60)/60)*30)
print(han)