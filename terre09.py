import sys

if len(sys.argv) == 3 :

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        if b > 0:
          print("%d" % (a**b))
        else:
            print("erreur")


    except ValueError:
        print("erreur..")
else:
    print("erreur..")
