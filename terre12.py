import sys
time24 = int(sys.argv[1].split(":")[0])
time2 = int(sys.argv[1].split(":")[1])

if time24 > 12:
    time12 = time24 - 12
    print("%d:%dPM" % (time12, time2))
if time24 < 13:
    print("%d:%dAM" %(time24, time2))

