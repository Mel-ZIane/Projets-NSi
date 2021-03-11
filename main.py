print (" Cette algorytme permet de retrouver qu'elle jour de la semaine tu es né si tu ne le connais pas")
Jour_de_n  = int(input("Inscris ici ton jour de naissance "))
Mois_de_n = int(input("Inscris ici ton mois de naissance (par exemple si c'est Février écris 2) "))
Anné_de_n = int(input("Inscris ici ton année de naissance"))
a=0
q=0
j=0
Jour_de_n = j
a = Anné_de_n - 1901
q = a // 4
if Mois_de_n == 1:
    Mois=de_n = 31
if Mois_de_n == 2:
    Mois_de_n = 59
if Mois_de_n == 3:
    Mois_de_n = 90
if Mois_de_n == 4:
    Mois_de_n = 120
if Mois_de_n == 5:
    Mois_de_n = 151
if Mois_de_n == 6:
    Mois_de_n = 181
if Mois_de_n == 7:
    Mois_de_n = 212
if Mois_de_n == 8:
    Mois_de_n = 243
if Mois_de_n == 9:
    Mois_de_n = 273
if Mois_de_n == 10:
    Mois_de_n = 304
if Mois_de_n == 11:
    Mois_de_n = 334
if Mois_de_n == 12:
    Mois_de_n = 395
i=0
i = a + q + Mois_de_n + j +1
s = i%7
if s == 0:
    print("Tu es né un Dimanche")
if s == 1:
    print("Tu es né un Lundi")
if s == 2:
    print("Tu es né un Mardi")
if s == 3:
    print("Tu es né un Mercredi")
if s == 4:
    print("Tu es né un Jeudi")
if s == 5:
    print("Tu es né un Vendredi")
if s == 6:
    print("Tu es né un Samedi")


