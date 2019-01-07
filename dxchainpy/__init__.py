#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains class that used to initialize the library
Class:
    Dxchain

Author: DxChain Team
Created at: 20181212
"""

from dxchainpy.client import Client
from dxchainpy.consensus import Consensus
from dxchainpy.miner import Miner
from dxchainpy.network import Network
from dxchainpy.provider import Provider
from dxchainpy.wallet import Wallet
from dxchainpy.api_util import get_host


class Dxchain:
    """Initialize all available classes"""
    def __init__(self, host=None, port='1688', user='', password='dxchaingogogo', agent='Dx-Agent'):
        if not host:
            host = get_host()
        self.consensus = Consensus(host, port, user, password, agent)
        self.network = Network(host, port, user, password, agent)
        self.miner = Miner(host, port, user, password, agent)
        self.provider = Provider(host, port, user, password, agent)
        self.wallet = Wallet(host, port, user, password, agent)
        self.client = Client(host, port, user, password, agent)
