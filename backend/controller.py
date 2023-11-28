from resdb import generateKeyForUser, createProfile, modifyProfile, getProfile
from localdb import getUserLoginDatabase, setUserLoginDatabase, getUserInfoDatabase, setUserInfoDatabase, getUserListDatabase, getUserKeyPairDatabase, setUserKeyPairDatabase

def getUserLogin(email):
    return getUserLoginDatabase(email)
    
def setUserLogin(email, password):
    public_key, private_key = generateKeyForUser(email)
    setUserLoginDatabase(email, password)
    setUserInfoDatabase(email = email, public_key = public_key)
    setUserKeyPairDatabase(public_key, private_key)

def getUserInfoAll(email):
    user = getUserInfoDatabase(email)
    if "transaction_id" not in user:
        return None
    else:
        return getProfile(user['transaction_id'])
    
def getUserInfoCategory(email, category):

    user = getUserInfoDatabase(email)
    if "transaction_id" not in user:
        return None
    else:
        metadata = getProfile(user["transaction_id"])
        if category == "cover": return metadata["cover"]
        elif category == "experience": return metadata["experience"]
        elif category == "education": return metadata["education"]
        elif category == "skill": return metadata["skill"]
        elif category == "achievements": return metadata["achievements"]

def setUserInfoCategory(email, category, data):
    userInfo = getUserInfoDatabase(email)
    public_key = userInfo["public_key"]
    private_key = getUserKeyPairDatabase(public_key)
    print(f'setUserInfo public key: {public_key}, private key:{private_key}')
    previous_meta = None
    if "transaction_id" not in userInfo:
        transaction_id = createProfile(email, public_key, private_key)
    else:
        transaction_id = userInfo["transaction_id"]
        previous_meta = getProfile(transaction_id)
    if previous_meta == None:
        previous_meta = {}
    if category == "cover": previous_meta["cover"] = data
    if category == "experience": previous_meta["experience"] = data
    if category == "education": previous_meta["education"] = data
    if category == "skill": previous_meta["skill"] = data
    if category == "achievements": previous_meta["achievements"] = data
    metadata = previous_meta
    transaction_id = modifyProfile(public_key, private_key, metadata, transaction_id) 
    setUserInfoDatabase(email = email, transaction_id = transaction_id)

def getUserList():
    return getUserListDatabase()

if __name__ == "__main__":
    email = "elliot@gmail.com"
    password = "elliot"
    setUserLogin(email, password)
    #print(getUserLogin(email))
    cover = {"cover":"cover elliot"}
    education = {"education":"ucdavis"}
    #print(getUserInfo(email)[0])
    setUserInfo(email, cover)
    #print(getUserInfo(email))
