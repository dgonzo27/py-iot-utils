# iot-edge-logger

[![python version](https://img.shields.io/badge/python-v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python-v3.9-blue?logo=python&logoColor=yellow)

This package is a custom log formatter to standardize, collect and analyze logs from IoT Edge Devices in an Azure Log Analytics Workspace.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-edge-logger) | [Package PyPI](https://pypi.org/project/iot-edge-logger/)

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)
- [API Documentation](#api-documentation)
  - [Init Logging Method](#init-logging-method)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [Deployment Process](#deployment-process)

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

## API Documentation

### Init Logging Method

A custom logger to provide well formatted logging for a given IoT Edge Module - or any Python program.

```python
init_logging(
    module_name,
    level="DEBUG",
    format="<%(levelno)s> %(asctime)s [%(levelname)s] %(module_name)s %(message)s",
    datefmt=None,
    timespec="milliseconds",
    timezone="UTC",
)
```

**Parameters**

- `module_name` str

  The name of the IoT Edge module that is using this logger. Used for filtering and querying in log analytics - use "this_format_for_module".

- `level` Optional[str]

  The logging level. Default is "DEBUG".

- `format` Optional[str]

  The desired logging format. Default seen above.

- `datefmt` Optional[str]

  The desired date format. Default is None.

- `timespec` Optional[str]

  The time accuracy represented in log records. Default is "milliseconds".

- `timezone` Optional[str]

  The timezone represented in log records. Default is "UTC".

**Valid Timezones**

- US/Alaska

- US/Central

- US/Eastern

- US/Mountain

- US/Pacific

- UTC

**Returns**

Returns a logger object.

## Contributing

Contributions and suggestions are welcomed. However, there is a level of responsibility placed on the contributor to follow best-practices, provide thorough testing, follow the branching strategy, use the pull request template, and maintain a positive and coachable attitude when receiving feedback or questions on your code.

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` - as is standard with PyPI packages **It's important to note** that you must maintain the version with your releases in `iot/edge/logger/_version.py`, otherwise a new package version will fail to get published.

## Deployment Process

1. Linting, testing and building occurs when a pull request is made from a `features/*` branch to the `master` branch.

2. Deployments to PyPI occur when an approved user triggers the GitHub Action. If the version has not been updated, this deployment will fail.
