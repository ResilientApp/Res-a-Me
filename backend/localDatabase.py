# loginDatabase = {}
loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
            "userId": "user0"
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
    
def getUserInfo(userId):
    if userId not in userInfoDatabase:
        return False
    else:
        return userInfoDatabase[userId]

if __name__ == "__main__":
    loginDatabase = {
        "jack@gmail.com":{
            "password": "jackjack",
            "userId": "user0"
        }
    }

    userInfoDatabase = {
        "user0":{
                "email": "jack@gmail.com",
                "publicKey":"CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz",
                "transactionId":[]
                },

    }
    
    userKeyPairDatabase = {
        "CX62ckRaUucsVi3cbxCkSAcxR7zsBBNSPPrEHz26X4vz": "DZBpCfHDsQhvy9vLkcRKYskfSaXwrGQTfzzKVJTvzQN9"
    }