def getUserLoginDatabase(email):
    if email not in loginDatabase:
        return False
    else:
        return loginDatabase[email]

def setUserLoginDatabase(email, password, new_user):
    loginDatabase[email] = {
        "password": password,
        "user_id": new_user
    } 

def getUserInfoDatabase(user_id):
    if user_id not in userInfoDatabase:
        return False
    else:
        return userInfoDatabase[user_id]

def setUserInfoDatabase(user_id, email = None, public_key = None, metadata = None):
    userInfoDatabase[user_id] = {}
    if email: userInfoDatabase[user_id]["email"] = email
    if public_key: userInfoDatabase[user_id]["public_key"] = public_key
    if metadata: userInfoDatabase[user_id]["metadata"] = metadata

def getUserKeyPairDatabase(public_key):
    if public_key not in userKeyPairDatabase:
        return False
    else:
        return userKeyPairDatabase[public_key]

def setUserKeyPairDatabase(public_key, private_key):
    if public_key in userKeyPairDatabase:
        return False
    else:
        userKeyPairDatabase[public_key] = private_key

loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
            "user_id": "user"
        }
    }
# loginDatabase = {}
userInfoDatabase = {}
userKeyPairDatabase = {}
userListDatabase = []

if __name__ == "__main__":
    loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
            "user_id": "user"
        }
    }

    userInfoDatabase = {
        "user":{
                "email": "jack@gmail.com",
                "public_key": "CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz",
                # "fulfilled_tx": "12345",
                "metadata": {"a": "b"}
                },
    }
    
    userKeyPairDatabase = {
        "CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz": "DZBpCfHDsQhvy9vLkcRKYskfSaXwrGQTfzzKVJTvzQN9"
    }

    userListDatabase = [
        {
            "name": "Jack",
            "title": "Software Engineer",
            "user_id": "user"
        },
        {
            "name": "Elliot",
            "title": "Software Engineer",
            "user_id": "userr"
        }
    ]