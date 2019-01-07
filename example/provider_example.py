#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is used to demo features on Provider module

Author: DxChain Team
Created at: 20181212
"""

# import dxchainpy package
import dxchainpy

# declare a class object with self defined host
dxchain = dxchainpy.Dxchain()

# Provider Information
provider_info = dxchain.provider.info()
print(provider_info)
