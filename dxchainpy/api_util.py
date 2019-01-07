#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file contains helper functions to call API.

Functions:
    get_url -- Perform HTTP GET Method to API
    post_url -- Perform HTTP POST Method to API
    get_host -- Get the host name from API

Author: DxChain Team
Created at: 20181212
"""

import json
import requests
from dxchainpy import dxexception

HOST_API = 'https://explore.dxchain.com/ip_address_code/'


def get_url(api, user, password, header) -> dict:
    """
    Access API with GET METHOD
    :param api: API to access (GET)
    :param user: HTTP Authorization User Name
    :param password: HTTP Authorization Password
    :param header: HTTP header
    :return: HTTP Returned Content
    """
    try:
        response = requests.get(
            api,
            headers=header,
            auth=(user, password),
            timeout=5,
        )
    except requests.exceptions.ConnectionError:
        raise dxexception.DxHttpConnectionError(api=api)

    # Check and handle HTTP exception
    _http_exception_handler(response.status_code, response.text, api)

    # Encode raw json data to dict
    if response.text:
        return json.loads(response.text)
    return {}


def post_url(api, user, password, data, header) -> dict:
    """
    Access API with POST METHOD
    :param api: API to access (POST)
    :param user: HTTP Authorization User Name
    :param password: HTTP Authorization Password
    :param data: data to be posted to API
    :param header: HTTP header
    :return: HTTP Returned Content
    """
    try:
        response = requests.post(
            api,
            data=data,
            headers=header,
            auth=(user, password),
            timeout=5,
        )
    except requests.exceptions.ConnectionError:
        raise dxexception.DxHttpConnectionError(api=api)

    # Check and handle HTTP exception
    _http_exception_handler(response.status_code, response.text, api)

    # Encode raw json data to dict
    if response.text:
        return json.loads(response.text)
    return {}


def get_host() -> str:
    """ Get host name from an API """
    try:
        host = requests.get(HOST_API, timeout=5)
    except requests.exceptions.ConnectionError:
        message = 'Connection to {} Failed: Please contact DxSupport Team'.format(HOST_API)
        raise dxexception.DxHttpConnectionError(message=message)

    host_dict = json.loads(host.text)
    return host_dict['ip']


def _http_exception_handler(status_code, content, api):
    """
    Check and Handle HTTP Exceptions
    :param status_code: HTTP Status Code
    :param content: HTTP Returned Content
    :param api: API Access
    :return: No Return
    """
    # Unauthorized Error
    if status_code == 401:
        raise dxexception.DxHttpAuthorizationError(api=api)

    # Other Errors Are Handled By API Already
    elif 400 <= status_code <= 599:
        raise dxexception.DxOperationError(status_code, content, api=api)
