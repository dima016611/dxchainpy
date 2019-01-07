## API document

### Overview

Along with the release of DxChain Testnet v0.3.6, Go-DxChain API is released as well. Three testing servers are hosted in different regions to handle API requests. To get the best performance, please select the server below based on IP location . 

| Node location | IP address | Port number |
| --- | --- | --- |
| US (N. California) |  13.52.66.101 | 1688 |
| EU (London) | 35.178.216.243 | 1688 |
| CN (Hebei) | 39.98.171.89 | 1688 |

Deamon programs are running on servers, making them fully synced with DxChain network. Currently, users are able to query on chain data and upload/download files with API. 

```
http://<IP address>:<port number>/<path>
```

For example, to get the current network status of the server hosted in Europe, use HTTP `GET` method with the following url:

```
curl http://35.178.216.243:1688/network

curl --header "User-Agent: Dx-Agent" --user "":"dxchaingogogo" http://35.178.216.243:1688/network

{"netaddress":"35.178.216.243:1689","peers":[{"inbound":false,"local":false,"netaddress":"52.52.118.251:1689","version":"0.3.6"},{"inbound":true,"local":false,"netaddress":"50.18.182.50:1689","version":"0.3.6"},{"inbound":false,"local":false,"netaddress":"18.191.35.18:1689","version":"0.3.6"},{"inbound":false,"local":false,"netaddress":"54.169.160.94:1689","version":"0.3.6"},{"inbound":false,"local":false,"netaddress":"13.52.66.101:1689","version":"0.3.6"},{"inbound":false,"local":false,"netaddress":"18.235.25.189:1689","version":"0.3.6"}]}
```

**Note**: The default size unit used is `byte`.

**Note**: The default currency unit used is `hump`, which is the smallest unit of dxcoin. One DXC is 10^24 humps

Detailed API usage will be discussed below.

### /network [GET]

Return information about current network status, including what the external address is, and which peers the current machine is connected to.

**Sample output**:

```json
{
    "netaddress": "13.57.1.24:1689",
    "peers": [
        {
            "inbound": false,
            "local": false,
            "netaddress": "13.52.96.207:1689",
            "version": "0.3.6"
        },
        {
            "inbound": false,
            "local": false,
            "netaddress": "52.8.2.87:1689",
            "version": "0.3.6"
        }
    ]
}
```

### /consensus [GET]

Return information on current consensus state, including the current height, current block ID, etc.

**Sample output**:

```json
{
    "synced": true,
    "height": 4225,
    "currentblock": "00000002aa3b9c4a12b3c9a426714cf1abff57e95d773bae46d09f4ef61d76b1",
    "target": [
        0,
        0,
        0,
        57,
        146,
        0,
        101,
        219,
        193,
        148,
        55,
        127,
        207,
        44,
        241,
        177,
        157,
        148,
        224,
        48,
        190,
        151,
        104,
        62,
        54,
        1,
        255,
        145,
        174,
        41,
        28,
        208
    ],
    "difficulty": "74603848"
}
```

### /consensus/blocks?height=*blockheight* [GET]

Return detailed block content with the specified block height.

| API Parameter | Description |
|---|---|
| blockheight | a number represents the height of the block | 

**Sample output**:

```json
{
    "id": "00000032b0e34b9d8d09283a8eb862cb06950ffb7be96846dad703674ab41d80",
    "height": 5,
    "parentid": "0000007340bbf82d80aada1a974f98a45e50b3e22e798c7d8a9b0b5a93670d4e",
    "difficulty": "22934380",
    "nonce": [
        149,
        32,
        0,
        0,
        0,
        0,
        0,
        0
    ],
    "timestamp": 1544828160,
    "minerpayouts": [
        {
            "id": "d3cb4ea14793ae05753f3fecf21fed548db35caa3cd1522cab8bff75ea188277",
            "value": "29700000000000000000000000000",
            "unlockhash": "WMsjbgFtmTF4xCTXJZSjEGNXvofbfvKrfHHdroLt5f1KfUsm3HxB"
        }
    ],
    "transactions": [
        {
            "id": "890980cdf546f3858fdf737c4fbf9e58b7b4e0df3c33656925e10a0ccae605e8",
            "dxcoininputs": [],
            "dxcoinoutputs": [],
            "storagecontracts": [],
            "storagecontractrevisions": [],
            "storageproofs": [],
            "minerfees": [],
            "arbitrarydata": [
                "Tm9uR2R4AAAAAAAAAAAAAHAFAybtijh3PrpUhY9h7NA="
            ],
            "transactionsignatures": []
        }
    ]
}
```

