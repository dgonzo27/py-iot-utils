# py-iot-utils

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://www.python.org/) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://pre-commit.com/) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://keepachangelog.com/en/1.0.0/) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://github.com/features/actions) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://pypi.org/)

This repository contains stateless PyPI packages to be used across an Azure IoT Platform as it relates to software written in Python.

While these packages are related in terms of their intended use cases, they are independent of one another and should be treated as such when collaborating, developing, and maintaining. For the consumers of these packages, please start by visiting the PyPI specific documentation - the links can be found in the [Packages](#packages) section below or by visiting [this page](https://pypi.org/user/dgonzo27/) to view all of the packages.

## Packages

As mentioned above, there are several PyPI packages contained within this repository. Each subfolder has it's own related build, README.md, and associated documentation to help you get started.

- [iot-edge-logger](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-edge-logger)

  This package is a custom log formatter to standardize, collect and analyze logs from IoT Edge Devices in an Azure Log Analytics Workspace. [View on PyPI](https://pypi.org/project/iot-edge-logger/).

- [iot-edge-validator](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-edge-validator)

  This package is a wrapper around the [azure-iot-device](https://pypi.org/project/azure-iot-device/) SDK to provide standardized exception handling and direct method request validation. [View on PyPI](https://pypi.org/project/iot-edge-validator).

- [iot-ftps-client](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-ftps-client)

  This package is a wrapper around the [ftplib](https://docs.python.org/3/library/ftplib.html) protocol to provide a synchronous client for interacting with FTPS servers from IoT edge devices.

- [iot-samba-client](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-samba-client)

  This package is a wrapper around the [smbprotocol](https://pypi.org/project/smbprotocol/) SDK to provide a synchronous client for interacting with file shares from IoT edge devices. [View on PyPI](https://pypi.org/project/iot-samba-client).

- [iot-storage-client](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-storage-client)

  This package is a wrapper around the [azure-storage-blob](https://pypi.org/project/azure-storage-blob/) SDK to provide an asynchronous and synchronous client for interacting with Azure storage accounts in the cloud and on the edge. [View on PyPI](https://pypi.org/project/iot-storage-client/).

## Need Support?

- Checkout our [Official Documentation](https://py-iot-utils.com)!
- File an issue via [GitHub Issues](https://github.com/dgonzo27/py-iot-utils/issues).

### Reporting Security Vulnerabilities and Security Bugs

Security vulnerabilities and bugs should be reported privately, via email, to the maintainers of this repository. Please contact [py.iot.utils@gmail.com](mailto:py.iot.utils@gmail.com).

## Contributing

Before contributing to this repository, please review the [code of conduct](./CODE_OF_CONDUCT.md).

Contributions and suggestions are welcomed. However, there is a level of responsibility placed on the contributor to follow best-practices, provide thorough testing, follow the branching strategy, use the pull request template, and maintain a positive and coachable attitude when receiving feedback or questions on your code. For more details on these responsibilities, please visit the [contributing guide](./CONTRIBUTING.md).

When contributing, you are granting the maintainers of this repository the rights to use your contribution(s).
