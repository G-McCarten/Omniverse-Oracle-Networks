from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()

    # Deploys a contract and returns the contract instance.
    simple_storage = SimpleStorage.deploy({"from": account}, publish_source=True)
    print(account)

    stored_value = simple_storage.storage_count()
    print(stored_value)

    # Test updating the count of the storage variable.
    # transaction = simple_storage.update_count(1, {"from": account})

    # How many blocks we want to wait for the transaction to be mined.
    # transaction.wait(1)
    # updated_stored_value = simple_storage.storage_count()
    # print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    print("Deploying...")
    deploy_simple_storage()
    print("Done.")
