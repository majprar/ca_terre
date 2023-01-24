import sys
if len(sys.argv) == 2 and sys.argv[1] != "" and sys.argv[1].isspace() is False:
    check = False
    y = 0
    for x in sys.argv[1]:
        y = y + 1
        if x.isdigit():
            check = True
            print("erreur.")
            break
    if not check :
        print(y)
else:
    print("erreur.")


