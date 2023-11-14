# from resdb import generateKeyForUser, createProfile

# loginDatabase = {}
loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
            "userId": "user"
        }
    }
userInfoDatabase = {}
userKeyPairDatabase = {}
user_cnt = 0

def getLoginInfo(email):
    if email not in loginDatabase:
        return False
    else:
        return loginDatabase[email]
    
def setLoginInfo(email, password):
    # public_key, private_key = generateKeyForUser()
    new_user = f'user{user_cnt}'
    loginDatabase[email] = {
        "password": password,
        "userId": new_user
    }
    userInfoDatabase[new_user] = {
        "email": email,
        # "publicKey":public_key
    }
    # userKeyPairDatabase[public_key] = private_key
    
def getUserInfo(userId):
    if userId not in userInfoDatabase:
        return False
    else:
        return userInfoDatabase[userId]

if __name__ == "__main__":
    loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
            "userId": "user"
        }
    }

    userInfoDatabase = {
        "user":{
                "email": "jack@gmail.com",
                "publicKey":"CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz",
                },
    }
    
    userKeyPairDatabase = {
        "CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz": "DZBpCfHDsQhvy9vLkcRKYskfSaXwrGQTfzzKVJTvzQN9"
    }