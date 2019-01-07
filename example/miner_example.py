#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is used to demo features on Miner module

Author: DxChain Team
Created at: 20181212
"""

# import dxchainpy package
import dxchainpy

# declare a class object with self defined host
dxchain = dxchainpy.Dxchain()

# call Miner method
# Miner Information
miner_info = dxchain.miner.info()
print(miner_info)
