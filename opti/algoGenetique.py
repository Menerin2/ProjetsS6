import sys
import random
from enumeration_fonction import *

taille_population = 100
proba_mutation = 1
nombre_de_generations = 1000

def generer_recette_initiale(listeIngredients):
    return random.sample(listeIngredients, k=random.randint(1,len(listeIngredients)))

#fitnesse de la recette (score par rapport aux ingredients aimes par chaque client et par rapport a ceux detestés)
def fitness_recette(recette, liste_gouts_clients):
    score=0
    for aime, deteste in liste_gouts_clients:
        if all(ingredient in recette for ingredient in aime) and not any(ingredient in recette for ingredient in deteste):
            ingredients_aimes_dans_recette = [ingredient for ingredient in aime if ingredient in recette]
            score += len(ingredients_aimes_dans_recette) / max(1, len(aime))
    return score


def crossover(parent1, parent2):
    point_de_crossover = random.randint(1, min(len(parent1), len(parent2)) - 1)
    enfant = parent1[:point_de_crossover] + parent2[point_de_crossover:]
    return enfant

def mutation(recette, listeIngredients, proba_mutation):
    for i in range(len(recette)):
        if random.random() < proba_mutation:
            recette[i] = random.choice(listeIngredients)
    return recette

def algo_genetique(listeIngredients, liste_gouts_clients, taille_population, mutation):
    population_listeRecettes = [generer_recette_initiale(listeIngredients) for x in range(taille_population)]
    #recetteParfaite = False
    bonneRecette = population_listeRecettes[0]

    #while recetteParfaite == False:
    for generations in range(nombre_de_generations):

        #calcul des meilleurs elements
        listeScores = [fitness_recette(recette, liste_gouts_clients) for recette in population_listeRecettes]
        meilleureRecette = population_listeRecettes[listeScores.index(max(listeScores))]

        #selection des meilleurs elements
        taille_liste_recettesElues = taille_population/2
        indices_recettesElues = sorted(range(taille_population), key=lambda i:listeScores[i], reverse=True)[:taille_liste_recettesElues]
        population_recettesElues = [population_listeRecettes[i] for i in indices_recettesElues]

        #realisation du crossover
        nouvelle_generation = []
        while len(nouvelle_generation<taille_population):
            parent1, parent2 = random.choices(population_recettesElues, k=2)
            enfant = crossover(parent1,parent2)
            enfant = mutation(enfant, listeIngredients, proba_mutation)
            nouvelle_generation.append(enfant)


        population_listeRecettes = nouvelle_generation

    return meilleureRecette

#meilleureRecette = algo_genetique(listeIngredients, liste_gouts_clients, taille_population, proba_mutation, nombre_de_generations)

