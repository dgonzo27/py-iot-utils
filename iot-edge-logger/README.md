# iot-edge-logger

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/PyPI-blue?logo=pypi&logoColor=yellow)

This package is a custom log formatter to standardize, collect and analyze logs from IoT Edge Devices in an Azure Log Analytics Workspace.

[Official Documentation](https://py-iot-utils.azurewebsites.net/packages/iotEdgeLogger) | [Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-edge-logger) | [Package PyPI](https://pypi.org/project/iot-edge-logger/)

## Table of Contents

- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` and in GitHub Releases. **It's important to note** that you must maintain the version with your releases in `iot/edge/logger/_version.py`, otherwise a new package version will fail to get published.

## Getting Started

This section provides basic examples with the `iot-edge-logger`.

### Prerequisites

- Python 3.7 or later is required to use this package.

### Basic Examples

1. Install via [pip](https://pypi.org/project/pip/):

   ```sh
   pip install iot-edge-logger
   ```

2. Import and say hello:

   ```python
   from iot.edge.logger import __version__


   print(f"hello world from iot-edge-logger version: {__version__}")
   ```

3. Basic usage:

   ```python
   from iot.edge.logger import init_logging

   # setup logging
   logger = init_logging(module_name="my_iot_module")


   logger.info("I am alive!")
   logger.warning("Plotting global takeover...")
   logger.error("Humans have become suspicious, shutting down")
   ```

4. Log output:

   ```sh
   <6> 2022-08-02 19:04:13,015 [INF] my_iot_module I am alive!
   <4> 2022-08-02 19:04:13,015 [WRN] my_iot_module Plotting global takeover...
   <3> 2022-08-02 19:04:13,015 [ERR] my_iot_module Humans have become suspicious, shutting down
   ```
