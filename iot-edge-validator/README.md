# iot-edge-validator

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://img.shields.io/badge/PyPI-blue?logo=pypi&logoColor=yellow) [![azure-iot-device](https://img.shields.io/badge/azure_iot_device_v2.11.0-blue?logo=microsoft-azure&logoColor=black)](https://img.shields.io/badge/azure_iot_device-v2.11.0-blue?logo=microsoft-azure&logoColor=black)

This package is a wrapper around the [azure-iot-device](https://pypi.org/project/azure-iot-device/) SDK to provide standardized exception handling and direct method request validation.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-edge-validator) | [Package PyPI](https://pypi.org/project/iot-edge-validator/)

## Table of Contents

- [Versioning](#versioning)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Examples](#basic-examples)
- [Compare Dictionary Method](#compare-dictionary-method)
- [Format Exception Error Method](#format-exception-error-method)
- [Generate Error Response Method](#generate-error-response-method)

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` and in GitHub Releases. **It's important to note** that you must maintain the version with your releases in `iot/edge/validator/_version.py`, otherwise a new package version will fail to get published.

## Getting Started

This section provides basic examples with the `iot-edge-validator`.

### Prerequisites

- Python 3.7 or later is required to use this package.

- You must have an Azure subscription and Azure IoT Edge Device to use this package.

### Basic Examples

1. Install via [pip](https://pypi.org/project/pip/):

   ```sh
   pip install iot-edge-validator
   ```

2. Import and say hello:

   ```python
   from iot.edge.validator import __version__


   print(f"hello world from iot-edge-validator version: {__version__}")
   ```

3. Basic usage:

   ```python
   from typing import Any, Dict, Union

   from azure.iot.device.iothub.models.methods import MethodRequest, MethodResponse

   from iot.edge.validator import (
      format_exception_error,
      generate_error_response,
      compare_dictionary,
    )

   EXPECTED_METHOD_NAME: str = "some_method_name"

   EXPECTED_METHOD_PAYLOAD: Dict[str, Any] = {
       "some": {},
       "expected": {},
       "payload": {},
   }


   def validate_method_requests(method_request: MethodRequest) -> Union[MethodResponse, None]:
       """validation handler for some_method_name listener"""
       if method_request.name == EXPECTED_METHOD_NAME:
           pass
       else:
           return generate_error_response(method_request,
               f"received unknown method request for {method_request.name}",
               400,
           )


   def validate_some_method_name_request(method_request: MethodRequest) -> Union[MethodResponse, None]:
       """validation for expected payload of some_method_name direct method request"""
       # top level basic format validation
       error_msg = compare_dictionary(
           d1=method_request.payload,
           d2=EXPECTED_METHOD_PAYLOAD,
           value_match=False,
           recurse=False,
       )
       if error_msg:
           return generate_error_response(
               method_request, f"error parsing payload: {error_msg}", 400
           )
       return None
   ```

## Compare Dictionary Method

Compare two dictionaries for keys, optionally compare recursively and optionally compare for exact values to match.

```python
compare_dictionary(d1, d2, value_match=False, recurse=True)
```

**Parameters**

- `d1` Dict[str, Any]

  Dictionary to compare.

- `d2` Dict[str, Any]

  Dictionary to compare.

- `value_match` Optional[bool]

  Compare for exact values to match. Default is False.

- `recurse` Optional[bool]

  Recurse through sub dictionaries of the given dictionary. Default is True.

**Returns**

Returns a string - either empty or containing an error message.

## Format Exception Error Method

Format exceptions using traceback.

```python
format_exception_error(context, exception)
```

**Parameters**

- `context` str

  The context of where your program was when the execption occurred.

- `exception` Exception

  The caught exception.

**Returns**

Returns a string containing the formatted exception error and tracing.

## Generate Error Response Method

Given a method request, generate an error response.

```python
generate_error_response(request, message, status=500)
```

**Parameters**

- `request` azure.iot.device.iothub.models.method.MethodRequest

  The method request to use when generating the error response.

- `message` str

  The custom error message.

- `status` Optional[int]

  Error status code. Default is 500.

**Returns**

Returns a MethodResponse of type `azure.iot.device.iothub.models.methods.MethodResponse`.
