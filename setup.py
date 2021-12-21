#!/usr/bin/env python

from setuptools import setup

setup(
    name="PythonPackageExample",
    version="1.0",
    description="Python Package Example",
    author="Rahul Pai",
    author_email="rahulpai@rocketmail.com",
    url="https://github.com/skarfie123/PythonPackageExample",
    packages=["package", "package.subpackage"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "pythonpackageexample = package.__main__:main",
        ]
    },
)