### /consensus/blocks?id=*blockid* [GET]

Return detailed block content with specified block ID. The return message is the same as the previous one.

| API Parameter | Description |
|---|---|
| blockid | 64-bit hash value represents the id of the block | 

### /wallet [GET]

Return current wallet status, including the balance, wallet status, etc.

**Sample output**:

```json
{
    "encrypted": true,
    "height": 4239,
    "rescanning": false,
    "unlocked": true,
    "confirmeddxcoinbalance": "82320612295115146315863328738930",
    "unconfirmedoutgoingdxcoins": "0",
    "unconfirmedincomingdxcoins": "0",
    "dxcoinclaimbalance": "0",
    "dxfundbalance": "0",
    "dustthreshold": "30000000000000000000"
}
```

### /wallet/address [GET] 

<spam style="font-size: 18px; font-weight: bold"> Authorization Required </spam>

Generate a new wallet address with the primary key and returned.

**Sample output**:

```json
{
    "address": "X6Hsi1KR2RYv15AA5zE1LcdMTgqvN7GZJgA3Fhzomt7pTVp54x22"
}
```

### /wallet/addresses [GET]

Return a list of addresses belonging to the wallet.

**Sample output**:

```json
{
    "Addresses": [
        {
            "id": "dgxNaR9eeJQAvm38FMAUJcrRLk1d2T9mSdXzSyfsUdy18zTddTfg",
            "balance": "0",
            "unconfirmedinput": "0",
            "unconfirmedoutput": "0"
        },
        {
            "id": "MMKUNwWPPqa1sFCymK8wajS75usCk7yMmeRNiW5eXjN81oToZuPT",
            "balance": "0",
            "unconfirmedinput": "0",
            "unconfirmedoutput": "0"
        }
    ]
}
```

### /miner [GET]

Return the current miner status.

**Sample output**:

```json
{
    "blocksmined": 2773,
    "cpuhashrate": 421533,
    "cpumining": true,
    "staleblocksmined": 4
}
```

### /provider [GET]

Return detailed provider settings information

**Sample output**:

```json
{
    "externalsettings": {
        "acceptingcontracts": true,
        "maxdownloadbatchsize": 17825792,
        "maxduration": 432,
        "maxrevisebatchsize": 17825792,
        "netaddress": "13.57.1.24:1690",
        "remainingstorage": 989855744,
        "sectorsize": 262144,
        "totalstorage": 989855744,
        "unlockhash": "PXLMoGZ8wgo8727DDCXNpE2zmJZxAE9U6TyKDG83stuG6js7SkPL",
        "windowsize": 36,
        "collateral": "2314814814",
        "maxcollateral": "5000000000000000000000000000",
        "contractprice": "300000000000000000000000",
        "downloadbandwidthprice": "25",
        "storageprice": "50",
        "uploadbandwidthprice": "1",
        "revisionnumber": 2025,
        "version": "0.3.6"
    },
    "financialmetrics": {
        "contractcount": 0,
        "contractcompensation": "0",
        "potentialcontractcompensation": "0",
        "lockedstoragecollateral": "0",
        "lostrevenue": "0",
        "loststoragecollateral": "0",
        "potentialstoragerevenue": "0",
        "riskedstoragecollateral": "0",
        "storagerevenue": "0",
        "transactionfeeexpenses": "0",
        "downloadbandwidthrevenue": "0",
        "potentialdownloadbandwidthrevenue": "0",
        "potentialuploadbandwidthrevenue": "0",
        "uploadbandwidthrevenue": "0"
    },
    "internalsettings": {
        "acceptingcontracts": true,
        "maxdownloadbatchsize": 17825792,
        "maxduration": 432,
        "maxrevisebatchsize": 17825792,
        "netaddress": "",
        "windowsize": 36,
        "collateral": "2314814814",
        "collateralbudget": "100000000000000000000000000000",
        "maxcollateral": "5000000000000000000000000000",
        "mincontractprice": "30",
        "mindownloadbandwidthprice": "25",
        "minstorageprice": "50",
        "minuploadbandwidthprice": "1"
    },
    "networkmetrics": {
        "downloadcalls": 0,
        "errorcalls": 0,
        "formcontractcalls": 0,
        "renewcalls": 0,
        "revisecalls": 0,
        "settingscalls": 2014,
        "unrecognizedcalls": 829
    },
    "connectabilitystatus": "connectable",
    "workingstatus": "working"
}
```

