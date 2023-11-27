def getUserLoginDatabase(email):
    if email not in loginDatabase:
        return False
    else:
        return loginDatabase[email]

def setUserLoginDatabase(email, password):
    loginDatabase[email] = {
        "password": password,
    } 

def getUserInfoDatabase(email):
    if email not in userInfoDatabase:
        return False
    else:
        return userInfoDatabase[email]

def setUserInfoDatabase(email, public_key = None):
    userInfoDatabase[email] = {}
    if public_key: userInfoDatabase[email]["public_key"] = public_key

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

def getUserListDatabase():
    return userListDatabase

def setUserListDatabase(email, name, position):
    new_user = {
        "email": email,
        "name": name,
        "position": position
    }
    userListDatabase.append(new_user)

loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
        }
    }
# # loginDatabase = {}
# userInfoDatabase = {}
# userKeyPairDatabase = {}
# userListDatabase = []
loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
        }
    }

userInfoDatabase = {
    "jack@gmail.com":{
        "public_key": "CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz",
        "transaction_id": "12342356"
        },
}
    
userKeyPairDatabase = {
    "CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz": "DZBpCfHDsQhvy9vLkcRKYskfSaXwrGQTfzzKVJTvzQN9"
}

userListDatabase = [
    {
        "email": "jack@gmail.com",
        "name": "Jack",
        "position": "Software Engineer"
    },
    {
        "email": "elliot@gmail.com",
        "name": "Elliot",
        "position": "Software Engineer"
    }
]
    