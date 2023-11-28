# from resdb import generateKeyForUser, createProfile, modifyProfile, getProfile
from localdb import getUserLoginDatabase, setUserLoginDatabase, getUserInfoDatabase, setUserInfoDatabase, getUserListDatabase
import json
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

def setUserInfo(email):
    setUserInfoDatabase(email = email)

def getUserList():
    return getUserListDatabase()

def getUserResume(email, category): # This function is for the edit page, which will ask for the resume data for a specific category
    with open(f'resumes/{email}/{category}.json', 'r') as f:
        data = json.load(f)
    return data
    
def setUserResume(email, category, data): # This function is for the edit page, which will send the resume data for a specific category
    with open(f'resumes/{email}/{category}.json', 'w') as f:
        for item in json.loads(data):
            json.dump(item, f, indent=4)

