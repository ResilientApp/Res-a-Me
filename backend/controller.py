# from resdb import generateKeyForUser, createProfile
from localdb import getUserLoginDatabase, setUserLoginDatabase, getUserInfoDatabase, setUserInfoDatabase

user_cnt = 0

def getUserLogin(email):
    return getUserLoginDatabase(email)
    
def setUserLogin(email, password):
    new_user = f'user{user_cnt}'
    # public_key, private_key = generateKeyForUser()
    setUserLoginDatabase(email, password, new_user)
    setUserInfoDatabase(user_id = new_user, email = email)
    # userKeyPairDatabase[public_key] = private_key
    
def getUserInfo(user_id):
    return getUserInfoDatabase(user_id)

def setUserInfo(user_id, email):
    setUserInfoDatabase(user_id = user_id, email = email)

