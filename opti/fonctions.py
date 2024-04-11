def lectureIngredient(fichier, listeIngredient, aime, deteste, isAime):
    ligne = fichier.readline()
    txt = ligne.split()
    for j in range(int(txt[0])):
        ingredientIncremente(listeIngredient, aime, deteste, txt[j+1], isAime)

def ingredientIncremente(listeIngredient, aime, deteste, ingredient, isAime):
    if ingredient not in listeIngredient:
        listeIngredient.append(ingredient)
        if isAime:
            aime.append(1)
            deteste.append(0)
        else:
            aime.append(0)
            deteste.append(1)
    else:
        indexIngredient = listeIngredient.index(ingredient)
        if isAime:
            incrementeAimeDeteste(aime, indexIngredient)
        else: 
            incrementeAimeDeteste(deteste, indexIngredient)

def incrementeAimeDeteste(incrementIngredient, indexIngredient):
    incrementIngredient[indexIngredient] = incrementIngredient[indexIngredient] + 1

def choixIngredient(listeIngredient, aime, deteste):
    print(listeIngredient)
    print(aime)
    print(deteste)
    choix = []
    for i in range(len(listeIngredient)):
        if aime[i] > 0 and deteste[i] <= 1:
            choix.append(listeIngredient[i])
    return choix

def ecritureReponse(fichier, listeIngredient):
    fichier.write(str(len(listeIngredient)))
    for i in range(len(listeIngredient)):
        fichier.write(" " + listeIngredient[i])
