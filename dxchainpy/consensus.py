#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file defines a class named Consensus which contains functions to access Consensus API

Class Functions:
    Consensus.info -- GET detailed information on consensus set
    Consensus.block_by_height -- GET detailed block content based on the height of the block
    Consensus.block_by_id -- GET detailed block content based on the id of the block

Author: DxChain Team
Created at: 20181212
"""

from dxchainpy import api_util


class Consensus:
    """Class contains all methods to access Consensus API"""
    def __init__(self, host, port, user, password, agent):
        """
        Class Initialization with HTTP Host, Port, Authorization, and Header
        :param host: Host Name
        :param port: Host port
        :param user: HTTP Authorization User Name
        :param password: HTTP Authorization Password
        :param agent: HTTP User Agent
        """
        self._user = user
        self._password = password
        self._header = {'User-Agent': agent}
        self._start_url = 'http://{}:{}/{}'.format(host, port, 'consensus')

    def info(self):
        """GET detailed information on consensus set"""
        return api_util.get_url(self._start_url, self._user, self._password, self._header)

    def block_by_height(self, block_height):
        """GET detailed block content based on the height of the block"""
        block_by_height_api = self._start_url + '/blocks?height=' + str(block_height)
        return api_util.get_url(block_by_height_api, self._user, self._password, self._header)

    def block_by_id(self, block_id):
        """GET detailed block content based on the id of the block"""
        block_by_id_api = self._start_url + '/blocks?id=' + block_id
        return api_util.get_url(block_by_id_api, self._user, self._password, self._header)
