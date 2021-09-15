#Algo minimum

L= []
min = L[0]
for item in L:
    if item < min :
        min = item

#Tri par sélection

L= []
N = len(L)
for i in range(N):
    min = L[i]
    i_min = i
    for j in range(i, N):
        if L[j] < min:
            min= L[j]
            i_min = j
    tmp = L[i]
    L[i] = min
    L[i_min] = tmp
print("Liste triée: ", L)


# Tri par insertion

L = []
for i in range(1, len(L)):
    val = L[i]
    j = i - 1
    while L[j] > val and j >=0:
        L[j+1] = L[j]
        L[j] = val
        j = j - 1
print(L)