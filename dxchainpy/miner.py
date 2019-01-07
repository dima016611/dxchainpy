#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file defines a class named Miner which contains functions to access Miner API

Class Functions:
    Miner.info -- GET detailed Miner Status Information

Author: DxChain Team
Created at: 20181212
"""

from dxchainpy import api_util


class Miner:
    """Class contains all methods to access Miner API"""
    def __init__(self, host, port, user, password, header):
        """
        Class Initialization with HTTP Host, Port, Authorization, and Header
        :param host: Host Name
        :param port: Host port
        :param user: HTTP Authorization User Name
        :param password: HTTP Authorization Password
        :param header: HTTP Header
        """
        self._user = user
        self._password = password
        self._header = {'User-Agent': header}
        self._start_url = 'http://{}:{}/{}'.format(host, port, 'miner')

    def info(self):
        """GET detailed Miner Status Information"""
        return api_util.get_url(self._start_url, self._user, self._password, self._header)
