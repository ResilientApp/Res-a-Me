# from resdb import generateKeyForUser, createProfile, modifyProfile, getProfile
from localdb import getUserLoginDatabase, setUserLoginDatabase, getUserInfoDatabase, setUserInfoDatabase, getUserListDatabase
import shutil
import os
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

def updateUserResume(email): # This function is for the resume page, which will send the whole resume data
    source_dir = f'resumes/{email}'
    target_dir = '../frontend/public/data/sections'

    if not os.path.exists(source_dir): # No resume found for this email
        return False

    for filename in os.listdir(source_dir):
        if filename.endswith('.json'):
            shutil.copy(os.path.join(source_dir, filename), target_dir)
    
    return True

