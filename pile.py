Pile & File
#Fonction

class Pile:
    def __init__(self):
        self.data = []


    def empiler(self,element):
        self.data.append(element)
        return self.data

    def hauteur(self):
        return len(self.data)

    def est_vide(self):
        return self.hauteur() == 0

    def sommet(self):
        return self.data[-1]

    def depiler(self,element):
        return  self.data.pop(element)

"""
#Exercice 1
L = Pile()
for i in range(10):
    L2 = Pile.empiler(L,i)
print(L2)

L3 = Pile()
for i in range(Pile.hauteur(L)):
    a = Pile.sommet(L)
    L4 = Pile.empiler(L3,a)
    Pile.depiler(L,a)

print(L2)
print(L4)

#Exercice 2
L = Pile()
for i in range(10):
    L2 = Pile.empiler(L,i)

m = Pile.hauteur(L)//2
L3 = Pile()
for i in range(m):
    a = Pile.sommet(L)
    L4 = Pile.empiler(L3,a)
    Pile.depiler(L,a)
print(L2)
print(L4)

#Exercice 3
L = Pile()
for i in range(5):
    L2 = Pile.empiler(L,i)

L1 = Pile()
for i in range(5):
    L3 = Pile.empiler(L1,i-1)
print(L2)
print(L3)

m = Pile.hauteur(L)
LL = Pile()

for i in range(m):
    a = Pile.sommet(L)
    b = Pile.sommet(L1)
    L4 = Pile.empiler(LL,a)
    Pile.depiler(L,a)
    L4 = Pile.empiler(LL,b)
    Pile.depiler(L1,b)

print(L4)


#Exercice 4
import random

L = Pile()
for i in range(5):
    L2 = Pile.empiler(L,i)

L1 = Pile()
for i in range(5):
    L3 = Pile.empiler(L1,i)
print(L2)
print(L3)

m = Pile.hauteur(L)
LL = Pile()

while not Pile.hauteur(L) == 0:
    R = random.randint(1,2)

    if R == 1:
        a = Pile.sommet(L)
        b = Pile.sommet(L1)
        L4 = Pile.empiler(LL,a)
        Pile.depiler(L,a)
        L4 = Pile.empiler(LL,b)
        Pile.depiler(L1,b)
    if R ==2:
        for i in range(2):
            a = Pile.sommet(L)
            b = Pile.sommet(L1)
            L4 = Pile.empiler(LL,a)
            Pile.depiler(L,a)
            L4 = Pile.empiler(LL,b)
            Pile.depiler(L1,b)
print(L4)
"""


#Exercice 5


class File:
    def __init__(self):
        self.data = []


    def emfiler(self,element):
        self.data.append(element)
        return self.data

    def longueur(self):
        return len(self.data)

    def est_vide(self):
        return self.hauteur() == 00

    def sommet(self):
        return self.data[-1]

    def depiler(self):
        return  self.data.pop(0)

F = File()
F2 = File.emfiler(F,21)
F2 = File.emfiler(F,22)
F2 = File.emfiler(F,23)
N = File.depiler(F)
F2 = File.emfiler(F,24)
F2 = File.emfiler(F,25)
N = File.depiler(F)
print(N)
print(F2)

# N = 22, F = [23, 24, 25]