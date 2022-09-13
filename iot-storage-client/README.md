# iot-storage-client

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://www.python.org/) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://pre-commit.com/) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://keepachangelog.com/en/1.0.0/) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://github.com/features/actions) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://pypi.org/) [![azure-storage-blob](https://img.shields.io/badge/azure_storage_blob_v12.13.1-blue?logo=microsoft-azure&logoColor=black)](https://pypi.org/project/azure-storage-blob/)

This package is a wrapper around the [azure-storage-blob](https://pypi.org/project/azure-storage-blob/) SDK to provide an asynchronous and synchronous client for interacting with Azure storage accounts in the cloud and on the edge.

[Official Documentation](https://py-iot-utils.com/packages/iotStorageClient) ([async version](https://py-iot-utils.com/packages/iotStorageClientAsync)) | [Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-storage-client) | [Package PyPI](https://pypi.org/project/iot-storage-client/)

## Table of Contents

- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` and in GitHub Releases. **It's important to note** that you must maintain the version with your releases in `iot/storage/client/_version.py`, otherwise a new package version will fail to get published.

## Getting Started

This section provides basic examples with the `iot-storage-client`.

### Prerequisites

- Python 3.7 or later is required to use this package.

- You must have an Azure subscription and Azure storage account to use this package.

### Basic Examples

1. Install via [pip](https://pypi.org/project/pip/):

   ```sh
   pip install iot-storage-client
   ```

2. Import and say hello:

   ```python
   from iot.storage.client import __version__


   print(f"hello world from iot-storage-client version: {__version__}")
   ```

3. Basic usage:

   ```python
   import tempfile

   from iot.storage.client import CredentialType, LocationType, IoTStorageClient

   # instantiate client
   storage_client = IoTStorageClient(
       credential_type=CredentialType.ACCOUNT_KEY,
       location_type=LocationType.CLOUD_BASED,
       account_name="myAzBlobStorageAcctName",
       credential="myBlobPrimaryKey***"
   )

   # print info w/ repr
   print(f"{storage_client.__repr__()}")

   # download blob to tempfile
   temp_file = tempfile.NamedTemporaryFile()
   download_result = storage_client.download_file(
       container_name="myAzBlobContainerName",
       source="path/to/blob.txt",
       dest=temp_file.name,
   )
   if not download_result:
       print("unable to download file")
       temp_file.close()
       raise

   # upload tempfile to blob
   upload_result = storage_client.upload_file(
       container_name="myAzBlobContainerName",
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

4. Basic async usage:

   ```python
   import tempfile

   from iot.storage.client import CredentialType, LocationType, IoTStorageClientAsync

   # instantiate client
   storage_client = IoTStorageClientAsync(
       credential_type=CredentialType.ACCOUNT_KEY,
       location_type=LocationType.CLOUD_BASED,
       account_name="myAzBlobStorageAcctName",
       credential="myBlobPrimaryKey***"
   )

   # print info w/ repr
   print(f"{storage_client.__repr__()}")

   # download blob to tempfile
   temp_file = tempfile.NamedTemporaryFile()
   download_result = await storage_client.download_file(
       container_name="myAzBlobContainerName",
       source="path/to/blob.txt",
       dest=temp_file.name,
   )
   if not download_result:
       print("unable to download file")
       temp_file.close()
       raise

   # upload tempfile to blob
   upload_result = await storage_client.upload_file(
       container_name="myAzBlobContainerName",
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
