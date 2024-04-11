from ajoutUtilFct import *
import hashlib
import random

def hach(mdp):
    bmdp = bytes(mdp, "utf-8")
    m = hashlib.sha256()
    m.update(bmdp)
    return m.hexdigest()

def salting(mdp, salt):
    hashed_password = hashlib.pbkdf2_hmac('sha256', mdp.encode('utf-8'), salt, 100000)
    return hashed_password

password = '123456789'
salt = random.getrandbits(16*8).to_bytes(16, 'little')
print(salting(password, salt))