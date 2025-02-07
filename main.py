from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
import time
import random
Account.enable_unaudited_hdwallet_features()
rpc_url = "https://sepolia.infura.io/v3/ISI API INFURA"

web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

mnemonic_phrase = "Isi mnemonic disini"
private_key = Account.from_mnemonic(mnemonic_phrase)._private_key.hex()
account_address = Account.from_mnemonic(mnemonic_phrase).address




for i in range(1, 101):
    nonce = web3.eth.get_transaction_count(account_address)
    with open("wallets.txt", "r") as file:
        lines = file.readlines()
        receiver_address = random.choice(lines)

    receiver_address = receiver_address.strip()
    sum = random.uniform(0.00001, 0.0001)

    amount_to_send = Web3.to_wei(sum, 'ether')
    gwei = random.uniform(9, 15)
    transaction = {
        'nonce': nonce,
        'to': receiver_address,
        'value': amount_to_send,
        'gas': 21000,
        'gasPrice': web3.to_wei(gwei, 'gwei'),
        'chainId': 11155111
    }

    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(f'Nomor transaksi: {i}', "Transaksi terkirim. Hash transaksi:", web3.to_hex(tx_hash))

    
    while True:
        time.sleep(45)
        tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
        if tx_receipt is not None:
            if tx_receipt['status'] == 1:
                print("Transaksi Sukses Bang!")
                break
            else:
                print("Transaksi gagal.")
        else:
            print("Transaksi tersebut belum termasuk dalam blok.")
        
