---
title: iot-sftp-client
---

# iot-sftp-client

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/PyPI-blue?logo=pypi&logoColor=yellow)

This package is a wrapper around the [pysftp](https://pypi.org/project/pysftp/) SDK to provide a synchronous client for interacting with SFTP servers from IoT edge devices.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-sftp-client) | [Package PyPI](https://pypi.org/project/iot-sftp-client/)

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

## IoTSFTPClient Class

A wrapper client to interact with an SFTP server from an IoT edge device.

This client provides operations to list, move, download, create and delete directories and files within the server.

```python
IoTSFTPClient(sftp_host, sftp_port, sftp_user, sftp_pass)
```

**Parameters**

- `sftp_host` str

  The IP address or DNS name for the SFTP server.

- `sftp_port` int

  The open connection port for the SFTP server.

- `sftp_user` str

  The username to be used for authentication with the SFTP server.

- `sftp_pass` str

  The password to be used for authentication with the SFTP server.

### Is Connected Method

Check if the current SFTP session is connected to the server.

```python
sftp_client.is_connected()
```

**Returns**

Returns a boolean - true if the connection exists, false if it doesn't exist.

### Disconnect Method

Disconnect the current SFTP session from the server.

```python
sftp_client.disconnect()
```

**Returns**

Returns `None`.

### Exists Method

Check if a file or directory exists on the SFTP server.

```python
sftp_client.exists(path)
```

**Parameters**

- `path` str

  The path to the file or directory inside the SFTP server to check for existence.

**Returns**

Returns a boolean - true if the file or directory exists, false if it does not.

### Download File Method

Download a file to a path on the local filesystem.

```python
sftp_client.download_file(source, dest)
```

**Parameters**

- `source` str

  The name and path to the file within the SFTP server to download.

- `dest` str

  The name and path to the file on the local filesystem to download to.

**Returns**

Returns a boolean - true if the file was downloaded, false if it was not.

### Upload File Method

Upload a file to a path inside the SFTP server.

```python
sftp_client.upload_file(source, dest)
```

**Parameters**

- `source` str

  The name and path to the file on the local filesystem to use for uploading.

- `dest` str

  The name and path to the file within the SFTP server to upload to/create.

**Returns**

Returns a boolean - true if the file was uploaded, false if it was not.

### Delete File Method

Delete a file from a path inside the SFTP server.

```python
sftp_client.delete_file(path)
```

**Parameters**

- `path` str

  The name and path to the file within the SFTP server to delete.

**Returns**

Returns a boolean - true if the file was deleted, false if it was not.

### Move File Method

Move a file (cut and paste) between any location within the SFTP server.

```python
sftp_client.move_file(source, dest)
```

**Parameters**

- `source` str

  The name and path to the file within the SFTP server to move.

- `dest` str

  The name and path to the file within the SFTP server to create or update.

**Returns**

Returns a boolean - true if the file was moved, false if it was not.

### List Files Method

List files under a path inside the SFTP server.

```python
sftp_client.list_files(path, file_pattern=None)
```

**Parameters**

- `path` str

  The path to the files within the SFTP server to list.

- `file_pattern` Optional[str]

  A substring of the file name or path to check for when returning the list. Default is `None`.

**Returns**

Returns a list of strings (file paths) or `None`.
