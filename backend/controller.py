from resdb import generateKeyForUser, createProfile, modifyProfile, getProfile
from localdb import getUserLoginDatabase, setUserLoginDatabase, getUserInfoDatabase, setUserInfoDatabase, getUserListDatabase, getUserKeyPairDatabase, setUserKeyPairDatabase

def getUserLogin(email):
    return getUserLoginDatabase(email)
    
def setUserLogin(email, password):
    public_key, private_key = generateKeyForUser(email)
    setUserLoginDatabase(email, password)
    setUserInfoDatabase(email = email, public_key = public_key)
    setUserKeyPairDatabase(public_key, private_key)
    
def getUserInfo(email, cover = None, experience = None, education = None, skill = None, achievements = None):
    user = getUserInfoDatabase(email)
    if "transaction_id" not in user:
        return None
    else:
        metadata = getProfile(user["transaction_id"])
        if cover: return metadata["cover"]
        if experience: return metadata["experience"]
        if education: return metadata["education"]
        if skill: return metadata["skill"]
        if achievements: return metadata["achievements"]

def setUserInfo(email, cover = None, experience = None, education = None, skill = None, achievements = None):
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
    if cover: previous_meta["cover"] = cover["cover"]
    if experience: previous_meta["experience"] = experience["experience"]
    if education: previous_meta["education"] = education["education"]
    if skill: previous_meta["skill"] = skill["skill"]
    if achievements: previous_meta["achievements"] = achievements["achievements"]
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
