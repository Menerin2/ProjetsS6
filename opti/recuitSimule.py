import random
from fonctionTestScore import *

def ajout(fichier, listeIngredient, listeClient, cpt):
    ligne = fichier.readline()
    txt = ligne.split()
    client = []
    client.append(cpt)
    for j in range(int(txt[0])):
        client.append(txt[j+1])
        if txt[j+1] not in listeIngredient:
            listeIngredient.append(txt[j+1])
    listeClient.append(client)
    return listeIngredient, listeClient

def getFirstIteration(listeIngredient):
    choixIngredient = []
    for i in range(random.randint(0, len(listeIngredient))):
        ingredient = listeIngredient[random.randint(0, len(listeIngredient)-1)]
        while ingredient in choixIngredient:
            ingredient = listeIngredient[random.randint(0, len(listeIngredient)-1)]
        choixIngredient.append(ingredient)
    return choixIngredient

def getModif(listeIngredient, choixIngredient):
    choix = random.randint(0, 2)
    if(choix == 0):
        if(len(choixIngredient) != 0):
            choixIngredient.pop(random.randint(0, len(choixIngredient)-1))
    if(choix == 1):
        if(len(choixIngredient) != 0):
            choixIngredient.pop(random.randint(0, len(choixIngredient)-1))
        newIngredient = listeIngredient[random.randint(0, len(listeIngredient)-1)]
        while newIngredient in choixIngredient:
                newIngredient = listeIngredient[random.randint(0, len(listeIngredient)-1)]
        choixIngredient.append(newIngredient)
    if(choix == 2):
        if(len(listeIngredient)!=len(choixIngredient)):
            ingredient = listeIngredient[random.randint(0, len(listeIngredient)-1)]
            while ingredient in choixIngredient:
                ingredient = listeIngredient[random.randint(0, len(listeIngredient)-1)]
            choixIngredient.append(ingredient)
    return choixIngredient


def get100Iteration(listeIngredient, listeClient):
    listeScore = []
    choixIngredient = getFirstIteration(listeIngredient)
    listeScore.append(nbAime(choixIngredient, listeClient))
    for i in range(99):
        choixIngredient = getModif(listeIngredient, choixIngredient)
        listeScore.append(nbAime(choixIngredient, listeClient))
    return listeScore, choixIngredient

def moyenne(score):
    var = []
    for i in range(len(score)-2):
        var.append(abs(score[i]-score[i+1]))
    return (sum(var))/len(var)

def perturbation(listeIngredient, choixIngredient, listeClient):
    choixTemp = choixIngredient.copy()
    choixTemp = getModif(listeIngredient, choixTemp)
    if(nbAime(choixIngredient, listeClient) < nbAime(choixTemp, listeClient)):
        return choixTemp, True
    return choixIngredient, False

fichier = open('e_elabore.txt')
nbClient = int(fichier.readline())
listeIngredient = []
listeClient = []
for i in range(nbClient):
    (listeIngredient, listeClient)=ajout(fichier, listeIngredient, listeClient, i)
    (listeIngredient, listeClient)=ajout(fichier, listeIngredient, listeClient, i)
(score, choixIngredient) = get100Iteration(listeIngredient, listeClient)
accept = 0
tented = 0
print(12*len(listeIngredient), 100*len(listeIngredient))
while accept < 12*20 and tented < 100*20:
    (choixIngredient, isBetter) = perturbation(listeIngredient, choixIngredient, listeClient)
    if isBetter:
        accept+=1
    tented+=1
    print(accept, tented)
print(nbAime(choixIngredient, listeClient))
