#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is used to demo features on Wallet module

Author: DxChain Team
Created at: 20181212
"""

# import dxchainpy package
import dxchainpy

# declare a class object with self defined host
dxchain = dxchainpy.Dxchain()

# Print out wallet information
wallet_info = dxchain.wallet.info()
print(wallet_info)
print('---- \n')

# New wallet address and print out new address
new_address = dxchain.wallet.new_address()
print(new_address)
print('---- \n')

# List of addresses belong to wallet
list_of_address = dxchain.wallet.address_list()
print(list_of_address)
print('---- \n')
