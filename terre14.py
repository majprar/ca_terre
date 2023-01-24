import sys
nbr1 = int(sys.argv[1])
nbr2 = int(sys.argv[2])
nbr3 = int(sys.argv[3])
list = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
max = 0
min = 0
mil = 0
for i in list:
    if i >= nbr1 and i >= nbr2 and i >= nbr3:
        list.remove(i)
    if i <= nbr1 and i <= nbr2 and i <= nbr3:
        list.remove(i)
print(list[0])

if nbr3 == nbr2 and nbr2 == nbr1:
    print("erreur.")