#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains customized DxChain Exceptions

Author: DxChain Team
Created at: 20181212
"""

from http import HTTPStatus


class DxHttpConnectionError(Exception):
    """Class Define DX HTTP Connection Error"""
    def __init__(self, api=None, message=None):
        """
        Initialize class with api
        :param api: API
        :param message: Exception Message
        """
        if message is None:
            message = 'Connection to {} Failed: Please check if the host name and port number were entered correctly'.format(api)
        super().__init__(message)


class DxHttpAuthorizationError(Exception):
    """Class Define DX HTTP Authorization Error"""
    def __init__(self, api=None, message=None):
        """
        Initialize class with api
        :param api: API
        :param message: Exception Message
        """
        if message is None:
            message = 'API {} Authorization Failed: Please check if the user name and password were entered correctly'.format(api)
        super().__init__(message)


class DxOperationError(Exception):
    """Class Define DX Operation Error: wrong input or wrong operation"""
    def __init__(self, status_code, content, api=None, message=None):
        """
        Initialize class with api, status_code, and content
        :param api: API
        :param status_code: HTTP Returned Status Code
        :param content: API Returned Error Message and Causes
        :param message: Exception Message
        """
        if message is None:
            message = 'Connection to {} returned error status {} {}: {}'.format(api, status_code, HTTPStatus(status_code).phrase, content)
        super().__init__(message)
