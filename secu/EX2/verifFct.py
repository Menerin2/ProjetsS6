import sqlite3

def Verification():
    connection = sqlite3.connect("donnees.db")
    curseur = connection.cursor()
    id = getId()
    mdp = getMdp()
    #tant que le login et le mot de passe ne correspondent à aucune entrée de la base de donnée, on demande à l'utilisateur d'en re-rentrer
    while checkAll(id, mdp, curseur):
        print("Mot de passe ou identifiant incorrect")
        id = getId()
        mdp = getMdp()
    #le login et le mot de passe correspondent à une entrée de la base de donnée
    print("Bravo ! Vous êtes connecté")
        
#fonction demandant à l'utilisateur de rentrer son login et le retourne
def getId():
    print("Connexion :\nEntrez votre identifiant")
    id = input()
    return id

#fonction demandant à l'utilisateur de rentrer son mot de passe et le retourne
def getMdp():
    print("Entrez votre mot de passe")
    mdp = input()
    return mdp

#fonction qui vérifie si le login et le mot de passe donné par l'utilisateur existent dans la base de donnée
def checkAll(id, mdp, curseur):
    res = curseur.execute("SELECT name FROM utilisateurs WHERE name = '" + id + "' AND password ='" + mdp +"'")
    return res.fetchone() is None