import sqlite3

def AjoutUtilisateur():
    connection = sqlite3.connect("donnees.db")
    curseur = connection.cursor()
    #uncomment next line to create table utilisateurs
    #curseur.execute("CREATE TABLE utilisateurs ( name TEXT, password TEXT)")
    id = identification(curseur)
    #tant que le login est déjà utilisé, on demande à l'utilisateur de re-rentrer un login
    while id == "":
        print("L'identifiant est déjà utilisé ou invalide, veuillez en saisir un autre")
        id = identification(curseur)
    mdp = choixMdp()
    #tant que les deux entrées de l'utilisateurs ne correspondent pas, on lui demande de re-rentrer un mot de passe et de le confirmer
    while mdp == "":
        print("Vos entrées ne correspondent pas")
        mdp = choixMdp()
    #On ajoute l'utilisateur à la base de donnée
    addUtil(id, mdp, curseur)
    connection.commit()
    #on affiche l'intégralité des utilisateurs
    print("Liste des utilisateurs :")
    res = curseur.execute("SELECT * FROM utilisateurs")
    print(res.fetchall())

#fonction permmettant de récuperer le login rentré par l'utilisateur et vérifier qu'il n'existe pas déjà dans la base de donnée
def identification(curseur):
    id = choixId()
    if checkId(id, curseur):
        return id
    return ""

#fonction retournant le login rentré par l'utilisateur
def choixId():
    print("Choississez votre identitfiant :")
    id = input()
    return id

#fonction permmetant de vérifier si le login de l'utilisateur est déjà dans la base de donnée
def checkId(id, curseur):
    res = curseur.execute("SELECT name FROM utilisateurs WHERE name = '" + id + "'")
    #si on n'a trouvé aucun résultat, le login n'existe pas dans la base de donnée
    return res.fetchone() is None

#fonction demandant à l'utilisateur de rentrer 2 fois le même mot de passe, si les deux diffèrent la fonction renvoi un String vide
def choixMdp():
    print("choisissez votre mot de passe :")
    mdp = input()
    print("Validez votre mot de passe :")
    mdp2 = input()
    if mdp == mdp2:
        return mdp
    return ""

#fonction permettant d'ajouter un login et un mot de passe à la ase de donnée
def addUtil(id, mdp, curseur):
    curseur.execute("INSERT INTO utilisateurs VALUES('"+id+"','"+mdp+"')")