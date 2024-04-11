from itertools import combinations

def creaListeIngredtient(fichier, nbClient):
    listeIngredient = []
    for i in range(nbClient*2):
        ligne = fichier.readline()
        txt = ligne.split()
        for j in range(int(txt[0])):
            if txt[j+1] not in listeIngredient:
                listeIngredient.append(txt[j+1])
    return listeIngredient

def creaToutesPossibilites(listeIngredient):
    cpt = 0
    for i in range(0,len(listeIngredient)+1):
        for j in combinations(listeIngredient, i):
            print(j)
            cpt += 1
    print(cpt)
