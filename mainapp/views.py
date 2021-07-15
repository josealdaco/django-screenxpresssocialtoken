from django.shortcuts import render
from django.http import HttpResponse
from . import views
from web3 import Web3
import os
# Create your views here.

def mainapp(request):
    return render(request,"homepage.html",{})
INFURA_KEY = os.environ.get("INFURA_KEY")
w3 = Web3(Web3.HTTPProvider(f'https://rinkeby.infura.io/v3/{INFURA_KEY}'))  # We are gonna interact with rikeby network
from web3.middleware import geth_poa_middleware
import tweepy

w3.middleware_onion.inject(geth_poa_middleware, layer=0)
api_consumer_key = os.environ.get("api_consumer_key")
api_consumer_secret_key = os.environ.get("api_consumer_secret_key")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
privateKey=os.environ.get("privateKey")
owner_address = os.environ.get("owner_address")
acct = w3.eth.account.privateKeyToAccount(privateKey)
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(api_consumer_key , api_consumer_secret_key)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

abi="""[
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": false,
      "inputs": [
        {
          "indexed": true,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": true,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": false,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        }
      ],
      "name": "allowance",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "subtractedValue",
          "type": "uint256"
        }
      ],
      "name": "decreaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "addedValue",
          "type": "uint256"
        }
      ],
      "name": "increaseAllowance",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "recipient",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "recipient",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "decimals",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "user",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "mintUserReward",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]"""

KEY_PHRASE = "screenxpress"
def send_token(request):
    if request.method != "POST":
        return HttpResponse("Server Error",status=404)

    TweetUrl = request.POST.get("tweet-url")
    if TweetUrl is None or  TweetUrl == "":
        return render(request, "homepage.html", {"error": "MUST HAVE A VALID TWITTER URL" })
    url = TweetUrl
    id = url.split('/')[-1]
    # the ID of the status
    # fetching the status
    status = None
    try:
        status = api.get_status(id)
    except Exception:
        """ Error wil either api or invalid url """
        return render(request, "homepage.html", {"error": "Detected invalid url" })
    # fetching the text attribute
    text = status.text
    if KEY_PHRASE not in text.lower():
        return render(request, "homepage.html", {"error": "YOU MUST HAVE ScreenXpress somewhere in your post to recieve a token" })
    # Now search for address
    is_address = text.find("0x")
    if is_address == -1:
        render(request, "homepage.html", {"error": "Detected invalid url" })
    else:
        """found address"""
        # address = text[is_address:39]
        address = text[is_address:].split("\n")[0]

        print("address: ", address)
        try:
            deployed_contract = w3.eth.contract(address="0x90b7E6fd704767740eb67900f3ac90B6BdFAF5F0",abi=abi)
            nonce = w3.eth.get_transaction_count(owner_address)
            new_mint = deployed_contract.functions.mintUserReward(address, 1).buildTransaction({
            'gas': 2000000,
            'nonce': nonce,
            'chainId': 4,

            })
            signed_txn = w3.eth.account.sign_transaction(new_mint, private_key=privateKey)
            w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            return render(request, 'congratulatePage.html', {})
        except Exception as error:
            print("error", str(error))
            return render(request, "homepage.html", {"error": "Detected invalid url" })
