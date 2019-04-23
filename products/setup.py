#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='nameko-examples-products',
    version='0.0.1',
    description='Store and serve products',
    author='nameko',
    packages=find_packages(exclude=['test', 'test.*']),
    py_modules=['products'],
    install_requires=[
        "marshmallow==2.15.1",
        "nameko==2.11.0",
        "redis==2.10.5",
        "nameko-grpc==1.0.1",        
    ],
    extras_require={
        'dev': [
            "pytest==4.3.0",
            "coverage==4.5.2",
            "flake8==3.7.6",
            "black==19.3b0",
            "grpcio-tools==1.18.0",
            "isort==4.3.9",
        ]
    },
    zip_safe=True,
)
