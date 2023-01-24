import sys
if len(sys.argv) == 2:
    try:
         float(sys.argv[1])
         if int(sys.argv[1][-1]) % 2 == 0 :
                print("pair")
         else:
             print("impair")

    except ValueError:
        print ("Tu ne me la mettras pas à l’envers.")
else:
    print("Tu ne me la mettras pas à l’envers.")