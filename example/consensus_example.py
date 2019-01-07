#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is used to demo features on Consensus module

Author: DxChain Team
Created at: 20181212
"""

# import dxchainpy package
import dxchainpy

# declare a class object with self defined host
dxchain = dxchainpy.Dxchain()

# call Consensus methods
# Get consensus information
consensus_info = dxchain.consensus.info()
print(consensus_info)
print('---- \n')

# Get block information based on height
block_info = dxchain.consensus.block_by_height(3)
print(block_info)
print('---- \n')

# Get block information based on id
block_id = '00000001ef0bfc292345e67cdd3f918206993036e7f500c7995d224e9b9da99a'
block_info = dxchain.consensus.block_by_id(block_id)
print(block_info)
print('---- \n')
