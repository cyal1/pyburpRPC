#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import PyBurp

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="PyBurp",
    version="1.0.0",
    author="cyal1",
    packages=find_packages(),
    author_email="admin@example.com",
    description="The rpc server api of https://github.com/cyal1/BcryptMontoya",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyal1/PyBurpRpc/tree/main/python",
    py_modules=['PyBurp',"burpextender_pb2","burpextender_pb2_grpc"],
    install_requires=[
        "grpcio-tools==1.54.2",
        "grpcio==1.54.2",
        "protobuf==4.23.2"
        ],
    classifiers=[
    ],
)

