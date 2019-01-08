#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is used to demo features on Client module

Author: DxChain Team
Created at: 20181212
"""

# import dxchainpy package
import time
import dxchainpy

# declare a class object with self defined host
dxchain = dxchainpy.Dxchain()

# # Looking for active providers and form contract
providers = dxchain.client.active_providers()
print(providers)
print('---- \n')

# Currently, only sample uploading files on remote servers are supported, which include:
# /home/ubuntu/data/DxChain-2018-Plan.doc
# /home/ubuntu/data/DxChain_API_Doc.md
# /home/ubuntu/data/DxChain-Flyer.png
# /home/ubuntu/data/DxChain-Post.pdf
# /home/ubuntu/data/DxChain_SDK.zip
# /home/ubuntu/data/DxChain-Staff.csv
# /home/ubuntu/data/DxChain-Video-Closing.mp4
# /home/ubuntu/data/DxChain-Video-Opening.avi
# /home/ubuntu/data/DxChain-Whitepaper.pdf

# Upload a file from /home/ubuntu/test1.txt as mzhang to node
dxchain.client.file_upload('/home/ubuntu/data/DxChain-Staff.csv', 'mzhang_testing')
print("WAITING FOR UPLOADING ...")
time.sleep(5)

# Checking file upload status
upload_status = dxchain.client.upload_status()
print(upload_status)
print('---- \n')

# Download file from the node named text2.txt (pre-uploaded file)
dxchain.client.file_download('mzhang_testing', '/data/mzhang_testing')

# Checking current downloading files
current_downloading_files = dxchain.client.current_downloads()
print(current_downloading_files)
print('---- \n')

# Checking all downloads
all_downloads = dxchain.client.downloads_list()
print(all_downloads)
print('---- \n')
