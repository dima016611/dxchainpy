from setuptools import setup


def read(filename):
    with open(filename) as file:
        return file.read()


setup(
    name='dxchainpy',
    version='0.3.6',
    description='Toolkit that allows users to interact with dxchain',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='DxChain',
    author_email='developer@dxchain.com',
    url='https://github.com/DxChainNetwork/dxchainpy',
    license='MIT',
    packages=['dxchainpy'],
    install_requires=[
        'requests'
    ]
)
