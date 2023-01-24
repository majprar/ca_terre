import sys

if len(sys.argv) == 3:

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        if a > b and a * b != 0:

            print("resultat: %d" % (a/b))
            print("reste: %d" % (a % b))
    except ValueError:
        print("erreur..")
else:
    print("erreur..")