### /client [GET]

Return information for client settings.

**Sample output**:

```json
{
    "settings": {
        "allowance": {
            "funds": "50000000000000000000000000",
            "providers": 3,
            "period": 1440,
            "renewwindow": 720
        },
        "maxuploadspeed": 0,
        "maxdownloadspeed": 0,
        "streamcachesize": 2
    },
    "financialmetrics": {
        "contractfees": "722880000000000000000000",
        "downloadspending": "743178240000000031428",
        "storagespending": "55410687980495437824",
        "totalallocated": "4999999999999999814962828",
        "uploadspending": "18874368000000000000",
        "unspent": "49276302536704019504530748",
        "contractspending": "4999999999999999814962828",
        "withheldfunds": "4277104271360005351444108",
        "releaseblock": 4816,
        "previousspending": "2168820582324131504854134"
    },
    "currentperiod": 4050
}
```
### /client/contracts [GET]

Return list of contracts that the client has formed with providers.

**Sample output**:

```json
{
  "activecontracts": [
    {
      "StorageSpending": "0",
      "downloadspending": "0",
      "endheight": 1583,
      "fees": "361440000000000000000000",
      "goodforrenew": true,
      "goodforupload": true,
      "hostpublickey": "ed25519:19d02c9a579ed6d6c5a385245b0f51ff3b6c7b2e96d340684b0c6bf9a7075b71",
      "id": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
      "lasttransaction": {
        "arbitrarydata": [],
        "storagecontractrevisions": [
          {
            "newfilemerkleroot": "0000000000000000000000000000000000000000000000000000000000000000",
            "newfilesize": 0,
            "newmissedproofoutputs": [
              {
                "unlockhash": "LYtMm6gk3gSTTGd5Q9SKshHmiQ9z56ojfkY9n4cpbFCPDsedYgaQ",
                "value": "10749671111111111111111111"
              },
              {
                "unlockhash": "Ss9aeNSfbcm8VhK5RJF58mq64s27WNenT9xET2cn7B79k17ZszU5",
                "value": "21799342222222219961039850"
              },
              {
                "unlockhash": "LYtMm6gk3gSTTGd5Q9SKshHmiQ9z56ojfkY9n4cpbFCPDsedYgaQ",
                "value": "0"
              }
            ],
            "newrevisionnumber": 1,
            "newunlockhash": "7oZmYeCzo1QRvFH9Sy6Mi3xPEBLpmXY4QiqZZHkB9pJqJMd8uX8f",
            "newvalidproofoutputs": [
              {
                "unlockhash": "LYtMm6gk3gSTTGd5Q9SKshHmiQ9z56ojfkY9n4cpbFCPDsedYgaQ",
                "value": "10749671111111111111111111"
              },
              {
                "unlockhash": "Ss9aeNSfbcm8VhK5RJF58mq64s27WNenT9xET2cn7B79k17ZszU5",
                "value": "21799342222222219961039850"
              }
            ],
            "newwindowend": 1619,
            "newwindowstart": 1583,
            "parentid": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
            "unlockconditions": {
              "publickeys": [
                "ed25519:61805be8af102e5ed1eeb45f3da647238c35b843b82cbf330ec31d592734fcf8",
                "ed25519:19d02c9a579ed6d6c5a385245b0f51ff3b6c7b2e96d340684b0c6bf9a7075b71"
              ],
              "signaturesrequired": 2,
              "timelock": 0
            }
          }
        ],
        "storagecontracts": [],
        "gdxcoininputs": [],
        "gdxcoinoutputs": [],
        "gdxfundinputs": [],
        "gdxfundoutputs": [],
        "minerfees": [],
        "storageproofs": [],
        "transactionsignatures": [
          {
            "coveredfields": {
              "arbitrarydata": [],
              "dxcoininputs": [],
              "dxcoinoutputs": [],
              "dxtokenallocation": [],
              "dxtokendistribution": [],
              "filecontractrevisions": [
                0
              ],
              "filecontracts": [],
              "minerfees": [],
              "storageproofs": [],
              "transactionsignatures": [],
              "wholetransaction": false
            },
            "parentid": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
            "publickeyindex": 0,
            "signature": "m7W5x3nN0QeFaKFgQeeOeaEr210lUvi3KfcUDp+VndJ4rCWnXmdzaqWPnQNiK0tmYFh4yDEAkGMiNu1rp+yHCQ==",
            "timelock": 0
          },
          {
            "coveredfields": {
              "arbitrarydata": [],
              "dxcoininputs": [],
              "dxcoinoutputs": [],
              "dxtokenallocation": [],
              "dxtokendistribution": [],
              "filecontractrevisions": [
                0
              ],
              "filecontracts": [],
              "minerfees": [],
              "storageproofs": [],
              "transactionsignatures": [],
              "wholetransaction": false
            },
            "parentid": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
            "publickeyindex": 1,
            "signature": "7KyruFXn0Xv48Ac75AI5Y+SMpEhQ6ZyNDNNnntBCv/H3keyNWs4R7zFYEqRYWuWwrIfF6LvqtRtX7oH5UMr4AA==",
            "timelock": 0
          }
        ]
      },
      "netaddress": "13.52.66.101:1690",
      "renterfunds": "10749671111111111111111111",
      "size": 0,
      "startheight": 143,
      "storagespending": "0",
      "totalcost": "11111111111111111111111111",
      "uploadspending": "0"
    }
  ],
  "contracts": [
    {
      "StorageSpending": "0",
      "downloadspending": "0",
      "endheight": 1583,
      "fees": "361440000000000000000000",
      "goodforrenew": true,
      "goodforupload": true,
      "hostpublickey": "ed25519:19d02c9a579ed6d6c5a385245b0f51ff3b6c7b2e96d340684b0c6bf9a7075b71",
      "id": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
      "lasttransaction": {
        "arbitrarydata": [],
        "filecontractrevisions": [
          {
            "newfilemerkleroot": "0000000000000000000000000000000000000000000000000000000000000000",
            "newfilesize": 0,
            "newmissedproofoutputs": [
              {
                "unlockhash": "LYtMm6gk3gSTTGd5Q9SKshHmiQ9z56ojfkY9n4cpbFCPDsedYgaQ",
                "value": "10749671111111111111111111"
              },
              {
                "unlockhash": "Ss9aeNSfbcm8VhK5RJF58mq64s27WNenT9xET2cn7B79k17ZszU5",
                "value": "21799342222222219961039850"
              },
              {
                "unlockhash": "LYtMm6gk3gSTTGd5Q9SKshHmiQ9z56ojfkY9n4cpbFCPDsedYgaQ",
                "value": "0"
              }
            ],
            "newrevisionnumber": 1,
            "newunlockhash": "7oZmYeCzo1QRvFH9Sy6Mi3xPEBLpmXY4QiqZZHkB9pJqJMd8uX8f",
            "newvalidproofoutputs": [
              {
                "unlockhash": "LYtMm6gk3gSTTGd5Q9SKshHmiQ9z56ojfkY9n4cpbFCPDsedYgaQ",
                "value": "10749671111111111111111111"
              },
              {
                "unlockhash": "Ss9aeNSfbcm8VhK5RJF58mq64s27WNenT9xET2cn7B79k17ZszU5",
                "value": "21799342222222219961039850"
              }
            ],
            "newwindowend": 1619,
            "newwindowstart": 1583,
            "parentid": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
            "unlockconditions": {
              "publickeys": [
                "ed25519:61805be8af102e5ed1eeb45f3da647238c35b843b82cbf330ec31d592734fcf8",
                "ed25519:19d02c9a579ed6d6c5a385245b0f51ff3b6c7b2e96d340684b0c6bf9a7075b71"
              ],
              "signaturesrequired": 2,
              "timelock": 0
            }
          }
        ],
        "filecontracts": [],
        "gdxcoininputs": [],
        "gdxcoinoutputs": [],
        "gdxfundinputs": [],
        "gdxfundoutputs": [],
        "minerfees": [],
        "storageproofs": [],
        "transactionsignatures": [
          {
            "coveredfields": {
              "arbitrarydata": [],
              "dxcoininputs": [],
              "dxcoinoutputs": [],
              "dxtokenallocation": [],
              "dxtokendistribution": [],
              "filecontractrevisions": [
                0
              ],
              "filecontracts": [],
              "minerfees": [],
              "storageproofs": [],
              "transactionsignatures": [],
              "wholetransaction": false
            },
            "parentid": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
            "publickeyindex": 0,
            "signature": "m7W5x3nN0QeFaKFgQeeOeaEr210lUvi3KfcUDp+VndJ4rCWnXmdzaqWPnQNiK0tmYFh4yDEAkGMiNu1rp+yHCQ==",
            "timelock": 0
          },
          {
            "coveredfields": {
              "arbitrarydata": [],
              "dxcoininputs": [],
              "dxcoinoutputs": [],
              "dxtokenallocation": [],
              "dxtokendistribution": [],
              "filecontractrevisions": [
                0
              ],
              "filecontracts": [],
              "minerfees": [],
              "storageproofs": [],
              "transactionsignatures": [],
              "wholetransaction": false
            },
            "parentid": "0e656096572210ae1c906084827d1c1042ca01eeb5558283bade7dd46d85eea5",
            "publickeyindex": 1,
            "signature": "7KyruFXn0Xv48Ac75AI5Y+SMpEhQ6ZyNDNNnntBCv/H3keyNWs4R7zFYEqRYWuWwrIfF6LvqtRtX7oH5UMr4AA==",
            "timelock": 0
          }
        ]
      },
      "netaddress": "13.52.66.101:1690",
      "renterfunds": "10749671111111111111111111",
      "size": 0,
      "startheight": 143,
      "storagespending": "0",
      "totalcost": "11111111111111111111111111",
      "uploadspending": "0"
    }
  ],
  "expiredcontracts": [],
  "inactivecontracts": []
}
```

