#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file defines a class named Provider which contains functions to access Provider API

Class Functions:
    Provider.info -- GET detailed provider information

Author: DxChain Team
Created at: 20181212
"""

from dxchainpy import api_util


class Provider:
    """Class contains all methods to access Provider API"""
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
        self._start_url = 'http://{}:{}/{}'.format(host, port, 'provider')

    def info(self):
        """GET detailed provider information"""
        return api_util.get_url(self._start_url, self._user, self._password, self._header)
