from itertools import combinations
import sys

#récupération des données dans un fichier
def lecture_fichier(fichier):
    data = []
    with open(fichier, "r") as f:
        data = f.readlines()     
    data = [l.strip().split() for l in data]
    return data

#création d'une liste d'ingrédient sans doublon
def getListeIngredient(data):
    liste = []
    for l in data:
        for i in range(1,len(l)):
            if(l[i] not in liste):
                liste.append(l[i])
    return liste


def choix_meilleur(liste, data):
    best = liste
    bestscore = 0
    score = 0
    con = 0
    for i in range(len(liste), 0, -1):
        #on teste toutes les combinaisons d'ingredients de taille i    
        for j in combinations(liste, i):
            #pour chaque client 
            for cpt in range(1, len(data), 2):
                #si aucun ingrédient de j n'est deteste par le client
                if(len(list(set(j).intersection(data[cpt+1]))) == 0):
                    #si j contient tous les ingrédients aime par le client
                    if(len(list(set(j).intersection(data[cpt])))+1 == len(data[cpt])):
                        score += 1
                con +=1
                print(con)
            if score >= bestscore:
                best = j
                bestscore = score
            score = 0
    return best

#ecrit dans un fichier la réponse trouvée selon les standards du sujet
def ecritureReponse(fichier, listeIngredient):
    with open(fichier, "w") as fichOut:
        fichOut.write(str(len(listeIngredient)))
        for i in range(len(listeIngredient)):
            fichOut.write(" " + listeIngredient[i])



data = lecture_fichier(sys.argv[1])
liste = getListeIngredient(data)
best = choix_meilleur(liste, data)
ecritureReponse(sys.argv[2], best)
