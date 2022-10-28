#!/usr/bin/python
'''
/*
 * @File: web3_transactionvalidator.py
 * @Author: Arunkumar Sadasivan
 * @Date: 04/05/2018
 * @Description: Clone all repo's that belong to a group or organization. Repo's can be segregated based on the branch.
 * @Usage: python3 web3_transactionvalidator.py -c <contract address> -k <etherscan apikey> -v <code to validate>
 * @Dependencies: python3 -m pip install web3
 */
'''

import json
import requests
from web3 import Web3
import argparse

# middleware required to avoid this error when not using mainnet: web3.exceptions.ExtraDataLengthError:
# The field extraData is 97 bytes, but should be 32. It is quite likely that you are connected to a POA chain.
from web3.middleware import geth_poa_middleware


# Get all transactions executed for a particular contract address
def getTransactionHistory(blockchainURL, contract_address, etherscan_apiKey):
    url = f"{blockchainURL}?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999" \
          f"&sort=asc&apikey={etherscan_apiKey}"
    try:
        response = requests.get(url)
        return response.json()["result"]
    except (
            requests.exceptions.HTTPError, requests.exceptions.ConnectTimeout,
            requests.exceptions.ConnectionError) as e:
        print(e)


'''
 * Contract Application Binary Interface (ABI) is the standard method of interacting with contracts in the Ethereum ecosystem,
 * both from outside the blockchain and for contract-to-contract interaction.
 * Data is encoded according to its type, as described in this specification.
'''


def getABI(blockchainURL, contract_address, etherscan_apiKey):
    abi_endpoint = f"{blockchainURL}?module=contract&action=getabi&address={contract_address}&apikey={etherscan_apiKey}"
    abi = json.loads(requests.get(abi_endpoint).text)
    return abi


def getWeb3Contract(nodeURL, contract_address, abi):
    # A provider is the interface that web3 uses to talk to the blockchain.
    # web3 = Web3(Web3.HTTPProvider(nodeURL))

    # middleware required to avoid this error when not using mainnet: web3.exceptions.ExtraDataLengthError:
    # The field extraData is 97 bytes, but should be 32. It is quite likely that you are connected to a POA chain.
    web3 = Web3(Web3.HTTPProvider(nodeURL))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # log if we're connected or not
    if web3.isConnected():
        print("[Info] Web3 Connection Successful.")
    else:
        print("[Error] Web3 Connection Unsuccessful.")

    # print(web3.eth.get_block('latest'))

    # Create Web3 contract object to interact with smart contract on the Ethereum blockchain.
    contract = web3.eth.contract(address=contract_address, abi=abi["result"])
    return contract


def getInputData(blockchainURL, nodeURL, contract_address, abi, etherscan_apiKey, functionName):
    transaction_history = getTransactionHistory(blockchainURL, contract_address, etherscan_apiKey)
    contract = getWeb3Contract(nodeURL, contract_address, abi)
    inputDataArry = []
    #print(transaction_history)
    for transactions in transaction_history:
        print(transactions)
        funcName = transactions['functionName']
        if functionName == funcName:
            # Decode input data
            func_obj, func_params = contract.decode_function_input(transactions["input"])
            print(func_params)
            data = func_params.get('data')
            inputDataArry.append(data.decode('utf-8'))  # bytes to string
    return inputDataArry


# check if code exists in transaction
def validateCode(inputDataArry, code):
    if code in inputDataArry:
        return True
    return False


###############################################################################
# Main
###############################################################################
def main(args):
    contract_address = args.contract
    blockchainURL = args.blockchainurl  # blockchain network URL
    nodeURL = args.nodeurl
    etherscanapikey = args.etherscanapikey
    code = args.validate

    if not blockchainURL:
        blockchainURL = "https://api-testnet.polygonscan.com/api"  # Polgon Testnet
    if not nodeURL:
        nodeURL = "https://polygon-testnet.public.blastapi.io"
        # nodeURL = "https://polygon-mumbai.g.alchemy.com/v2/<apikey>"  # alchemy node URL
        # infura node URL: "https://mainnet.infura.io/v3/<apikey>"

    functionName = f'safeTransferFrom(address from, address to, uint256 tokenId, bytes _data)'
    abi = getABI(blockchainURL, contract_address, etherscanapikey)
    inputDataArry = getInputData(blockchainURL, nodeURL, contract_address, abi, etherscanapikey, functionName)

    if args.data:
        print(inputDataArry)
    if args.validate:
        print(f" Code Exists: {validateCode(inputDataArry, code)}")


if __name__ == "__main__":
    def help_formatter(prog):
        r"Widen the text that is printed when the app is invoked with --help"
        args = dict(max_help_position=60, width=120)
        return argparse.HelpFormatter(prog, **args)


    parser = argparse.ArgumentParser(formatter_class=help_formatter)
    parser.add_argument("-c", "--contract", default=None,
                        required=True,
                        help="Contract Address")
    parser.add_argument("-k", "--etherscanapikey", default=None,
                        required=True,
                        help="Etherscan API Key")
    parser.add_argument("-u", "--blockchainurl", default=None,
                        required=False,
                        help="Blockchain Network URL")
    parser.add_argument("-n", "--nodeurl", default=None,
                        required=False,
                        help="Node URL (EX: Infura or Alchemy")
    parser.add_argument("-v", "--validate", default=None,
                        required=False,
                        help="Check if code exists as part of data bytes in transaction.")
    parser.add_argument("-d", "--data", action="store_true",
                        required=False,
                        help="Returns an array of data bytes in transaction.")

    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        pass