### /client/providers/active [GET]

Return list of active storage providers and corresponding settings

**Sample output**:

```json
{
  "providers": [
    {
      "LastHistoricUpdate": 4466,
      "acceptingcontracts": true,
      "collateral": "2314814814",
      "contractprice": "300000000000000000000000",
      "downloadbandwidthprice": "25000000000000",
      "firstseen": 354,
      "historicdowntime": 0,
      "historicfailedinteractions": 0.43131736091896283,
      "historicsuccessfulinteractions": 87.18474978322104,
      "historicuptime": 0,
      "maxcollateral": "5000000000000000000000000000",
      "maxdownloadbatchsize": 17825792,
      "maxduration": 25920,
      "maxrevisebatchsize": 17825792,
      "netaddress": "52.8.2.87:1690",
      "publickey": "ed25519:43413f53af6a4faba11bcf27d3d25b82be259a2a1671d22a97ac38359a7081b9",
      "publickeystring": "ed25519:43413f53af6a4faba11bcf27d3d25b82be259a2a1671d22a97ac38359a7081b9",
      "recentfailedinteractions": 0,
      "recentsuccessfulinteractions": 24,
      "remainingstorage": 975699968,
      "revisionnumber": 2348,
      "scanhistory": [
        {
          "success": true,
          "timestamp": "2018-12-15T02:58:07.585416871Z"
        },
        {
          "success": true,
          "timestamp": "2018-12-15T03:05:30.256567793Z"
        },
        {
          "success": true,
          "timestamp": "2018-12-17T23:53:07.362785471Z"
        },
        {
          "success": true,
          "timestamp": "2018-12-17T23:57:19.925556696Z"
        }
      ],
      "sectorsize": 262144,
      "storageprice": "1157407407",
      "totalstorage": 989855744,
      "unlockhash": "bmSxefo3yA52Ws5um9NFSdeRHdnVyt4iRdeu5GgUFwSUF6AsuBa3",
      "uploadbandwidthprice": "1000000000000",
      "version": "0.3.6",
      "windowsize": 36
    },
    {
      "LastHistoricUpdate": 4466,
      "acceptingcontracts": true,
      "collateral": "2314814814",
      "contractprice": "300000000000000000000000",
      "downloadbandwidthprice": "25000000000000",
      "firstseen": 354,
      "historicdowntime": 0,
      "historicfailedinteractions": 2.125778421672031,
      "historicsuccessfulinteractions": 89.46039349530885,
      "historicuptime": 0,
      "maxcollateral": "5000000000000000000000000000",
      "maxdownloadbatchsize": 17825792,
      "maxduration": 25920,
      "maxrevisebatchsize": 17825792,
      "netaddress": "13.52.96.207:1690",
      "publickey": "ed25519:bbb67c4613c3e3bb146c630b20e10f9c2f8638d14be4fe174aaef069abe1ece3",
      "publickeystring": "ed25519:bbb67c4613c3e3bb146c630b20e10f9c2f8638d14be4fe174aaef069abe1ece3",
      "recentfailedinteractions": 0,
      "recentsuccessfulinteractions": 24,
      "remainingstorage": 975699968,
      "revisionnumber": 2358,
      "scanhistory": [
        {
          "success": true,
          "timestamp": "2018-12-14T18:43:16.357434544Z"
        },
        {
          "success": true,
          "timestamp": "2018-12-15T02:33:16.357435427Z"
        },
        {
          "success": true,
          "timestamp": "2018-12-15T07:18:21.16006678Z"
        },
        {
          "success": true,
          "timestamp": "2018-12-15T07:25:00.239986709Z"
        },
        {
          "success": true,
          "timestamp": "2018-12-15T07:29:04.571050096Z"
        }
      ],
      "sectorsize": 262144,
      "storageprice": "1157407407",
      "totalstorage": 989855744,
      "unlockhash": "K7huKPCSPtnrgEMdWEFAne3TWiZ1Bho1gpUna9Ggr96jaKK5T9Ut",
      "uploadbandwidthprice": "1000000000000",
      "version": "0.3.6",
      "windowsize": 36
    },
   ]
}
```

