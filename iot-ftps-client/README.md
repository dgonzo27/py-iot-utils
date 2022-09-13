# iot-ftps-client

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://www.python.org/) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://pre-commit.com/) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://keepachangelog.com/en/1.0.0/) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://github.com/features/actions) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://pypi.org/)

This package is a wrapper around the [ftplib](https://docs.python.org/3/library/ftplib.html) protocol to provide a synchronous client for interacting with FTPS servers from IoT edge devices.

[Official Documentation](https://py-iot-utils.com/packages/iotFtpsClient) | [Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-ftps-client) | [Package PyPI](https://pypi.org/project/iot-ftps-client/)

## Table of Contents

- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` and in GitHub Releases. **It's important to note** that you must maintain the version with your releases in `iot/ftps/client/_version.py`, otherwise a new package version will fail to get published.

## Getting Started

This section provides basic examples with the `iot-ftps-client`.

### Prerequisites

- Python 3.7 or later is required to use this package.

### Basic Examples

1. Install via [pip](https://pypi.org/project/pip/):

   ```sh
   pip install iot-ftps-client
   ```

2. Import and say hello:

   ```python
   from iot.ftps.client import __version__


   print(f"hello world from iot-ftps-client version: {__version__}")
   ```

3. Basic usage:

   ```python
   import tempfile

   from iot.ftps.client import IoTFTPSClient

   # instantiate client
   ftps_client = IoTFTPSClient(
       ftps_host="myServerIP",
       ftps_port=990,
       ftps_user="myServerUsername",
       ftps_pass="myServerPass***",
       ssl_implicit=True,
   )

   # print info w/ repr
   print(f"{ftps_client.__repr__()}")

   # download blob to tempfile
   temp_file = tempfile.NamedTemporaryFile()
   download_result = ftps_client.download_file(
       source="path/to/blob.txt",
       dest=temp_file.name,
   )
   if not download_result:
       print("unable to download file")
       temp_file.close()
       raise

   # upload tempfile to blob
   upload_result = ftps_client.upload_file(
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
