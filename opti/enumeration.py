import sys
from enumeration_fonction import *

fichierIn = open(sys.argv[1], "r")
nbClient = int(fichierIn.readline())
listeIngredient = []

listeIngredient = creaListeIngredtient(fichierIn, nbClient)
creaToutesPossibilites(listeIngredient)

fichierIn.close()