#!/usr/bin/env python

import os
import re

from setuptools import find_packages, setup

PACKAGE_NAME = "iot-samba-client"
PACKAGE_PPRINT_NAME = "IoT Samba Client"

package_folder_path = PACKAGE_NAME.replace("-", "/")


with open(os.path.join(package_folder_path, "_version.py"), "r") as version_file:
    version = re.search(
        r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', version_file.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("unable to find version information")


setup(
    name=PACKAGE_NAME,
    version=version,
    include_package_data=True,
    description=f"{PACKAGE_PPRINT_NAME} Library for Python",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT License",
    author="Dylan Gonzales",
    author_email="py.iot.utils@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    packages=find_packages(
        exclude=[
            "iot",
            "iot.samba",
            "tests",
        ]
    ),
    python_requires=">=3.7",
    install_requires=["smbprotocol==1.9.0", "pydantic==1.9.0"],
)
