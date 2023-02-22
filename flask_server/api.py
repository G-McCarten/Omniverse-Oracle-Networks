from flask import Flask, request, jsonify
from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os

app = Flask(__name__)


@app.route("/api/omniverse/", methods=["POST"])
def omniverse():
    req = request.json  # Get the request body as a json object
    if req:
        print("object: ", req.get("object"))
        print("quantity: ", req.get("quantity"))
        print("timestamp: ", req.get("timestamp"))

        # Test updating the count of the storage variable.
        # transaction = simple_storage.update_count(req.get("quantity"), {"from": account})

        # How many blocks we want to wait for the transaction to be mined.
        # transaction.wait(1)
        # updated_stored_value = simple_storage.storage_count()
        # print(updated_stored_value)

        return jsonify({"message": "Success"})
    else:
        return jsonify({"ERROR": "POST request unsuccessful."})


@app.route("/")
def index():
    # A welcome message to test our server
    return "<h1>Welcome to the omniverse API.</h1>"


def get_storage_contract():
    return ""


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

    # -------------------- BLOCKCHAIN SETUP -------------------- #

    # # Read the Solidity file.
    # with open("./SimpleStorage.sol", "r") as file:
    #     # Read all the contents of the file and place it in the simple_storage_file variable.
    #     simple_storage_file = file.read()

    # # Before compile_standard() is called, the solcx package needs to be installed.
    # install_solc("0.6.0")

    # # Solidity source code
    # compiled_sol = compile_standard(
    #     {
    #         "language": "Solidity",
    #         "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
    #         "settings": {
    #             "outputSelection": {
    #                 "*": {
    #                     "*": [
    #                         "abi",
    #                         "metadata",
    #                         "evm.bytecode",
    #                         "evm.bytecode.sourceMap",
    #                     ]
    #                 }
    #             }
    #         },
    #     },
    #     solc_version="0.6.0",
    # )

    # with open("compiled_code.json", "w") as file:
    #     json.dump(compiled_sol, file)

    # # Get Bytecode
    # bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    #     "bytecode"
    # ]["object"]

    # # Get ABI
    # abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

    # # Connect to the Rinkeby test network.
    # w3 = Web3(
    #     Web3.HTTPProvider(
    #         "https://rinkeby.infura.io/v3/6ed21371abb441bfa11979474f0e3a6a"
    #     )
    # )
    # chain_id = 4  # Chain ID in Rinkeby.

    # private_key = os.getenv("PRIVATE_KEY")
    # print("private_key: ", private_key)

    # my_address = os.getenv("MY_ADDRESS")
    # print("my_address: ", my_address)

    # SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
    # # Get the latest transaction count. (This is the nonce)
    # nonce = w3.eth.getTransactionCount(my_address)

    # # When working with the contract, you need the Contract Address and the Contract ABI.
    # simple_storage = w3.eth.contract(address=get_storage_contract(), abi=abi)

    # -------------------- BLOCKCHAIN SETUP -------------------- #

    # Get the current state of the counter from the smart contract deployed.
