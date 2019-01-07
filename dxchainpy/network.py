#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file defines a class named Network which contains functions to access Network API

Class Functions:
    Network.info -- GET detailed information of the network

Author: DxChain Team
Created at: 20181212
"""

from dxchainpy import api_util


class Network:
    """Class contains all methods to access Network API"""
    def __init__(self, host, port, user, password, agent):
        """
        Class Initialization with HTTP Host, Port, Authorization, and Header
        :param host: Host Name
        :param port: Host Port
        :param user: HTTP Authorization User Name
        :param password: HTTP Authorization Password
        :param agent: HTTP User Agent
        """
        self._user = user
        self._password = password
        self._header = {'User-Agent': agent}
        self._start_url = 'http://{}:{}/{}'.format(host, port, 'network')

    def info(self) -> dict:
        """ GET detailed information of the network """
        return api_util.get_url(self._start_url, self._user, self._password, self._header)
