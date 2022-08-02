# iot-samba-client

[![python version](https://img.shields.io/badge/python-v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python-v3.9-blue?logo=python&logoColor=yellow) [![smbprotocol version](https://img.shields.io/badge/smbprotocol-v1.9.0-blue?logo=sabanci&logoColor=004B93)](https://img.shields.io/badge/smbprotocol-v1.9.0-blue?logo=sabanci&logoColor=004B93)

This package is a wrapper around the [smbprotocol](https://pypi.org/project/smbprotocol/) SDK for use in an IoT Platform.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-samba-client) | [Package PyPI](https://pypi.org/project/iot-samba-client/)

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)
- [API Documentation](#api-documentation)
  - [IoTSambaClient Class](#iotsambaclient-class)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Deployment Process](#deployment-process)

## Getting Started

This section provides basic examples with the `iot-samba-client`.

### Prerequisites

- Python 3.7 or later is required to use this package.

- You must have a Samba Windows File Share server to use this package.

### Basic Examples

1. Install via [pip](https://pypi.org/project/pip/):

   ```sh
   pip install iot-samba-client
   ```

2. Import and say hello:

   ```python
   from iot.samba.client import __version__


   print(f"hello world from iot-samba-client version: {__version__}")
   ```

3. Basic usage:

   ```python
   import tempfile

   from iot.samba.client import IoTSambaClient

   # instantiate client
   samba_client = IoTSambaClient(
       smb_server="windows-samba-s",
       smb_host="1.2.3.456",
       smb_port=445,
       smb_user="mySambaUserName",
       smb_pass="mySambaPass***"
   )

   # print info w/ repr
   print(f"{samba_client.__repr__()}")

   # download blob to tempfile
   temp_file = tempfile.NamedTemporaryFile()
   download_result = samba_client.download_file(
       share="MY_SAMBA_SHARE",
       path="path\\to\\blob\\parent\\dir",
       file="blob.txt",
       dest=temp_file.name,
   )
   if not download_result:
       print("unable to download file")
       temp_file.close()
       samba_client.disconnect()
       raise

   # upload tempfile to blob
   upload_result = samba_client.upload_file(
       share="MY_SAMBA_SHARE",
       path="path\\to\\new\\parent\\dir",
       file="newBlob.txt",
       source=temp_file.name,
   )
   if not upload_result:
       print("unable to upload file")
       temp_file.close()
       samba_client.disconnect()
       raise

   # clean-up local memory and disconnect from smb session
   temp_file.close()
   samba_client.disconnect()
   ```

## API Documentation

### IoTSambaClient Class

A wrapper client to interact with the smbprotocol at the share level.

This client provides operations to list, download, create and delete blobs within the share.

```python
IoTSambaClient(smb_server, smb_host, smb_port, smb_user, smb_pass)
```

**Parameters**

- `smb_server` str

  The name of the Samba Windows File Share server.

- `smb_host` str

  The hostname or IP address of the Samba Windows File Share server.

- `smb_port` int

  The port of the Samba Windows File Share server.

- `smb_user` str

  The username to connect to the Samba Windows File Share server.

- `smb_pass` Optional[str]

  The password to connect to the Samba Windows File Share server.

## Contributing

Contributions and suggestions are welcomed. However, there is a level of responsibility placed on the contributor to follow best-practices, provide thorough testing, follow the branching strategy, use the pull request template, and maintain a positive and coachable attitude when receiving feedback or questions on your code.

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` - as is standard with PyPI packages **It's important to note** that you must maintain the version with your releases in `iot/samba/client/_version.py`, otherwise a new package version will fail to get published.

## Deployment Process

1. Linting, testing and building occurs when a pull request is made from a `features/*` branch to the `master` branch.

2. Deployments to PyPI occur when an approved user triggers the GitHub Action. If the version has not been updated, this deployment will fail.
