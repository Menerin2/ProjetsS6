def nbAime(choixIngredient, listeClient):
    cptAime=0
    for i in range(0, len(listeClient), 2):
        if(testAime(choixIngredient, listeClient[i]) and not testDeteste(choixIngredient, listeClient[i+1])):
            cptAime+=1
    return cptAime

def testAime(choixIngredient, clientAime):
    if all(ingredient in choixIngredient for ingredient in clientAime):
        return True
    return False

def testDeteste(choixIngredient, clientDeteste):
    if any(ingredient in clientDeteste for ingredient in choixIngredient):
        return True
    return False