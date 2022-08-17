# iot-sftp-client

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/PyPI-blue?logo=pypi&logoColor=yellow)

This package is a wrapper around the [pysftp](https://pypi.org/project/pysftp/) SDK to provide a synchronous client for interacting with SFTP servers from IoT edge devices.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-sftp-client) | [Package PyPI](https://pypi.org/project/iot-sftp-client/)

## Table of Contents

- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` and in GitHub Releases. **It's important to note** that you must maintain the version with your releases in `iot/sftp/client/_version.py`, otherwise a new package version will fail to get published.

## Getting Started

This section provides basic examples with the `iot-sftp-client`.

### Prerequisites

- Python 3.7 or later is required to use this package.

### Basic Examples

1. Install via [pip](https://pypi.org/project/pip/):

   ```sh
   pip install iot-sftp-client
   ```

2. Import and say hello:

   ```python
   from iot.sftp.client import __version__


   print(f"hello world from iot-sftp-client version: {__version__}")
   ```

3. Basic usage:

   ```python
   import tempfile

   from iot.sftp.client import IoTSFTPClient

   # instantiate client
   sftp_client = IoTSFTPClient(
       sftp_host="myServerIP",
       sftp_port=22,
       sftp_user="myServerUsername",
       sftp_pass="myServerPass***",
   )

   # print info w/ repr
   print(f"{sftp_client.__repr__()}")

   # download blob to tempfile
   temp_file = tempfile.NamedTemporaryFile()
   download_result = sftp_client.download_file(
       source="path/to/blob.txt",
       dest=temp_file.name,
   )
   if not download_result:
       print("unable to download file")
       temp_file.close()
       raise

   # upload tempfile to blob
   upload_result = sftp_client.upload_file(
       source=temp_file.name,
       dest="path/to/new/blob.txt",
   )
   if not upload_result:
       print("unable to upload file")
       temp_file.close()
       raise

   # clean-up local memory
   temp_file.close()
   ```
