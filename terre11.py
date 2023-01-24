import sys

if len(sys.argv) == 2 :

    try:
        a = int(sys.argv[1])
        if a  <= 0 :
            a = a * -1
        if a == 1 or a == 0:
            print("Non, %s n'est pas un nombre premier." % sys.argv[1])
        else:
            for i in range(2,a):
                if a % i == 0 :
                    print("Non, %s n'est pas un nombre premier." % sys.argv[1])
                    break
                if i == int(a/2):
                    print ("Oui, %s est un nombre premier." % sys.argv[1])




    except ValueError:
        print("erreur..")
else:
    print("erreur..")