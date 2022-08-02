# py-iot-utils

[![python version](https://img.shields.io/badge/python-v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python-v3.9-blue?logo=python&logoColor=yellow) [![package PyPI](https://img.shields.io/badge/package-PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/package-PyPI-blue?logo=pypi&logoColor=yellow) [![CI_CD GitHub_Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-blue?logo=githubactions&logoColor=2088FF)](https://img.shields.io/badge/CI/CD-GitHub_Actions-blue?logo=githubactions&logoColor=2088FF)

This repository contains stateless PyPI packages to be used across an Azure IoT Platform as it relates to software written in Python.

## Packages

As mentioned above, there are several PyPI packages contained within this repository. Each subfolder has it's own build, README.md, and associated contribution documentation to help you get started.

- [iot-edge-logger](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-edge-logger)

  This package is a custom log formatter to standardize, collect and analyze logs from IoT Edge Devices in an Azure Log Analytics Workspace. [View on PyPI](https://pypi.org/project/iot-edge-logger/).

- [iot-edge-validator](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-edge-validator)

  This package is a wrapper around the [azure-iot-device](https://pypi.org/project/azure-iot-device/) SDK to provide standardized exception handling and direct method request validation. [View on PyPI](https://pypi.org/project/iot-edge-validator).

- [iot-samba-client](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-samba-client)

  This package is a wrapper around the [smbprotocol](https://pypi.org/project/smbprotocol/) SDK. [View on PyPI](https://pypi.org/project/iot-samba-client).

- [iot-storage-client](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-storage-client)

  This package is a wrapper around the [azure-storage-blob](https://pypi.org/project/azure-storage-blob/) SDK. [View on PyPI](https://pypi.org/project/iot-storage-client/).
