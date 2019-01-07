# DxChainPy

DxChainPy is a simple Python implementation for DxChain API, which allows users to build their own application based on DxChain Network.

Table of Contents:

* [Requirements](#requirements)
* [Installation](#installation)
* [Documentation](#documentation)
* [Examples](#examples)
* [License](#license)

## Requirements

* Python: 3.7

## Installation

There are two ways to install the library:

* Installation using pip (Python Package Manager):

```bash
$ pip install dxchainpy
```

* Installation from source (requires git):

```bash
$ git clone https://github.com/DxChainNetwork/dxchainpy
$ cd dxchainpy 
$ python setup.py install
```

## Documentation
Documentation is available online: [https://dxchainapidoc.readthedocs.io/en/latest/index.html](https://dxchainapidoc.readthedocs.io/en/latest/index.html)

For support, please email **developer@dxchain.com**

## Examples
**Getting information of consensus and specific blocks**

```python
# import dxchainpy package
import dxchainpy

# declare a class object with self defined host
dxchain = dxchainpy.Dxchain()

# call Consensus methods
# Get consensus information
consensus_info = dxchain.consensus.info()
print(consensus_info)

# Get block information based on height
block_info = dxchain.consensus.block_by_height(3)
print(block_info)

# Get block information based on id
block_id = '00000001ef0bfc292345e67cdd3f918206993036e7f500c7995d224e9b9da99a'
block_info = dxchain.consensus.block_by_id(block_id)
print(block_info)
```

The example will print (python dictionary format):

```python
{'synced': True, 'height': 835, 'currentblock': '00000005a198330a265aab9538fa882e41a423181570923fd9b1d7c78dcb0780', 'target': [0, 0, 0, 6, 166, 127, 91, 80, 240, 184, 121, 105, 236, 89, 120, 91, 125, 245, 238, 213, 218, 145, 156, 7, 207, 210, 3, 236, 200, 20, 186, 116], 'difficulty': '645822761'}

{'id': '0000000f28ee9ea58b711b1870a0e243ab415b5eea7eabf6db2f3c0670fb3026', 'height': 3, 'parentid': '00000002a23b13c30d4d5400ae3a94f74bba4cc63c65e39eedfa5922987ee78e', 'difficulty': '238609294', 'nonce': [19, 30, 0, 0, 0, 0, 0, 0], 'timestamp': 1546563148, 'minerpayouts': [{'id': 'a25cb81b9d1e3ea33f9177c4fc7d9c1d1b15337c5f676d22b1d785c61d468c8d', 'value': '29700000000000000000000000000', 'unlockhash': 'TeRWdaMsigXka35nPtT4mBXVRTSeXGRqMDRVknswNjG1WKSDiKdk'}], 'transactions': [{'id': '7cc21c8aea62561e78b42a32cf928b5e94a098e2c49f1f7e776bc07e1507eeed', 'dxcoininputs': [], 'dxcoinoutputs': [], 'storagecontracts': [], 'storagecontractrevisions': [], 'storageproofs': [], 'minerfees': [], 'arbitrarydata': ['Tm9uR2R4AAAAAAAAAAAAABq7mAmGSRQKzVN2umDuyaQ='], 'transactionsignatures': []}]}

{'id': '00000001ef0bfc292345e67cdd3f918206993036e7f500c7995d224e9b9da99a', 'height': 243, 'parentid': '00000004cd371436d403e7c53d55ee6e65ffd7a5c666bd4c2c1e21d7088f781a', 'difficulty': '120769904', 'nonce': [45, 24, 0, 0, 0, 0, 0, 0], 'timestamp': 1546564063, 'minerpayouts': [{'id': '1d2578fa90e8f62da0d38bc9c13bdcd606137c42ff628de18d77b875f28c6d8c', 'value': '29695000000000000000000000000', 'unlockhash': 'BWNc8v3innYXCF6shQPyCXsEA14YdogYKYGXYwGeu26cnJ6iG4mQ'}], 'transactions': [{'id': '3e3e530e93a26d61bbd4b0ad40d20f9f96c71b18b0a0d1ce1a859d9d8b6efa81', 'dxcoininputs': [], 'dxcoinoutputs': [], 'storagecontracts': [], 'storagecontractrevisions': [], 'storageproofs': [], 'minerfees': [], 'arbitrarydata': ['Tm9uR2R4AAAAAAAAAAAAAAM4ko5KxCHocnNSFXC6jXE='], 'transactionsignatures': []}]}
```

## License
DxChainPy is released under the MIT License. See LICENSE for more information.