### /client/files [GET]

Return list of all files' status that are known to the client.

**Sample output**:

```json
{
    "files": [
        {
            "dxpath": "testing/txt",
            "localpath": "/home/ubuntu/test2.txt",
            "filesize": 2097152,
            "available": true,
            "renewing": true,
            "redundancy": 2,
            "uploadedbytes": 4718592,
            "uploadprogress": 100,
            "expiration": 6210,
            "filecontracts": [
                "31438d979d6eba856b0bf54abe7e028be49fb78bc47bcea1e93eb9ba2a3dc04d",
                "e3037621a2283e186f2177da4dd123a99ecd07c19ef1d7f758af943f02577666"
            ]
        },

        {
            "dxpath": "home/mzhang/test2.txt",
            "localpath": "/home/ubuntu/api_test/text2.txt",
            "filesize": 2097152,
            "available": true,
            "renewing": true,
            "redundancy": 2,
            "uploadedbytes": 4718592,
            "uploadprogress": 100,
            "expiration": 6210,
            "filecontracts": [
                "e3037621a2283e186f2177da4dd123a99ecd07c19ef1d7f758af943f02577666",
                "31438d979d6eba856b0bf54abe7e028be49fb78bc47bcea1e93eb9ba2a3dc04d"
            ]
        },
        {
            "dxpath": "testing.txt",
            "localpath": "/home/ubuntu/test2.txt",
            "filesize": 2097152,
            "available": true,
            "renewing": true,
            "redundancy": 2,
            "uploadedbytes": 4718592,
            "uploadprogress": 100,
            "expiration": 6210,
            "filecontracts": [
                "31438d979d6eba856b0bf54abe7e028be49fb78bc47bcea1e93eb9ba2a3dc04d",
                "e3037621a2283e186f2177da4dd123a99ecd07c19ef1d7f758af943f02577666"
            ]
        }
    ]
}
```
### /client/downloads?active=*active* [GET]

