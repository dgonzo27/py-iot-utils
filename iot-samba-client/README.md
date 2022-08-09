# iot-samba-client

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/PyPI-blue?logo=pypi&logoColor=yellow) [![smbprotocol version](https://img.shields.io/badge/smbprotocol_v1.9.0-blue?logo=sabanci&logoColor=004B93)](https://img.shields.io/badge/smbprotocol_v1.9.0-blue?logo=sabanci&logoColor=004B93)

This package is a wrapper around the [smbprotocol](https://pypi.org/project/smbprotocol/) SDK to provide a synchronous client for interacting with file shares from IoT edge devices.

[Official Documentation](https://py-iot-utils.azurewebsites.net/packages/iotSambaClient) | [Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-samba-client) | [Package PyPI](https://pypi.org/project/iot-samba-client/)

## Table of Contents

- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` and in GitHub Releases. **It's important to note** that you must maintain the version with your releases in `iot/samba/client/_version.py`, otherwise a new package version will fail to get published.

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
