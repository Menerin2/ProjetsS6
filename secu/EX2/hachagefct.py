from ajoutUtilFct import *
import hashlib

def hach(mdp):
    bmdp = bytes(mdp, "utf-8")
    m = hashlib.sha256()
    m.update(bmdp)
    return m.hexdigest()

def salt(mdp, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', mdp.encode('utf-8'), salt, 100000)
    return hashed_password

mdp = "123456789"
sal = "Ceci est mon sel"
hashed_password = hashlib.pbkdf2_hmac('sha256', mdp.encode('utf-8'), salt, 100000)
print(hashed_password)