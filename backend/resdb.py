from ResilientDB_GraphQL.resdb_driver import Resdb
from ResilientDB_GraphQL.resdb_driver.transaction import Transaction
#from ResilientDB_GraphQL.copy import deepcopy
from ResilientDB_GraphQL.resdb_driver.crypto import generate_keypair

db_root_url = "http://127.0.0.1:18000"
db = Resdb(db_root_url)

def generateKeyForUser(user = None):
    public_key, private_key = generate_keypair()
    return public_key, private_key

def createProfile(email, public_key, private_key):
    Profile = {
        "data": {
            "token_for": email,
            "description": "user's profile",
        }
    }
    prepared_token_tx = db.transactions.prepare(
        operation="CREATE",
        signers=public_key,
        recipients=[([public_key], 1)],
        asset=Profile,
    )

    fulfilled_tx = db.transactions.fulfill(
        prepared_token_tx, private_keys=private_key
    )
    sent_token_tx = db.transactions.send_commit(fulfilled_tx)
    return sent_token_tx[4:]

def modifyProfile(public_key, private_key, metadata, transaction_id):
    fulfilled_tx = db.transactions.retrieve(txid=transaction_id)

    transfer_asset = {"id": fulfilled_tx["id"]}
    output_index = 0
    output = fulfilled_tx["outputs"][output_index]
    transfer_input = {
        "fulfillment": output["condition"]["details"],
        "fulfills": {"output_index": output_index, "transaction_id": fulfilled_tx["id"]},
        "owners_before": output["public_keys"],
    }
    prepared_transfer_tx = db.transactions.prepare(
        operation="TRANSFER",
        asset=transfer_asset,
        inputs=transfer_input,
        metadata=metadata,
        recipients=[([public_key], 1)],
    )
    fulfilled_tx = db.transactions.fulfill(
        prepared_transfer_tx, private_keys=private_key
    )
    sent_transfer_tx = db.transactions.send_commit(fulfilled_tx)
    return sent_transfer_tx[4:]

def getProfile(transaction_id):
    data = db.transactions.retrieve(txid = transaction_id)
    if "metadata" not in data:
        return None
    else:
        return data["metadata"]

if __name__ == "__main__":
    alice, bob = generate_keypair(), generate_keypair()