Return list of downloads

| API Flag | Description |
|---|---|
| active | Boolean. If true, return current downloading files. Otherwise, returns all downloaded and downloading files | 

**Sample output**:

```json
{
    "downloads": [
        {
            "destination": "/home/ubuntu/api_test/filename.txt",
            "destinationtype": "file",
            "filesize": 2097152,
            "length": 2097152,
            "offset": 0,
            "dxpath": "mzhang",
            "completed": true,
            "endtime": "2018-12-17T21:12:15.968824153Z",
            "error": "",
            "received": 2097152,
            "starttime": "2018-12-17T21:12:06.764122744Z",
            "starttimeunix": 1545081126764122744,
            "totaldatatransferred": 4718088
        },
        {
            "destination": "/home/ubuntu/api_test/text2.txt",
            "destinationtype": "file",
            "filesize": 2097152,
            "length": 2097152,
            "offset": 0,
            "dxpath": "text2.txt",
            "completed": true,
            "endtime": "2018-12-15T03:45:21.505550618Z",
            "error": "",
            "received": 2097152,
            "starttime": "2018-12-15T03:45:12.603814196Z",
            "starttimeunix": 1544845512603814196,
            "totaldatatransferred": 4718088
        }
    ]
}
```

### /client/upload/\*upload_as [POST] 

