import sys

if len(sys.argv) == 2 :

    try:
        a = int(sys.argv[1])
        if a > 0:
            if (str(a ** 0.5))[-1] == "0":
              print(int(a**0.5))
            else:
                print(a**0.5)
        else:
            print("erreur.")
    except ValueError:
        print("erreur..")
else:
    print("erreur..")
