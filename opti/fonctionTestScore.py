def nbAime(choixIngredient, listeClient):
    cptAime=0
    for i in range(0, len(listeClient), 2):
        if(testAime(choixIngredient, listeClient[i]) and not testDeteste(choixIngredient, listeClient[i+1])):
            cptAime+=1
    return cptAime

def testAime(choixIngredient, clientAime):
    cpt = 0
    for ingredient in clientAime:
        if(ingredient in choixIngredient):
            cpt +=1
    if(cpt == len(clientAime)-1):
        return True
    return False

def testDeteste(choixIngredient, clientDeteste):
    for ingredient in clientDeteste:
        if(ingredient in choixIngredient):
            return True
    return False