<spam style="font-size: 18px; font-weight: bold"> Authorization Required </spam>


uploads file to dxchain network. If successfully uploaded file, nothing will be returned. Otherwise,
specific error message will be returned.

| API Parameter | Description |
|---|---|
| upload_as | the file name that is used to upload the file to chain. When download file from the chain, this file name will be used as a key | 

POST Data:

| Key | Value | Description |
|---|---|---|
| source | *absolute path* | source specifies the absolute path of the file that will be uploaded to chain | 

Example Data:

```
data = {
    'source' = /home/ubuntu/temp_folder/file_upload.txt
}
```

Example Usage:

```
curl --header "User-Agent: Dx-Agent" --user "":"dxchaingogogo" -d "source=%2Fhome%2Fubuntu%2Fdata%2FDxChain-Staff.csv" -X POST http://35.178.216.243:1688/client/upload/testing2
```


**Note**： Currently, only sample uploading files on remote servers are supported, which include:
* /home/ubuntu/data/DxChain-2018-Plan.doc
* /home/ubuntu/data/DxChain_API_Doc.md
* /home/ubuntu/data/DxChain-Flyer.png
* /home/ubuntu/data/DxChain-Post.pdf
* /home/ubuntu/data/DxChain_SDK.zip
* /home/ubuntu/data/DxChain-Staff.csv
* /home/ubuntu/data/DxChain-Video-Closing.mp4
* /home/ubuntu/data/DxChain-Video-Opening.avi
* /home/ubuntu/data/DxChain-Whitepaper.pdf

### /client/download/\*filename?destination=\*abs_path [GET]

<spam style="font-size: 18px; font-weight: bold"> Authorization Required </spam>


downloads file from dxchain network. If successfully downloaded file, nothing will be returned. Otherwise,
specific error message will be returned.

| API Parameter | Description |
|---|---|
| filename | name of the file saved on the chain |
| destination | the absolute path of the file | 

**Note**: Currently, download destination must be within the directory `/data/`.

### /client/delete/\*filename [POST] 

<spam style="font-size: 18px; font-weight: bold"> Authorization Required </spam>


deletes file from dxchain network. If successfully deleted file, nothing will be returned. Otherwise,
specific error message will be returned.

| API Parameter | Description |
|---|---|
| filename | the name of the file that will be deleted from the chain |
