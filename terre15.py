import sys

check = 0
for i in range(1,len(sys.argv) - 1):
    try:
        int(sys.argv[i])
    except ValueError:
        print("erreur.")
        check = 1
        break
if check == 0:
    for y in range(1,len(sys.argv) - 1):
        if int(sys.argv[y]) > int(sys.argv[y + 1]):
            print("pas trié")
            check = 2
            break
if check == 0:
    print("trié")