# iot-samba-client

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/PyPI-blue?logo=pypi&logoColor=yellow) [![smbprotocol version](https://img.shields.io/badge/smbprotocol_v1.9.0-blue?logo=sabanci&logoColor=004B93)](https://img.shields.io/badge/smbprotocol_v1.9.0-blue?logo=sabanci&logoColor=004B93)

This package is a wrapper around the [smbprotocol](https://pypi.org/project/smbprotocol/) SDK to provide a synchronous client for interacting with file shares from IoT edge devices.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-samba-client) | [Package PyPI](https://pypi.org/project/iot-samba-client/)

## Table of Contents

- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)
- [IoTSambaClient Class](#iotsambaclient-class)
  - [Is Connected Method](#is-connected-method)
  - [Disconnect Method](#disconnect-method)
  - [Stat Method](#stat-method)
  - [Download File Method](#download-file-method)
  - [Upload File Method](#upload-file-method)
  - [Delete File Method](#delete-file-method)
  - [Move File Method](#move-file-method)
  - [List Files Method](#list-files-method)

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

## IoTSambaClient Class

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

### Is Connected Method

Checks if the current session is connected to the smbclient.

```python
samba_client.is_connected()
```

**Returns**

Returns a boolean - true if the session is connected, false if not connected.

### Disconnect Method

Disconnect the current session from the smbclient.

```python
samba_client.disconnect()
```

**Returns**

Returns `None`.

### Stat Method

Returns file information for a given path.

```python
samba_client.stat(share, path, file="")
```

**Parameters**

- `share` str

  The name of the file share for the desired stat.

- `path` str

  The path on the file share for the desired stat.

- `file` Optional[str]

  The name of the file for the desired stat.

**Returns**

Returns a `smbclient.SMBStatResult` if found, or `None`.

### Download File Method

Download a file to a path on the local filesystem.

```python
samba_client.download_file(share, path, file, dest)
```

**Parameters**

- `share` str

  The name of the file share for the file to download.

- `path` str

  The path on the file share for the file to download.

- `file` str

  The name of the file to download.

- `dest` str

  The name and path to the file on the local filesystem to download to.

**Returns**

Returns a boolean - true if the file was downloaded, false if it was not.

### Upload File Method

Upload a file to a path inside the samba server.

```python
samba_client.upload_file(share, path, file, source)
```

**Parameters**

- `share` str

  The name of the file share for the file to upload.

- `path` str

  The path on the file share for the file to upload.

- `file` str

  The name of the file to upload.

- `source` str

  The name and path to the file on the local filesystem to upload.

**Returns**

Returns a boolean - true if the file was uploaded, false if it was not.

### Delete File Method

Delete a file from a path inside the samba server.

```python
samba_client.delete_file(share, path, file)
```

**Parameters**

- `share` str

  The name of the file share for the file to delete.

- `path` str

  The path on the file share for the file to delete.

- `file` str

  The name of the file to delete.

**Returns**

Returns a boolean - true if the file was deleted, false if it was not.

### Move File Method

Move a file from a path inside the samba server to another path inside the samba server.

```python
samba_client.move_file(share, path, file, new_path, new_file)
```

**Parameters**

- `share` str

  The name of the file share for the file to move.

- `path` str

  The path on the file share for the file to move.

- `file` str

  The name of the file to move.

- `new_path` str

  The new path on the file share for the file to move.

- `new_file` str

  The new name of the file to move.

**Returns**

Returns a boolean - true if the file was moved, false if it was not.

### List Files Method

List files under a path inside the samba server.

```python
samba_client.list_files(share, path, file_pattern)
```

**Parameters**

- `share` str

  The name of the file share to list files under.

- `path` str

  The path on the file share to list files under.

- `file_pattern` str

  A regex or file name to list files under.

**Returns**

Returns a list of string file paths, or `None`.
