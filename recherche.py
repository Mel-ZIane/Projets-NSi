L = [1,2,3,4,5,6,7,8,9,10]
debut = 0
fin  = 9
val = 4
trouv = False
while trouv == False and debut <= fin:
    m = int(debut + fin)//2
    if L[m] == val:
        trouv = True
    else:
        if val > L[m]:
            debut = m + 1
        else:
            fin = m-1
print (trouv)
