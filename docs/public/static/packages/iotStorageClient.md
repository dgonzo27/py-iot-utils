---
title: iot-storage-client
---

# iot-storage-client

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/PyPI-blue?logo=pypi&logoColor=yellow) [![azure-storage-blob](https://img.shields.io/badge/azure_storage_blob_v12.13.1-blue?logo=microsoft-azure&logoColor=black)](https://img.shields.io/badge/azure_storage_blob_v12.13.1-blue?logo=microsoft-azure&logoColor=black)

This package is a wrapper around the [azure-storage-blob](https://pypi.org/project/azure-storage-blob/) SDK to provide an asynchronous and synchronous client for interacting with Azure storage accounts in the cloud and on the edge.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-storage-client) | [Package PyPI](https://pypi.org/project/iot-storage-client/)

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

## IoTStorageClient Class

A wrapper client to interact with the Azure Blob Service at the account level.

This client provides operations to list, create and delete storage containers and blobs within the account.

```python
IoTStorageClient(credential_type, location_type, account_name, credential, host=None, port=None)
```

**Parameters**

- `credential_type` str

  The type of credential that will be used for authentication. One of "ACCOUNT_KEY" or "CONNECTION_STRING".

- `location_type` str

  The location of the Azure storage account. This allows for communicating with storage accounts that live on IoT Edge devices. One of "CLOUD_BASED" or "EDGE_BASED".

- `account_name` str

  The name of the Azure storage account.

- `credential` str

  The credential (account key or connection string), that is being used for authentication.

- `host` Optional[str]

  The DNS or IP address of the Azure storage account when it lives on an IoT Edge device.

- `port` Optional[str]

  The open port of the Azure storage account when it lives on an IoT Edge device.

### Container Exists Method

Check if a container exists.

```python
storage_client.container_exists(container_name)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account to check for existence.

**Returns**

Returns a boolean - true if the container exists, false if it doesn't exist.

### File Exists Method

Check if a file exists.

```python
storage_client.file_exists(container_name, file_name)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the file is in.

- `file_name` str

  The name and path to the file within the Azure storage account to check for existence.

**Returns**

Returns a boolean - true if the file exists, false if it doesn't exist.

### Download Method

Download a file or directory to a path on the local filesystem.

```python
storage_client.download(container_name, source, dest)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the file or directory is in.

- `source` str

  The name and path to the file or directory within the Azure storage account to download.

- `dest` str

  The name and path to the file or directory on the local filesystem to download to.

**Returns**

Returns a boolean - true if the file or directory was downloaded, false if it was not.

### Download File Method

Download a file to a path on the local filesystem.

```python
storage_client.download_file(container_name, source, dest)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the file is in.

- `source` str

  The name and path to the file within the Azure storage account to download.

- `dest` str

  The name and path to the file on the local filesystem to download to.

**Returns**

Returns a boolean - true if the file was downloaded, false if it was not.

### Upload Method

Upload a file or directory to a path inside the container.

```python
storage_client.upload(container_name, source, dest)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the file or directory will be uploaded to.

- `source` str

  The name and path to the directory or file on the local filesystem to use for uploading.

- `dest` str

  The name and path to the directory or file within the Azure storage account to upload to/create.

**Returns**

Returns a boolean - true if the file or directory was uploaded, false if it was not.

### Upload File Method

Upload a file to a path inside the container.

```python
storage_client.upload_file(container_name, source, dest, content_type="application/octet-stream", overwrite=True)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the file will be uploaded to.

- `source` str

  The name and path to the file on the local filesystem to use for uploading.

- `dest` str

  The name and path to the file within the Azure storage account to upload to/create.

- `content_type` Optional[str]

  The content-type for the uploaded blob. Default is "application/octet-stream".

- `overwrite` Optional[bool]

  Overwrite the blob if it already exists. Default is True.

**Returns**

Returns a boolean - true if the file was uploaded, false if it was not.

### Delete Directory Method

Delete a directory and its contents recursively from a path inside the container.

```python
storage_client.delete_dir(container_name, path)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the directory is located in.

- `path` str

  The name and path to the directory within the Azure storage account to delete.

**Returns**

Returns a boolean - true if the directory was deleted, false if it was not.

### Delete File Method

Delete a file from a path inside the container.

```python
storage_client.delete_file(container_name, path)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the file is located in.

- `path` str

  The name and path to the file within the Azure storage account to delete.

**Returns**

Returns a boolean - true if the file was deleted, false if it was not.

### List Directories Method

List directories under a path inside the container, optionally recursive.

```python
storage_client.list_dirs(container_name, path, recursive=False)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the directories are located in.

- `path` str

  The path to the directories within the Azure storage account to list.

- `recursive` Optional[bool]

  List all sub-directories of the listed directories. Default is False.

**Returns**

Returns a list of strings (directory paths) or `None`.

### List Files Method

List files under a path inside the container, optionally recursive.

```python
storage_client.list_files(container_name, path, recursive=False)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the files are located in.

- `path` str

  The path to the files within the Azure storage account to list.

- `recursive` Optional[bool]

  List all sub-directories and its files of the listed files root directory. Default is False.

**Returns**

Returns a list of strings (file paths) or `None`.

### Copy File Method

Copy a file between any location within the same storage account.

```python
storage_client.copy_file(container_name, source, dest_container, dest)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the source file is located in.

- `source` str

  The name and path to the file within the Azure storage account to copy.

- `dest_container` str

  The name of the container within the Azure storage account where the file will be copied to.

- `dest` str

  The name and path to the file within the Azure storage account to create or copy to.

**Returns**

Returns a boolean - true if the file was copied, false if it was not.

### Move File Method

Move a file (cut and paste) between any location within the same storage account.

```python
storage_client.move_file(container_name, source, dest_container, dest)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account that the source file is located in.

- `source` str

  The name and path to the file within the Azure storage account to move.

- `dest_container` str

  The name of the container within the Azure storage account where the file will be moved to.

- `dest` str

  The name and path to the file within the Azure storage account to create or update.

**Returns**

Returns a boolean - true if the file was moved, false if it was not.

### Copy From URL Method

Copy a file from a URL to a path inside the container.

```python
storage_client.copy_from_url(source_url, container_name, dest, timeout=100)
```

**Parameters**

- `source_url` str

  The URL where the file is being copied from. For example, a SAS URL for another storage account.

- `container_name` str

  The name of the container within the Azure storage account where the file will be copied to.

- `dest` str

  The name and path to the file within the Azure storage account to create or update.

- `timeout` Optional[str]

  The time in seconds to wait for the copy operation to complete before timing out. Default is `100`.

**Returns**

Returns a boolean - true if the file was copied, false if it was not.

### Generate File SAS URL

Generate a SAS URL for a given file inside the container.

```python
storage_client.generate_file_sas_url(
  container_name,
  source,
  read=True,
  write=False,
  delete=False,
  start=None,
  expiry=datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
)
```

**Parameters**

- `container_name` str

  The name of the container within the Azure storage account where the file is located.

- `source` str

  The name and path to the file within the Azure storage account used to generate a SAS URL.

- `read` Optional[bool]

  Determine if the SAS URL should grant read permission to the file. Default is `True`.

- `write` Optional[bool]

  Determine if the SAS URL should grant write permission to the file. Default is `False`.

- `delete` Optional[bool]

  Determine if the SAS URL should grant delete permission to the file. Default is `False`.

- `start` Optional[Union[datetime.datetime, str]]

  The start time for accessing the file via the SAS URL - a default of `None` sets the start time to the SAS URL's creation time.

- `expiry` Optional[Union[datetime.datetime, str]]

  The expiration time for accessing the file via the SAS URL. Default is `datetime.datetime.utcnow() + datetime.timedelta(minutes=15)`.

**Returns**

Returns a string or `None` - the SAS URL if successful, `None` if it was not.
