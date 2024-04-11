import sqlite3

def AjoutUtilisateur():
  connection = sqlite3.connect("donnees.db")
  curseur = connection.cursor()
  #uncomment next line to create table utilisateurs
  #curseur.execute("CREATE TABLE utilisateurs ( name TEXT, password TEXT)")
  is_id_ok = False
  #tant que le login est déjà utilisé, on demande à l'utilisateur de re-rentrer un login
  while is_id_ok:
    print("Choississez votre identitfiant :")
    id = input()
    res = curseur.execute("SELECT name FROM utilisateurs WHERE name = '" + id + "'")
    #si on n'a trouvé aucun résultat, le login n'existe pas dans la base de donnée
    if res.fetchone() is None:
      is_id_ok = True
    else:
      print("L'identifiant est déjà utilisé ou invalide, veuillez en saisir un autre")
  is_mdp_ok = False
  #tant que les deux entrées de l'utilisateurs ne correspondent pas, on lui demande de re-rentrer un mot de passe et de le confirmer
  while is_mdp_ok:
    print("choisissez votre mot de passe :")
    mdp = input()
    print("Validez votre mot de passe :")
    mdp2 = input()
    if mdp == mdp2:
      is_mdp_ok = True
    else:
      print("Vos entrées ne correspondent pas")
  #On ajoute l'utilisateur à la base de donnée
  curseur.execute("INSERT INTO utilisateurs VALUES('"+id+"','"+mdp+"')")
  connection.commit()