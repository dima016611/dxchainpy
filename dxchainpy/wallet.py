#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file defines a class named Wallet which contains functions to access Wallet API

Functions:
    info -- GET detailed wallet information
    new_address -- Generate and GET new wallet address
    addresses -- GET list of addresses belong to the wallet

Author: DxChain Team
Created at: 20181212
"""

from dxchainpy import api_util


class Wallet:
    """Class contains all methods to access Wallet API"""
    def __init__(self, host, port, user, password, agent):
        """
        Class Initialization with HTTP Host, Port, Authorization, and Header
        :param host: Host Name
        :param port: Host Port
        :param user: HTTP Authorization User Name
        :param password: HTTP Authorization Password
        :param agent: HTTP Header User-Agent
        """
        self._user = user
        self._password = password
        self._header = {'User-Agent': agent}
        self._start_url = 'http://{}:{}/{}'.format(host, port, 'wallet')

    def info(self):
        """GET detailed wallet information"""
        return api_util.get_url(self._start_url, self._user, self._password, self._header)

    def new_address(self):
        """Generate and GET new wallet address"""
        new_address_api = self._start_url + '/address'
        return api_util.get_url(new_address_api, self._user, self._password, self._header)

    def address_list(self):
        """GET list of addresses belong to the wallet"""
        addresses_api = self._start_url + '/addresses'
        return api_util.get_url(addresses_api, self._user, self._password, self._header)
