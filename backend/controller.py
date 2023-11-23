# from resdb import generateKeyForUser, createProfile, modifyProfile, getProfile
from localdb import getUserLoginDatabase, setUserLoginDatabase, getUserInfoDatabase, setUserInfoDatabase, getUserListDatabase

def getUserLogin(email):
    return getUserLoginDatabase(email)
    
def setUserLogin(email, password):
    # public_key, private_key = generateKeyForUser()
    setUserLoginDatabase(email, password)
    setUserInfoDatabase(email = email)
    # userKeyPairDatabase[public_key] = private_key
    
def getUserInfo(email):
    user = getUserInfoDatabase(email)
    info = {}
    #info = getProfile(user["transaction_id"])
    return info

def setUserInfo(email, about = False, experience = False, education = False, skill = False, achievements = False):
    setUserInfoDatabase(email = email)

def getUserList():
    return getUserListDatabase()
    

