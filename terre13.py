import sys
time24 = int(sys.argv[1][0:5].split(":")[0])
time2 = int(sys.argv[1][0:5].split(":")[1])
AMPM = sys.argv[1][5:7]
if AMPM == "PM":
    print("%d:%d" % (time24+ 12, time2))
else:
    print("%d:%d" % (time24 , time2))