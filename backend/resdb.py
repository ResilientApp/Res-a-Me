from resdb_driver import Resdb
from resdb_driver.transaction import Transaction
from copy import deepcopy

db_root_url = "https://resdb.free.beeceptor.com"

db = Resdb(db_root_url)
from resdb_driver.crypto import generate_keypair

def generateKeyForUser(user):
    public_key, private_key = generate_keypair()
    return public_key, private_key

def createProfile(user, public_key, private_key, metadata):
    Profile = {
        "owner": {
            "token_for": user,
            "description": "user's profile",
        }
    }
    prepared_token_tx = db.transactions.prepare(
        operation="CREATE",
        signers=public_key,
        recipients=[([public_key], 1)],
        asset=Profile,
    )

    prepared_token_tx["metadata"] = metadata #metadata has to be a dict 
    fulfilled_token_tx = db.transactions.fulfill(
        prepared_token_tx, private_keys=private_key
    )
    sent_token_tx = db.transactions.send_commit(fulfilled_token_tx)
    return fulfilled_token_tx, sent_token_tx

def modifyProfile(public_key, private_key, metadata, userInfo):
    fulfilled_token_tx = userInfo["fulfilled_token_tx"]

    transfer_asset = userInfo["fulfilled_token_tx"]["id"]
    output_index = 0
    transfer_asset = {"id": fulfilled_token_tx["id"]}
    output_index = 0
    output = fulfilled_transfer_tx["outputs"][output_index]
    transfer_input = {
        "fulfillment": output["condition"]["details"],
        "fulfills": {"output_index": output_index, "transaction_id": fulfilled_transfer_tx["id"]},
        "owners_before": output["public_keys"],
    }
    prepared_transfer_tx = db.transactions.prepare(
        operation="TRANSFER",
        asset=transfer_asset,
        inputs=transfer_input,
        metadata=metadata,
        recipients=[([public_key], 1)],
    )
    fulfilled_transfer_tx = db.transactions.fulfill(
        prepared_transfer_tx, private_keys=private_key
    )
    sent_transfer_tx = db.transactions.send_commit(fulfilled_transfer_tx)
    return sent_transfer_tx

if __name__ == "__main__":
    alice, bob = generate_keypair(), generate_keypair()