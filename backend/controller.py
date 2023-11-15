# from resdb import generateKeyForUser, createProfile
from localdb import getUserLoginDatabase, setUserLoginDatabase, getUserInfoDatabase, setUserInfoDatabase

user_cnt = 0

def getUserLogin(email):
    return getUserLoginDatabase(email)
    
def seUserLogin(email, password):
    new_user = f'user{user_cnt}'
    # public_key, private_key = generateKeyForUser()
    setUserLoginDatabase(email, password, new_user)
    setUserInfoDatabase(new_user, email)
    # userKeyPairDatabase[public_key] = private_key
    
def getUserInfo(user_id):
    return getUserInfoDatabase(user_id)

def setUserInfo(user_id, email):
    setUserInfoDatabase(new_user, email)

