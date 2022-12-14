---
title: iot-lru-cache
---

# iot-lru-cache

[![python version](https://img.shields.io/badge/python_v3.9-blue?logo=python&logoColor=yellow)](https://www.python.org/) [![pre-commit](https://img.shields.io/badge/pre--commit-blue?logo=pre-commit&logoColor=FAB040)](https://pre-commit.com/) [![Keep a Changelog](https://img.shields.io/badge/keep_a_changelog-blue?logo=keepachangelog&logoColor=E05735)](https://keepachangelog.com/en/1.0.0/) [![CI_CD GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-blue?logo=githubactions&logoColor=black)](https://github.com/features/actions) [![package PyPI](https://img.shields.io/badge/PyPI-blue?logo=PyPI&logoColor=yellow)](https://pypi.org/)

This package is an implementation of a Least Recently Used (LRU) caching algorithm for optimized caching on an IoT edge device.

[Source code](https://github.com/dgonzo27/py-iot-utils/tree/master/iot-lru-cache) | [Package PyPI](https://pypi.org/project/iot-lru-cache/)

## Versioning

This repository adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). It will be maintained through the `CHANGELOG.md` and in GitHub Releases. **It's important to note** that you must maintain the version with your releases in `iot/lru/cache/_version.py`, otherwise a new package version will fail to get published.

## Getting Started

This section provides basic examples with the `iot-lru-cache`.

### Prerequisites

- Python 3.7 or later is required to use this package.

### Basic Examples

1. Install via [pip](https://pypi.org/project/pip/):

```sh
pip install iot-lru-cache
```

2. Import and say hello:

```python
from iot.lru.cache import __version__

print(f"hello world from iot-lru-cache version: {__version__}")
```

3. Basic usage:

```python
from iot.lru.cache import IoTLRUCache

# instantiate cache
cache = IoTLRUCache(capacity=100)

# print info w/ repr
print(f"{cache.__repr__()}")

# add a key-value pair to the cache
cache.put(key="my_key", value={"my": "value"})

# retrieve the value for a given key (returns -1 if not found)
val = cache.get(key="my_key")
```

## IoTLRUCache Class

A Least Recently Used (LRU) caching algorithm for optimized caching on an IoT edge device.

This class provides operations to get, and put key-value pairs of type `Any`.

```python
IoTLRUCache(capacity)
```

**Parameters**

- `capacity` int

  The number of key-value pairs to be stored in-memory before evicting on a LRU basis.

### Get Method

Retrieves the value of a key if it exists.

```python
cache.get(key)
```

**Parameters**

- `key` Any

  The key that should be used to retrieve its value.

**Returns**

Returns the key's value if it exists, -1 if it does not exist.

### Put Method

Update the value of a key if it exists, or simply adds the key-value pair to the cache.

```python
cache.put(key, value)
```

**Parameters**

- `key` Any

  The key in a key-value pair.

- `value` Any

  The value in a key-value pair.

**Returns**

Returns `None`.
