import sys
a = ""
if len(sys.argv) == 2 and sys.argv[1] != "" and sys.argv[1].isspace() is False:
   print(sys.argv[1][::-1])
else:
    print("Veuillez écrire 'UN' argument")