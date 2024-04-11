import sqlite3
import hashlib
import random

def creaUtil():
  connection = sqlite3.connect("donnees.db")
  curseur = connection.cursor()
  curseur.execute("CREATE TABLE utilisateurs ( name TEXT, password TEXT)")

def AjoutUtilisateur():
  connection = sqlite3.connect("donnees.db")
  curseur = connection.cursor()
  is_id_incorrect = True
  #tant que le login est deja utilise, 
  #on demande a l'utilisateur de re-rentrer un login
  while is_id_incorrect:
    print("Choississez votre identitfiant :")
    id = input()
    res = curseur.execute("SELECT name FROM utilisateurs WHERE name = '"+id+"'")
    #si on n'a trouve aucun resultat, 
    #le login n'existe pas dans la base de donnee
    if res.fetchone() is None:
      #on sort de la boucle
      is_id_incorrect = False
    else:
      #on redemande son identifiant a l'utilisateur
      print("L'identifiant est deja utilise, veuillez en saisir un autre")
  is_mdp_incorrect = True
  #tant que les deux entrees de l'utilisateurs ne correspondent pas, 
  #on lui demande de re-rentrer un mot de passe et de le confirmer
  while is_mdp_incorrect:
    print("choisissez votre mot de passe :")
    mdp = input()
    print("Validez votre mot de passe :")
    mdp2 = input()
    #si les deux entrees correspondent
    if mdp == mdp2:
      #on sort de la boucle
      is_mdp_incorrect = False
    else:
      print("Vos entrees ne correspondent pas")
  return [id, mdp]
 
def addUtilBDD(ids):
  connection = sqlite3.connect("donnees.db")
  curseur = connection.cursor()
  curseur.execute("INSERT INTO utilisateurs VALUES('"+ids[0]+"','"+ids[1]+"')")
  connection.commit()

def printUtil():
  connection = sqlite3.connect("donnees.db")
  curseur = connection.cursor()
  res = curseur.execute("SELECT * FROM utilisateurs")
  print(res.fetchall())

def Verification():
  connection = sqlite3.connect("donnees.db")
  curseur = connection.cursor()
  print("Connexion :")
  is_not_connected = True
  #tant que le login et le mot de passe ne correspondent a aucune entree de la base de donnee, on demande a l'utilisateur d'en re-rentrer
  while is_not_connected:
    print("Entrez votre identifiant")
    id = input()
    print("Entrez votre mot de passe")
    mdp = input()
    res = curseur.execute("SELECT name FROM utilisateurs WHERE name = '" + id + "' AND password ='" + mdp +"'")
    if res.fetchone() is None:
      print("Mot de passe ou identifiant incorrect")
    #le login et le mot de passe correspondent a une entree de la base de donnee
    else:
      is_not_connected = False
  print("Bravo ! Vous etes connecte")

def hachage(ids):
  bmdp = bytes(ids[1], "utf-8")
  m = hashlib.sha256()
  m.update(bmdp)
  ids[1] = m.hexdigest()
  return ids

def hachageSalage(ids, salt):
    bmdp = bytes(ids[1], "utf-8")
    bsalt = bytes(salt, "utf-8")
    hashed_password = hashlib.pbkdf2_hmac('sha256', bmdp, bsalt, 100000)
    ids[1] = hashed_password
    return ids

def randomHachageSalage(ids):
    bmdp = bytes(ids[1], "utf-8")
    salt = random.getrandbits(16*8).to_bytes(16, 'little')
    hashed_password = hashlib.pbkdf2_hmac('sha256', bmdp, salt, 100000)
    ids[1] = hashed_password
    connection = sqlite3.connect("donnes.db")
    curseur = connection.cursor()
    curseur.execute("INSERT INTO sels VALUES('"+ids[0]+"','"+salt+"')")
    connection.commit()
    return ids

password = '123456789'
print(randomHachageSalage(["leo", "hehe"]))