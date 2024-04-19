import sys
import random

from enumeration_fonction import *

taille_population = 100
proba_mutation = 1
nombre_de_generations = 10

def generer_recette_initiale(listeIngredients):
    return random.sample(listeIngredients, k=random.randint(1,len(listeIngredients)))

#fitnesse de la recette (score par rapport aux ingredients aimes par chaque client et par rapport a ceux detestés)
def fitness_recette(recette, liste_gouts_clients):
    score=0
    #print(recette)

    for aime, deteste in liste_gouts_clients:

        if all(ingredient in recette for ingredient in aime) and not any(ingredient in recette for ingredient in deteste):
            score+=1
        #print("----------------",aime,deteste,score)

    #print(score)
    return score

def crossover(parent1, parent2):
    #print("AAAAAAAA   ",parent1,parent2)
    taille_parent_minimum = min(len(parent1), len(parent2))
    if taille_parent_minimum > 1:
        point_de_crossover = random.randint(1, taille_parent_minimum-1)
    else:
        point_de_crossover = taille_parent_minimum
    enfant = parent1[:point_de_crossover] + parent2[point_de_crossover:]
    return enfant

def mutation(recette, listeIngredients, proba_mutation):
    for i in range(len(recette)):
        if random.random() < proba_mutation:
            recette[i] = random.choice(listeIngredients)
    return recette

def algo_genetique(listeIngredients, liste_gouts_clients, taille_population, proba_mutation, nombre_de_generations):
    population_listeRecettes = [generer_recette_initiale(listeIngredients) for _ in range(taille_population)]
    compteur_score_stagnant = 0
    compteur_generation = 0
    score_precedent = 0
    #recetteParfaite = False
    #bonneRecette = population_listeRecettes[0]

    #while recetteParfaite == False:
    while compteur_score_stagnant <15 and compteur_generation < nombre_de_generations:
        compteur_generation+=1

        #calcul des meilleurs elements
        listeScores = [fitness_recette(recette, liste_gouts_clients) for recette in population_listeRecettes]
        #print(listeScores)
        meilleureRecette = population_listeRecettes[listeScores.index(max(listeScores))]
        if score_precedent>=max(listeScores):
            compteur_score_stagnant+=1


        #selection des meilleurs elements (elitisme)
        taille_liste_recettesElues = int(taille_population/2)
        all_indices_recettesElues = sorted(range(len(listeScores)), key=lambda i:listeScores[i], reverse=True)
        indices_recettesElues=all_indices_recettesElues[:taille_liste_recettesElues]
        population_recettesElues = [population_listeRecettes[i] for i in indices_recettesElues]





        #realisation du crossover
        nouvelle_generation = []
        nouvelle_generation.append(population_recettesElues[0])
        while (len(nouvelle_generation)<taille_population):
            parent1, parent2 = random.choices(population_recettesElues, k=2)
            enfant = crossover(parent1,parent2)
            enfant = mutation(enfant, listeIngredients, proba_mutation)
            nouvelle_generation.append(enfant)


        population_listeRecettes = nouvelle_generation

    return meilleureRecette

def creer_dictionnaire_listes_gouts_ingredients(fichier,nbClient):

    listeIngredients = []
    liste_gouts = []

    for i in range(nbClient):
        aime = []
        deteste = []
        client = []
        ligne = fichier.readline()
        txt = ligne.split()
        for j in range(1,int(txt[0])+1):
            aime.append(txt[j])
            if txt[j] not in listeIngredients:
                listeIngredients.append(txt[j])

        ligne = fichier.readline()
        txt = ligne.split()
        for j in range(1,int(txt[0])+1):
            deteste.append(txt[j])
            if txt[j] not in listeIngredients:
                listeIngredients.append(txt[j])
        client.append(aime)
        client.append(deteste)
        liste_gouts.append(client)

    dict_listes_ingr_gouts = {'listeIngredients':listeIngredients, 'liste_gouts':liste_gouts}
    return dict_listes_ingr_gouts

def ecritureReponse(fichier, recette):
    fichier.write(str(len(recette)))
    for i in range(len(recette)):
        fichier.write(" " + recette[i])


fichierIn = open(sys.argv[1], "r")
fichierOut = open(sys.argv[2], "w")
nbClient = int(fichierIn.readline())


dictionnaire_listes = creer_dictionnaire_listes_gouts_ingredients(fichierIn,nbClient)

liste_gouts_clients = dictionnaire_listes['liste_gouts']
listeIngredients = dictionnaire_listes['listeIngredients']


meilleureRecette = algo_genetique(listeIngredients, liste_gouts_clients, taille_population, proba_mutation, nombre_de_generations)

ecritureReponse(fichierOut, meilleureRecette)

