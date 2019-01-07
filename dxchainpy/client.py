#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This file defines a class named Client which contains functions to access Client API

Class Functions:
    info -- GET detailed client setting information
    contracts -- GET list of contracts that client formed with provider
    active_providers -- GET list of active storage providers and corresponding settings
    upload_status -- GET list of all files' status that are known to client
    current_downloads -- GET list of files that are current downloading
    downloads_list -- GET list of all downloads
    file_upload -- Upload file to DxChain Network
    file_download -- Download file from DxChain Network
    file_delete -- Delete file from DxChain Network

Author: DxChain Team
Created at: 20181212
"""

import urllib
from urllib.parse import urlparse
from dxchainpy import api_util


class Client:
    """Class contains all methods to access Client API"""
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
        self._start_url = 'http://{}:{}/{}'.format(host, port, 'client')

    def info(self):
        """GET detailed client setting information"""
        return api_util.get_url(self._start_url, self._user, self._password, self._header)

    def contracts(self):
        """GET list of contracts that client formed with provider"""
        contracts_api = self._start_url + '/contracts'
        return api_util.get_url(contracts_api, self._user, self._password, self._header)

    def active_providers(self):
        """GET list of active storage providers and corresponding settings"""
        providers_api = self._start_url + '/providers/active'
        return api_util.get_url(providers_api, self._user, self._password, self._header)

    def upload_status(self):
        """GET list of all files' status that are known to client"""
        file_list_api = self._start_url + '/files'
        return api_util.get_url(file_list_api, self._user, self._password, self._header)

    def current_downloads(self):
        """GET list of files that are current downloading"""
        current_downloads_api = self._start_url + '/downloads?active=true'
        return api_util.get_url(current_downloads_api, self._user, self._password, self._header)

    def downloads_list(self):
        """GET list of all downloads"""
        downloads_list_api = self._start_url + '/downloads?active=false'
        return api_util.get_url(downloads_list_api, self._user, self._password, self._header)

    def file_upload(self, source, upload_as):
        """
        Upload file to DxChain Network
        :param source: location of the file
        :param upload_as: file name you want to upload as
        """
        upload_as = urllib.parse.quote(upload_as, safe='')
        file_upload_api = self._start_url + '/upload/' + upload_as
        data = {
            'source': source
        }
        return api_util.post_url(file_upload_api, self._user, self._password, data, self._header)

    def file_download(self, file_name, destination, download_async='true'):
        """
        Download file from DxChain Network
        :param file_name: file you are trying to download from DxChain Network
        :param destination: absolute path, where to place downloaded file
        :param download_async: download file in async way
        """
        file_name = urllib.parse.quote(file_name, safe='')
        destination = urllib.parse.quote(destination, safe='')

        file_download_api = '{}/{}/{}?destination={}&async={}'.format(self._start_url, 'download', file_name,
                                                                      destination, download_async)
        return api_util.get_url(file_download_api, self._user, self._password, self._header)

    def file_delete(self, file_name):
        """
        Delete file from DxChain Network
        :param file_name: name of the file that needs to deleted
        """
        file_name = urllib.parse.quote(file_name, safe='')
        file_delete_api = self._start_url + '/delete/' + file_name
        data = {}
        return api_util.post_url(file_delete_api, self._user, self._password, data, self._header)
