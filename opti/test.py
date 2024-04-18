from fonctionTestScore import *

def product(*args, repeat=1):
    # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

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

fichier = open('c_grossier.txt')
nbClient = int(fichier.readline())
listeIngredient = []
listeClient = []
choixIngredient=["byyii", "dlust", "xdozp", "luncl", "vxglq", "xveqd", "tfeej"]
for i in range(nbClient):
    (listeIngredient, listeClient)=ajout(fichier, listeIngredient, listeClient, i)
    (listeIngredient, listeClient)=ajout(fichier, listeIngredient, listeClient, i)
print(nbAime(choixIngredient, listeClient))